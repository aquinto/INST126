# Project 4 Newsletter Application 

This is the fourth project for INST126 for the Fall 2020 semester at the University of Maryland.


## Description 

The goal of this project is to create an application where the user is able to search for any articles on a specific 
subject and has the ability to choose their source. Also, the application will be able to create a newsletter type format 
where the user can sign up to receive emails on the most popular topics on a certain subject or the top headlines for any given country. 


## Function Descriptions

### catchInformation 
This method takes in a type, keyword, and country which are all strings that will be used to determine how
the api calls will be made. Also it takes in a api variable as a parameter which is used to call the api and get
the information that we want from the api. 

If the type is "top headlines" then we use the .get_top_headlines() call from the api to get the top headlines 
for a given country that the user types in. We store this information inside a database dictionary that has a key value of 
a the title of the top headline article and the value is a list that contains the description of that article, url to that given article
and the url to that feature image of the article. 

If the type is "get articles" then we use the .get_everything() call from the api to get the most revelant articles
from a given keyword that the user provides and we store it inside a database that is a dictionary where the key is
the title of the article and the value is a list that contains the description of the article, url to the articles,
and the url to the feature image of the article 

## Future functions
There are still some function we have to think about that will help with the implementation of the project but so 
far we have the two functions listed on this README. 

### sendEmail()
This function will be able to send an email to any given user through python. It is in current developmenet. 

# Update 2 

## Function Descriptions

### catchInformation 
This method takes in a type, keyword, and country which are all strings that will be used to determine how
the api calls will be made. Also it takes in a api variable as a parameter which is used to call the api and get
the information that we want from the api. 

If the type is "top headlines" then we use the .get_top_headlines() call from the api to get the top headlines 
for a given country that the user types in. We store this information inside a database dictionary that has a key value of 
a the title of the top headline article and the value is a list that contains the description of that article, url to that given article
and the url to that feature image of the article. 

If the type is "get articles" then we use the .get_everything() call from the api to get the most revelant articles
from a given keyword that the user provides and we store it inside a database that is a dictionary where the key is
the title of the article and the value is a list that contains the description of the article, url to the articles,
and the url to the feature image of the article 

### createHeadEmail 

### createHTML

### sendEmail

### main
