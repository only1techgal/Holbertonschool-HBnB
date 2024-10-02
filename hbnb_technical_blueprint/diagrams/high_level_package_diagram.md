``` mermaid
    classDiagram
    class PresentationLayer {
        <<Interface>>
        +ServiceAPI()
    }
    class BusinessLogicLayer {
        +User()
        +Place()
        +Review()
        +Amenity()

    }
    class PersistenceLayer {
        +DatabaseAccess()
    }
    PresentationLayer --> BusinessLogicLayer : Facade Pattern
    BusinessLogicLayer --> PersistenceLayer : Database Operations
```
HIGH-LEVEL ARCHITECTURE.
As you navigate this code base, it is great to note the following concepts, while completing this project.

How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and de serialize a Class
How to write and read a J SON file
How to manage date time
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
