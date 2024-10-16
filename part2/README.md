HBnb
==== 

This is the first segment of the HBnb project that will cover fundamental concepts of Higher level learning programming. The main goal is to evnetually deploy our server a simple ccopy of AirBnb Website. A command interpreter is created in this segment to manage objects of the AirBnB Website.

FUNCTIONALITIES OF THIS COMMAND INTERPRETER:
============================================

1. Create a new object(new user, or new place)
2. Retrieve an object from a file.(Database)
3. Do operations on objects( count, compute stats)
4. update attributes of an object
5. Destroy an object

TABLE OF CONTENTS
=================

1. ENVIRONMENT
2. INSTALATION
3. FILE DESCRIPTION
4. USUAGE
5. EXAMPLES OF USE
6. BUGS
7. AUTHORS
8. LICENSE

ENVIRONMENT
===========

This project is interpreted/tested in Ubuntu 14.4 LTS using python 3(version 3.4.3)

FILE DESCRIPTION
================

console.py - the console contains the entry point of the command interpreter.

LISTS OF COMMANDS THIS CONSOLE SUPPORTS:
========================================
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
==================================
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

/tests_models/test_base_model.py- contains the TestBaseModel and TestBaseModelDocs classes TestBaseModelDocs Class:

def setUpClass(cls) - Set up for the doc tests
def test_pep8_conformance_base_model(self)- Test that models/base_model.py conforms to PEP8
def test_pepe8_conformance_test_base_model(self)- Test that tests/tes_models/test_base_model.py conforms to PEP8
def test_bm_module_docstring(self)- Test for the base_model.py module docstring
def test_bm_func_docstrings(sekf) - Test for the presence of docstrings in BaseModel methods

TestBaseModel clas;
===================

def test_is_base_model(self) - Test that the instatiation of a BaseModel works
def test_created_at_instatiation(self) - Test Created_at is a pub.instance attribute of type detetime
def test_updated_at_instantiation(self)- Tested updated_at is a pub.instance attribute of type datetime
def test_diff_datetime_objs(self)- Test that two BaseModel instances have differenct datetime objects.

/test_models/test_amenity.py- Contains the TestAmenityDocs class:
def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_amenity(self) - Test that models/amenity.py conforms to PEP8
    def test_pep8_conformance_test_amenity(self) - Test that tests/test_models/test_amenity.py conforms to PEP8
    def test_amenity_module_docstring(self) - Test for the amenity.py module docstring
    def test_amenity_class_docstring(self) - Test for the Amenity class docstring

/test_models/test_city.py - Contains the TestCityDocs class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_city(self) - Test that models/city.py conforms to PEP8
    def test_pep8_conformance_test_city(self) - Test that tests/test_models/test_city.py conforms to PEP8
    def test_city_module_docstring(self) - Test for the city.py module docstring
    def test_city_class_docstring(self) - Test for the City class docstring

/test_models/test_file_storage.py - Contains the TestFileStorageDocs class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_file_storage(self) - Test that models/file_storage.py conforms to PEP8
    def test_pep8_conformance_test_file_storage(self) - Test that tests/test_models/test_file_storage.py conforms to PEP8
    def test_file_storage_module_docstring(self) - Test for the file_storage.py module docstring
    def test_file_storage_class_docstring(self) - Test for the FileStorage class docstring

/test_models/test_place.py - Contains the TestPlaceDoc class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_place(self) - Test that models/place.py conforms to PEP8.
    def test_pep8_conformance_test_place(self) - Test that tests/test_models/test_place.py conforms to PEP8.
    def test_place_module_docstring(self) - Test for the place.py module docstring
    def test_place_class_docstring(self) - Test for the Place class docstring

/test_models/test_review.py - Contains the TestReviewDocs class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_review(self) - Test that models/review.py conforms to PEP8
    def test_pep8_conformance_test_review(self) - Test that tests/test_models/test_review.py conforms to PEP8
    def test_review_module_docstring(self) - Test for the review.py module docstring
    def test_review_class_docstring(self) - Test for the Review class docstring

/test_models/state.py - Contains the TestStateDocs class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_state(self) - Test that models/state.py conforms to PEP8
    def test_pep8_conformance_test_state(self) - Test that tests/test_models/test_state.py conforms to PEP8
    def test_state_module_docstring(self) - Test for the state.py module docstring
    def test_state_class_docstring(self) - Test for the State class docstring

/test_models/user.py - Contains the TestUserDocs class:

    def setUpClass(cls) - Set up for the doc tests
    def test_pep8_conformance_user(self) - Test that models/user.py conforms to PEP8
    def test_pep8_conformance_test_user(self) - Test that tests/test_models/test_user.py conforms to PEP8
    def test_user_module_docstring(self) - Test for the user.py module docstring
    def test_user_class_docstring(self) - Test for the User class docstring

Documented commands (type help <topic>):
========================================
EOF all create/ destroy/help/quit/show/update

Bugs
====

No known bugs at this time.

Authors
=======

Keketso Nchai - Github(klehloenya) (keketsolehloenya516@gmail.com) 
Lemohang Lipholo - Github(only1techgal) (jenn.lipholo@gmail.com)



