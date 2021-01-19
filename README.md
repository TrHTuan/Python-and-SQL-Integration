# Python-and-SQL-Integration
This repository is to demonstrate how I would transfer file from Python to MySQL server.
The steps include:
- Import CSV file to Python, clean up these files if needed.
- Connect Python to MySQL server
- Create table(s) in MySQL server with columns (without data) to store the incoming information from Python
- Execute the 'Insert' command in MySQL through Python and create the loop for automatic addition of information from Python to MySQL

Of course, one big draw back of this loop function that is executed in Python is that it adds string values to the corresponding table in MySQL.
This means that when creating the corresponding table in MySQL server, you can't specify float / integer etc. data type for a specific column.
Thus, the accuracy of the incoming data from Python depends heavily on the clean up step in Python to make sure that any value within a column is of the same data type.

But, I like this method as I don't need to care about the data type in MySQL server if I'm confident in my clean up step in Python.
Specifically, I can just copy paste the code for table creation in MySQL server, modify it a bit without having to put too much thought to it.
Then I can just execute the loop function in Python and transfer every information as required to MySQL server.

Disclaimer: This isn't the only way to integrate Python and MySQL and certainly may not be the most effective way :P but it's my way and I'm proud of it, whether or not the approach is similar to other folks.
