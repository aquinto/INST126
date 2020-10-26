
# Project 3 Hacker Vibes

### Group members: Alexander Quinto and Eric Chu

### Overview 
The implementation of the project will vary on the certain task we have to complete using the log file. Overall when parsing the file
to get the information regarding the user, you could possibly read through the file normally using .readlines(). Since there is 4 total data points, our first thought was to contain the information about a certain user in a dictionary that has a key that is a tuple that contains the user id and server they are associated to and the value would be another dictonary where its key would be the activity and the value is the date and time of the activity. 
An example of what we mean: 
> ` dict = {} 
  dict[(user_id, server_name)] = {}
  dict[(user_id, server_name)]["activity"] = "date and time" 
` 
We arent sure if this would be the correct idea to user the following date structure to contain the information but this the the original idea we had when reading through the problem. The implementation of each of the logs we have to create will be explained further below. 

## Suspicious Activities
This problem would require us to keep track of the amount of times the user logs in per day and the date/time of each login, 
we can use loops to go through our data structure and count the amount of logs in per day and make sure the date/time of the login is between the times that we allow log in. 

To solve the issue of keeping track of total cases of suspicious activity, you could keep a counter that would us to keep track of the amount of suspicious activity that occurs per day for all users. The same logic could be applied for keeping track of the total number of cases of suspicious activity per day for one user. 

The time, activity, and server information could be sorted using the built in python sorted() function call 

## Irresponsible Behavior 
This problem would just require us to keep track of the amount of logins a certain user has and compare it against the amount of times that certain user has logged out of the system. 

The same logical would apply to keeping track of the total count of irresponsible activities and for the individual users as well 
## System Glitch 
This problem would just be the opposite of what the irresponbile behavior does, so if the amount of times the user logged out doesnt match the amount of times the user logged in then we have a system glitch 

## Domain Count 
This problem would just require us to go through our data structure and create a dictionary that contains the domain as they key and the value for a key would the the number of users registered within that specific domain 
