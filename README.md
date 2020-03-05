# Elections 2020
This repository is for the DS3 Projects Committee for Elections 2020. We will be using data regarding the upcoming 2020 elections and past elections to perform sentiment and time series analysis on Twitter data. We ultimately want to figure out if large events have swayed the public's opinion on presidential candidates. Using our findings, we will explain the outcome of past primaries and general elections, while predicting what it going to happen in this upcoming presidential election. 

**Outline**
1. Scrape tweets from Twitter using a Twitter search API 
2. Perform Twitter Sentiment Analysis on the tweets based on hashtag
    1. Categorize the tweets into positive, negative, or neutral sentiments using RNN and classification methods 
    2. Use Naive Bayes, k-NN, and SVM algorithms to test its accuracy
    3. Visualize the sentiments for each candidate (how many positive tweets were there, etc.)
3. Perform time series forecasting to predict how much sentiment for a candidate fluctuated after a certain large-scale event
    1. Compare the number of votes a candidate had before and after a large change in sentiment
        1. Do this using SVM and N. Networking
    2. Visualize outcomes with a summary tree
4. Analyze how much a change in sentiment affects the average number of votes a candidate obtains 
5. Conclude how public opinion affects voting outcomes for different candidates. 
  
