0x00. AirBnB clone - The console

General:
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

More Info:
Execution
Your shell should work like this in interactive mode:

##########################################################

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

##########################################################

But also in non-interactive mode: (like the Shell project in C)

##########################################################

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

##########################################################
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

description of the project:

----------------------------------------------------------
AirBnB: 
we make website
should it store data
execute command
save data and and reload it from files
----------------------------------------------------------

description of the command interpreter:

how to start it:
----------------------------------------------------------
you should know about:
How to serialize and deserialize a Class
How to manage datetime
UUID
*args
**kwargs
How to handle named arguments in a function

Read the greneral consept in the ^ above
----------------------------------------------------------

how to use it
----------------------------------------------------------

----------------------------------------------------------

examples
----------------------------------------------------------

----------------------------------------------------------
##########################################
#****************************************#
#************################************#
#************# THANK YOU !! #************#
#************################************#
#****************************************#
##########################################
