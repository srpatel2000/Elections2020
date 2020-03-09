# Elections 2020
This repository is for the DS3 Projects Committee for Elections 2020. We will be using data regarding the upcoming 2020 elections and past elections to perform sentiment and time series analysis on Twitter data. We ultimately want to figure out if large events have swayed the public's opinion on presidential candidates, thus affecting the number of votes. Using our findings, we will find the extent to which public mood affects voting turnouts. 

**Outline**
1. Scrape tweets from Twitter using a Twitter search API 
2. Perform Twitter Sentiment Analysis on the tweets based on query search
    1. Categorize the tweets into positive, negative, or neutral sentiments using OpinionFinder and Twitter Emotion Recognition  
    2. Recognize it's accuracy from the sources
    3. Visualize the sentiments for each candidate with graphs and word cloud(how many positive tweets were there, etc.)
3. Perform time series forecasting to predict how much sentiment for a candidate fluctuated after a certain large-scale event based on the number of tweets about a candidate
    1. Compare the sentiment towards a candidate before and after a large change in sentiment
        1. Do this using Granger causality analysis in order to prove causality
    2. Visualize outcomes 
4. Analyze how much a change in sentiment affects the average number of followers a candidate obtains on Twitter
    1. Predict follower count based on sentiment using a Self-organizing Fuzzy Neural Network (SOFNN) model
5. Is there a correlation between the number of followers a candidate has with the number of votes they received? 
    1. Prove causation with Granger causality analysis 
    
**Credits**

  
