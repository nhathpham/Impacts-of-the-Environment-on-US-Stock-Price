# Impacts-of-the-Environment-on-US-Stock-Price
Goldman Sach Challenge, Texas A&M University Datathon 2021
https://tamudatathon.com/challenges/docs/goldman
Honorable Mention
Authors: Deep Desai, Nhat Pham, Rishabh Prasad

<h2>Inspiration:</h2>
- The stock market has always been a dynamic presentation of both economic activities and energy consumption across countries and economic sectors. Stock market activities are hence expected to have a significant effect on environment indicators such as CO2 emissions, greenhouse gas emissions etc.<br /> 
- Many studies find that weather has a close relationship with human’s mood and behavior. Hence, weather factors might also have an impact on stock return and trading volume.__
- We are interested in exploring how environment and weather indicators and stock markets are correlated and tied together. Our results can enable us to build models to predict risk events and discover investment opportunities based on environmental variations<br /> 

<h2>Final Product:</h2>
We created an interactive user interface that lets users choose environmental factors and industries to analyze. Then, by pulling corresponding data from the cloud database, the program will provide visualizations of pertinent information that communicates common trends between gas emissions or temperature and stock success by industry over the past 40 years. Find the tool in the file attached ('interface.py')

![tamu1](https://user-images.githubusercontent.com/87089936/143787404-dee67d9f-ea4f-4b2a-8607-652171dafa74.PNG)

![tamu2](https://user-images.githubusercontent.com/87089936/143787459-5be20eae-1623-4d76-9813-beac3d864b4d.PNG)

<h2>What we learned:</h2>
- Working with a new data warehouse platform and new data. None of us has worked with Snowflake before so it was a hurdle at the beginning to get used to the platform and extract data we need for our analysis. Yet it was a great learning experience as we all learned so much from looking into it together. Representatives from Goldman Sachs were very approachable and helpful with that too. We also built up our domain knowledge when researching the problem to understand and analyze the given financial and environmental data.<br /> 
- Work with big data and collaborative coding<br /> 
- Collaboration! Our team never met before and it was a bit challenging to communicate given different time zones and virtual-in-person situation. Yet we made a great team and helped each other learn a lot about technical knowledge, project management, and communication.<br /> 

 <h2>How we built your project:</h2>
Our first order of things was to get used to the data set and research the problem. Once we had defined our hypothesis, we familiarized ourselves with the Snowflake platform and unload data to Python for analysis. Next, we cleaned data, performed EDA, and decided on visualizations. After that we proceeded to build the interactive programming tool. And we finally ended the competition with testing and writing the reports. Further details are presented in the slide deck and video attached<br /> 

<h2>Insights:</h2>
Through our process of creating the demo and analysis of the data, we found a need to be concise and decisive about our decisions every step of the way. We discovered as data scientists the importance of exploring the data to its fullest and the impact it makes. Along the way, we realized that we need not be bogged down by all of the data, nor feel the need to analyze every single piece. Instead, our goal is to provide the briefest summary of the data that fully realizes what the dataset is about. We hope that our small tool can help the people working on this dataset to explore the relations between Environment and the Stock market without being overwhelmed by the wealth of information contained in each of these datasets. 


<h2>Challenges:</h2>
- Communication online/ in-person, plus (3) different timezones :)!<br /> 
- Unfamiliarity with new data storage platform<br /> 
- Deal with limitations in the dataset:<br /> 
+ Lack of data documentation in the data sources made it difficult to understand the variables and interpret the analysis results. We missed a few instances of data cleaning that were quite obvious to us late during the project. For example, there were some instances where the “High” in a single day was in the millions. Cross checking with the history online showed this to be obviously false. Similarly, when comparing to some of the indicators, some features like “Price” are averaged over entire years. This is a gross oversimplification of a sensitive market such as the stock market, but this is helpful in seeing a general trend.<br /> 
+ Environment indicators data were only available on a yearly estimates, while stock prices are volatile by day/hours. This makes it more challenging to correctly identify the correlation of these two factors.<br /> 

<h2>Future Work:</h2>
We hope to add further compatibility with dynamic plotting in the user interface for more visualizations. We also want to account for a larger set of environmental factors, including precipitation, humidity, and particulate matter. The ultimate goal is to generate more specific correlation matrix metrics to provide specific variable insights to users. <br /> 

  
<h2>Results Presentation:</h2> 
[https://www.youtube.com/watch?v=_cdxCKAJTA8](url)<br /> 
[https://docs.google.com/presentation/d/16zxH9t-UvXI2a-QQGV9KDtWtvMxwHxFZYTuhMgWxWCI/edit?usp=sharing](url)
