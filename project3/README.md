
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
