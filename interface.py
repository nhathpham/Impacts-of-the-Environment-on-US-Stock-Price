import argparse

import os
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper

sectors = ['Consumer Cyclical', 'Financial', 'Technology', 'Pharmaceuticals', 'Financial Services', 'Industrials', 'Basic Materials', 'Conglomerates', 'Services', 'Industrial Goods', 'Consumer Defensive', 'Communication Services', 'Real Estate', 'Utilities', 'Media', 'Energy', 'Healthcare', 'Building']
indicators = ['co2', 'ghg', 'temp']

sectors_dict = dict(zip(range(1, len(sectors)+1), sectors))

indicators_dict = dict(zip(range(1, len(indicators)+1), indicators))

sector_helper = ""
for i in sectors_dict.keys():
	sector_helper += f"{i}. {sectors_dict[i]}\n"
	
parser = argparse.ArgumentParser(description="interface for plotting Environment and Stock data", add_help=True)

parser.add_argument('output_path', action = 'store', metavar = 'path', type = str, help='path to output folder where plots are generated')
parser.add_argument('indicator', action = 'store', metavar = 'indicator', type = int, choices = range(1, len(indicators_dict)+1), help = '1. CO2 Emmissions\n2. Greenhouse Gas Emmissions\n3. Temperature (F)')
parser.add_argument('sector', action = 'store', metavar = 'sector', type = int, choices = range(1, len(sectors)+1), help = sector_helper)

args = parser.parse_args()

if not os.path.isdir(args.output_path):
    os.mkdir(args.output_path)
    print('The output path has been created')
    


def get_df(df, string):
    df_new = df.loc[df["Indicator Name"] == "Total including LUCF"]
    gas_type = ""
    if string.lower() == 'co2':
        gas_type = "Carbon dioxide"
    elif string.lower() == 'ghg':
        gas_type = "All Green house gases"
    df_new = df_new.loc[df_new["Gases Name"] == gas_type]
    df_new['Date'] = pd.to_datetime(df_new.Date, format='%Y-%m-%d')
    df_new = df_new.loc[df_new["Location Name"] == "World"].reset_index()
    return df_new

def plot_temp():
    pass

def plot_emissions(df, type):
    print("\nCreating lineplot for sector...\n")
    if (type == "temp"):
        plot_temp()
        return
    plt.figure()
    df_spec = get_df(df, type.lower())
    plt.plot(df_spec["Date"], df_spec["Value"])
    plt.title(type + " Emissions in US for 1990-2018")
    plt.xlabel("Year")
    plt.ylabel("Volume Emitted (" + df_spec["Units"][0] + ")")
    print("\nShowing plot for emissions...\n")
    plt.show()
    file_name = type + "_emissions_line.png"   
    file_name = os.path.join(args.output_path, file_name)
    plt.savefig(file_name, bbox_inches='tight')
    print("\nSaved plot to given path.\n")

def get_stocks_by_sector(sector):
    stocks_by_sector = stocks.loc[stocks["SECTOR"] == sector].reset_index()
    stocks_by_sector["Date"] = pd.Series([""]*len(stocks_by_sector))
    for i in range(len(stocks_by_sector)):
    #     print(type(stocks_by_sector["YEAR(DATE)"][i]))
    #     stocks_by_sector["Date"][i] = stocks_by_sector["YEAR(DATE)"][i] + "-01-01"
        stocks_by_sector["Date"][i] = pd.to_datetime(str(stocks_by_sector["YEAR(DATE)"][i]) + "0101", format='%Y%m%d')
    stocks_by_sector = stocks_by_sector.loc[stocks_by_sector["YEAR(DATE)"] >= 1990].loc[stocks_by_sector["YEAR(DATE)"] <= 2018]
    return stocks_by_sector

def boxplot_by_sector(sector, value):
    print("\nCreating boxplot for sector...\n")
    stocks_by_sector = get_stocks_by_sector(sector)
#     stocks_by_sector = stocks_by_sector.loc[stocks_by_sector["YEAR(DATE)"] >= 1990].loc[stocks_by_sector["YEAR(DATE)"] <= 2018]
    plt.figure(figsize=(16,6))
    # plt.figure(2)
    # plt.plot(stocks_by_sector["YEAR(DATE)"], stocks_by_sector["SUM(STOCK_HISTORY.VOLUME)"])
    if value == "SUM(STOCK_HISTORY.VOLUME)":
        sns.boxplot(stocks_by_sector["YEAR(DATE)"], np.log(stocks_by_sector[value]))
    elif value == "AVG(STOCK_PRICE)":
        sns.boxplot(stocks_by_sector["YEAR(DATE)"], np.log((np.array(stocks_by_sector["AVG(STOCK_HISTORY.LOW)"]) + np.array(stocks_by_sector["AVG(STOCK_HISTORY.HIGH)"])) / 2))
    plt.xlabel('Year', fontsize=12)
    if value == "SUM(STOCK_HISTORY.VOLUME)":
        ylabel = 'Total Volume of Shares ($)'
        plt.ylabel(ylabel, fontsize=12) # Log-transforming to make the trend clearer, as the distribution is heavily positively skewed
    elif value == "AVG(STOCK_PRICE)":
        ylabel = 'Average Price of Shares ($)'
#         ylabel = "Average"
        plt.ylabel(ylabel, fontsize=12) # Log-transforming to make the trend clearer, as the distribution is heavily positively skewed
    title = 'Stock Performance per Year in ' + sector + ' Sector, 1990-2021'
    plt.xticks(rotation=45)
    plt.title(title, fontsize=16)
    print("\nShowing boxplot by sector...\n")
    plt.show()
    file_name = sector + "_" + value + "_boxplot.png"  
    file_name = os.path.join(args.output_path, file_name)
    plt.savefig(file_name, bbox_inches='tight')
    print("\nSaved boxplot to given path.\n")

df = pd.read_csv("global_ghg_co2.csv", parse_dates=True)
stocks = pd.read_csv("stocks.csv", parse_dates = True)

# if not os.path.isdir("images"):
#     os.mkdir("images")

plot_emissions(df, indicators_dict[args.indicator])
boxplot_by_sector(sectors_dict[args.sector], value="AVG(STOCK_PRICE)")
boxplot_by_sector(sectors_dict[args.sector], value="SUM(STOCK_HISTORY.VOLUME)")

