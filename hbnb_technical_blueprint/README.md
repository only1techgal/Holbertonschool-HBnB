

INTRODUCTION.
The Holberton HBnB sums up the implementation of my four months of studies at the Holberton School - the fullstack software engineering program. The goal of the project is to deploy a replica of the Airbnb Website using my server. The final version of this project will have:

> A command interpreter to manipulate data without a visual interface, like a shell( for developemt and debugging a website (front-end) with static and dynamic functionalities.
> A comprehensive database to manage the backend functionalities
> An API that provides a communication inteface between the front and backenf of the stystem.

  
HIGH-LEVEL ARCHITECTURE.
As you navigate this code base, it is great to note the following concepts, while completing this project.

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


BUSINESS LOGIC LAYER
Files and Directories
> Models directory will contain all classes used for the entire project.
> a class, called "model" in an OPP project is the presentation of an object/instance
> tests directoru will contain all unit tests.
> console.py file is the entity point of our command interpreter.
> models/base_model.py file is the base class of all our models.

THIS WILL CONTAIN ELEMENTS:
    > attributes: id, (created and updated)
    >methods: Save() and to_json()
    models/engine directory will contain all storage classes (using the same prototype). we will have only one: file_storage.py.

API INTERACTION FLOW.

The Project Phase:
The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, We will:

1. Put in place a parent class(BaseMode) to take care of the intialization, serializatin and the deserialization of our future instances.
2. Create a simoke flow od serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnb ()User, state , city, Place ..) that inherit from BaseMode1.
4. create the first abstracted storage engine of the project: file Storage.
5. create a data model
6. Manage (create, update, destroy, etc) objects via a console/command interpreter, store and persit object to the files (JSON files).
7. 
    

