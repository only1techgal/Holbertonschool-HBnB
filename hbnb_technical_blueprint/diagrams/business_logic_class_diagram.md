``` mermaid 
classDiagram
    class BaseModel {
        -id: string
        -created_at: datetime
        -updated_at: datetime
        +save(): void
        +to_json(): dict
    }

    class User {
        -email: string
        -password: string
        -name: string
    }

    class Place {
        -location: string
        -price: float
        -description: string
    }

    class Review {
        -rating: int
        -comments: string
    }

    class Amenity {
        -name: string
    }

    class FileStorage {
        +all(): dict
        +save(obj): void
        +reload(): void
    }

    BaseModel <|-- User
    BaseModel <|-- Place
    BaseModel <|-- Review
    BaseModel <|-- Amenity
    FileStorage --> BaseModel : stores
```



















BUSINESS LOGIC LAYER Files and Directories

Models directory will contain all classes used for the entire project. 
a class, called "model" in an OPP project is the presentation of an object/instance tests directoru will contain all unit tests. 
console.py file is the entity point of our command interpreter. models/base_model.py file is the base class of all our models.

THIS WILL CONTAIN ELEMENTS: 
> attributes: id, (created and updated) >methods: Save() and to_json()
> models/engine directory will contain all storage classes (using the same prototype).
> we will have only one: file_stora
