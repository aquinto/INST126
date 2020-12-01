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
This method creates the head of the email html essentially. We pass in the user's choice, keyword and country. 
We are then able to use the user's choice to determine if they selected top headlines or get articles. 
We then create a string that will be the h1 of the email and return it at the end of the method. 

### createHTML
This method creates what will go inside of the body tag of the email html. Through the use of multi line string we are able 
to construct the html code that makes use of media object for the body of the email. We use custom css class from Bootstrap to provide some css to our html 
code than it just being plain html in our email with no styling. 

We have the database parameter which we use to gather the information such as the title, description and url to the article
we then construct the html and using a clickable link on the title that would re direct the user to the webpage of that given article.
Iterating through our database we are able to get the data from the article to create our html code. 

### sendEmail
This method allows us to send emails to the user with the information they selected inside the main() method. 
It takes in the html_body, email, country, keyword and choice as parameters, through the use of the MIMEMultipart python library
we are able to construct a message which contains a subject, from, and to fields. 

Using multi line strings we then construct a general html file which will be embedded within our email to display our data to
our user. Once we construct the html code for our email, we use the smtplib library to be able to send the email to the user 
through a gmail server that uses a personalized account. 

### main
This method handles the general code of what the user interact with. 
We ask the user for their input in which we then call the functions necessary that will handle the main portions 
of our project
