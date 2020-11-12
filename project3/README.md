
# Project 3: Hacker Vibes

### Group members: Alexander Quinto and Eric Chu

### Overview 
The implementation of the project will vary on the certain task we have to complete using the log file. Overall when parsing the file
to get the information regarding the user, you could possibly read through the file normally using .readlines(). Since there is 4 total data points, our first thought was to contain the information about a certain user in a dictionary that has a key that is a tuple that contains the user id and server they are associated to and the value would be another dictonary where its key would be the activity and the value is the date and time of the activity. 
An example of what we mean: 

```python  
  dict = {} 
  dict[(user_id, server_name)] = {}
  dict[(user_id, server_name)]["activity"] = "date and time" 
 ``` 
We arent sure if this would be the correct idea to use the following data structure to contain the information but this the the original idea we had when reading through the problem. The implementation of each of the logs we have to create will be explained further below. 

## Suspicious Activities
This problem would require us to keep track of the amount of times the user logs in per day and the date/time of each login, 
we can use loops to go through our data structure and count the amount of logs in per day and make sure the date/time of the login is between the times that we allow log in. 

To solve the issue of keeping track of total cases of suspicious activity, you could keep a counter that would us to keep track of the amount of suspicious activity that occurs per day for all users. The same logic could be applied for keeping track of the total number of cases of suspicious activity per day for one user. 

The time, activity, and server information could be sorted using the built in python sorted() function call 
The following problem could be solved in essentially one function although it might be a long one, it can also be split up into various amount to make the code more readable. 

## Irresponsible Behavior 
This problem would just require us to keep track of the amount of logins a certain user has and compare it against the amount of times that certain user has logged out of the system. 

The same logical would apply to keeping track of the total count of irresponsible activities and for the individual users as well. 
The following problem could be solved in essentially one function although it might be a long one, it can also be split up into various amount to make the code more readable. 
## System Glitch 
This problem would just be the opposite of what the irresponbile behavior does, so if the amount of times the user logged out doesnt match the amount of times the user logged in then we have a system glitch 

The following problem could be solved in essentially one function although it might be a long one, it can also be split up into various amount to make the code more readable. 
## Domain Count 
This problem would just require us to go through our data structure and create a dictionary that contains the domain as they key and the value for a key would the the number of users registered within that specific domain 

The following problem could be solved in essentially one function although it might be a long one, it can also be split up into various amount to make the code more readable. 

# **Week 2 Updates** 

### Parsing the file 
From the original idea that we had for the database, we had come up with the following idea: 
```python  
  dict = {} 
  dict[(user_id, server_name)] = {}
  dict[(user_id, server_name)]["activity"] = "date and time" 
 ``` 
 However, after some thought we decided that it would be better if we had a dictionary of tuples. 
 Where the key would represent the user and the value for each key would be a tuple of the server, activity and date/time
 ```python  
  dict = {} 
  tuple = (server, activity, date and time)
  dict[user] = tuple
 ``` 
 It is still important to understand that the data structure we use can change as we continue to implement our solution to our project. 
 
## Domain Count 
Using the database structure we defined above this problem wasn't that difficult, it was basically involved us going through our database and splitting the username at the character @ to create a new dictionary that contained the domain as the key and the value would be the number of users attached to that username. 

It involved a simple iteration through our database and just using String built in functions that allowed us to obtain the correct count for the information that we needed to get. 

## System Glitch and Irresponsible Behavior 
These two problem sets involved more of a thought process than domain count, our implementation using our database created above was not working the way we wanted to. Upon further discussion we decided to just create a whole new seperate database directly from parsing the file that could contain the number of times a user logged in or out per day. 
```python  
  dict = {} 
  dict[user] = {}
  dict[user][date] = (login count, logout count)
 ``` 
 We believe that using the following data structure for these two problems is going to allow us to get the desired output we want to write to our file. 
 
## Suspicious Activities
This problem is very similar to system glitch and irresponsible behavior with the difference of time being a factor. This is the problem we haven't fully tackled yet but we have a general idea as to how to approach it. We could follow the similar structure we did in irresponsible behavior and system glitch but account for the time criteria that is require for the activity to be considered suspicious. 


# **Week 3 Updates** 

### Parsing the file 
From the original idea that we had for the database, we had come up with the following idea for week 1: 
```python  
  dict = {} 
  dict[(user_id, server_name)] = {}
  dict[(user_id, server_name)]["activity"] = "date and time" 
 ``` 
 However, after some thought we decided that it would be better if we had a dictionary of tuples. 
 Where the key would represent the user and the value for each key would be a tuple of the server, activity and date/time for week 2 
 ```python  
  dict = {} 
  tuple = (server, activity, date and time)
  dict[user] = tuple
 ``` 
As we started to implement the project we found that our database wasn't ideal for getting the correct information that we wanted from the database in order to complete the tasks. The following database is what we settled on to implement the project:
```python  
  dict = {} 
  dict[user] = {}
  dict[user][date] = [[time, activity,server]]
 ``` 
 The reasoning behind this database is that we want to have a dictionary of dictionary where the key was the user that points to a date and then contains a list of lists that contain the time, activity and server names. If we encountered a user and date we entered into our database then we add the time, activity, and server name to our list as a list. Our original database design didn't account for duplicates due to the way we had implemented it and didn't contain all the information from the data file we parse.
 
 ### Suspicious Activities
 This problem was made much more doable given our new database, before we begin tackling the problem we have to sort our database given the time so once we write to a file we are able to have our times in accending order. In the method we will create a new database that will allow us to have the number of suspicious activity per user and the dates that the activity occurred. We iterate through the users and dates of our database, we then count the number of logins for that user and their number of activities that were between 12 AM and 5 AM by using .split(":") and converting it to an int and checking if it is between 0 and 5. We also use a counter to keep track of the total amount of suspicious activities. 
 
We then check if the number of logins is greater than 5 and if we had a suspicious login given the time constraints. If we do then we add that user to our suspicious database, which looks like: 
```python  
  sus = {} 
  sus[user] = []
  sus[user] = [count of sus activity for that user, [dates]]
 ``` 
 Once we create this database then we use it to create our report for suspicious activities. We iterate through and write to our file our total amount of cases of suspicious activity. We then for each user write the user and their number of cases. We use our original database to get our time, server and activty to write to our file. 
 
 ### Irresponsible Behavior
 to do
 ### System Glitch 
 to do
 
 ### Domain Count
This problem's implementation description has not changed from week 2, using the database structure we defined above this problem wasn't that difficult, it was basically involved us going through our database and splitting the username at the character @ to create a new dictionary that contained the domain as the key and the value would be the number of users attached to that username. 

It involved a simple iteration through our database and just using String built in functions that allowed us to obtain the correct count for the information that we needed to get and storing it inside a new dictionary that had a key which was the domain name and the value was the number of people who used that domain. We then iterated through that database and wrote to our file to create our report. 

### Errors
to do 
### Changes in Flowcharts
to do
