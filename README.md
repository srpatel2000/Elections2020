# Elections 2020
This repository is for the DS3 Projects Committee for Elections 2020. We will be using data regarding the upcoming 2020 elections and past elections to perform sentiment and time series analysis on Twitter data. We ultimately want to figure out if large events have swayed the public's opinion on presidential candidates, thus affecting the number of votes. Using our findings, we will find the extent to which public mood affects voting turnouts. In this project, we will be focusing on five candidates: Donald Trump, Joe Biden, Bernie Sanders, Mike Bloomberg, and Elizabeth Warren. 

**Outline**
1. Scrape tweets from Twitter using a Twitter search API 
    1. Visualize most common words said about candidates using a word cloud
2. Perform Twitter Sentiment Analysis on the tweets based on query search before, day of, and after the most viewed Democratic debate. (9th Dem Debate b/c that was the most viewed debate)
    1. Categorize the tweets into positive, negative, or neutral sentiments using Naive Bayes classifier module from NLTK 
    2. Recognize its accuracy
        1. Test out other methods (Multinomial Naive Bayes, Bernoulli Naive Bayes, Logistic Regression, Stochastic Gradient Descent and Support Vector Classifier) if the accuracy is not adequate --> Future goal to get done this spring break.
    3. Visualize the changing sentiments for each candidate with graphs 
3. Visualize the endorser number for each candidate to see what kinds of people endorse the certain candidates
    1. Visualize with grouped bar chart
4. Compare the sentiment of a candidate before and after the ninth Democratic Debate with the types of endorsers. This will answer the question: Is there a correlation between the type of endorser a candidate has with the sentiment of their tweets?
    1. Visualize sentiment and number of tweets together in a joint plot with seaborn
    2. Perform causality analysis to determine whether endorsers affect the overall sentiment surrounding a candidate
        1. If there is a causal relationship, determine the extent to which certain endorsers affect sentiment. Do this with a neural network algorithm. --> Future goal to get done this spring break. 
    
**Credits**

  
