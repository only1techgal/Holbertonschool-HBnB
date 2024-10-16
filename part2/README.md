HBnb 

This is the first segment of the HBnb project that will cover fundamental concepts of Higher level learning programming. The main goal is to evnetually deploy our server a simple ccopy of AirBnb Website. A command interpreter is created in this segment to manage objects of the AirBnB Website.

FUNCTIONALITIES OF THIS COMMAND INTERPRETER:

1. Create a new object(new user, or new place)
2. Retrieve an object from a file.(Database)
3. Do operations on objects( count, compute stats)
4. update attributes of an object
5. Destroy an object

TABLE OF CONTENTS

1. ENVIRONMENT
2. INSTALATION
3. FILE DESCRIPTION
4. USUAGE
5. EXAMPLES OF USE
6. BUGS
7. AUTHORS
8. LICENSE

ENVIRONEMMT

This project is interpreted/tested in Ubuntu 14.4 LTS using python 3(version 3.4.3)

FILE DESCRIPTION

console.py - the console contains the entry point of the command interpreter. 
LISTS OF COMMANDS THIS CONSOLE SUPPORTS:
1. EOF - exit console
2. quite - exits console
<emptyline> - overwrites default emptyline method and does nothing.
3. create - Creates an instance based on the class name and id(to JSON file) and prints id.
4. Destroy - Deletes an instance based on the class name and id(Save the change into the JSON file.)
5. Show - Prints the string representation of an instance based on the class name and id.
6. Update - Updates an instance based on the classs name and id by adding or updating attributes(save the change into a JSON file)

modeles/directory contains classes used for this project:

base_model.py - The BaseModel class from which fute classes will be derived

def__int__(self, *args, *kwargs) - initialization of the base model
def__str__(self) - String representation of the BaseModel class
def save(self) - Updates the atrribute updated_at with the current datetime
def to_Dict(self) - returns a dictionary containing all keys/values of  the instance

Classes inherited from Base Model:
1. amenity.py
2. city.py
3. place.py
4. review.py
5. state.py
6. user.py

/models/engine directory contains file Storage that handles JSON serialization and deserilization:

file_storage.py - serialises instances to a JSON file and deserialise back to instances

def all(self) - returns the dictionary_objects
def new(self, obj) - sets in_objects the obj with key.id
def save(self) - serializes_object to the JSON file(path:__file_path)
def reload(sefl)- deserializes the JSON file to__objects

/tests dierctory contains all unit test cases for this project:



