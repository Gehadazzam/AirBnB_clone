# The AirBnB Clone Project
![The AirBnB Clone Project](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1280px-Airbnb_Logo_B%C3%A9lo.svg.png)
# 0x00. AirBnB clone - The console <topic>

## Project Description:
This project is a command-line interpreter designed to emulate a simplified version of an Airbnb clone. It allows users to interact with the system by executing various commands to create, update, delete, and display objects. The interpreter is built using Python and utilizes the cmd module for command handling.

---

## General:
1. How to create a Python package
2. How to create a command interpreter in Python using the cmd module
3. What is Unit testing and how to implement it in a large project
4. How to serialize and deserialize a Class
5. How to write and read a JSON file
6. How to manage datetime
7. What is an UUID
8. What is *args and how to use it
9. What is **kwargs and how to use it
10. How to handle named arguments in a function

---

## More Info

### Execution

#### Your shell should work like this in interactive mode:

```
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
```
----------------------------------------------------------
#### But also in non-interactive mode: (like the Shell project in C)

```
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
```
----------------------------------------------------------
#### All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
----------------------------------------------------------
## Command Interpreter Description
The command interpreter provides a user-friendly interface for interacting with the system. It supports the following commands:

- create: Creates a new instance of a specified class.
- show: Displays the string representation of a specified instance.
- update: Updates attributes of a specified instance.
- destroy: Deletes a specified instance.
- all: Displays string representations of all instances or all instances of a specified class.
- quit: Exits the command interpreter.
- EOF: Exits the command interpreter (Ctrl + D).
- count: Retrieves the number of instances of a specified class.
----------------------------------------------------------

### description of the command interpreter

#### how to start it
----------------------------------------------------------
How to Start
To start the command interpreter, follow these steps:

> 1. Clone the repository to your local machine.
> 2. Navigate to the project directory.
> 3. Run the main script "console.py" using Python.
```
python ./console.py
```
----------------------------------------------------------

#### how to use it
----------------------------------------------------------
Once the command interpreter is started, you can enter commands following the syntax:
```
(class name).(command)([arguments])
```

For example:
```
User.create()
User.update("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8", {'first_name': "John", "age": 89})
User.show("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8")
User.destroy("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8")
User.all()
User.count()
```
----------------------------------------------------------

#### Examples
----------------------------------------------------------
Creating a new User instance:
```
User.create()
```
Updating attributes of a User instance:
```
User.update("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8", {'first_name': "John", "age": 89})
```
Showing details of a User instance:
```
User.show("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8")
```
Deleting a User instance:
```
User.destroy("e09d0e1d-a2a4-4615-8854-6f73b9dfe1a8")
```
Displaying all User instances:
```
User.all()
```
Counting the number of User instances:
```
User.count()
```
----------------------------------------------------------

## THANK YOU !!