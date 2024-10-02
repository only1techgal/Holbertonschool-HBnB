``` mermaid

sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Persistence

    User->>API: Create new Place
    API->>BusinessLogic: Validate input
    BusinessLogic->>Persistence: Save Place to database
    Persistence-->>BusinessLogic: Place saved
    BusinessLogic-->>API: Return success response
    API-->>User: Place created successfully
```

API INTERACTION FLOW.

The Project Phase: The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, We will:

  Put in place a parent class(BaseMode) to take care of the intialization, serializatin and the deserialization of our future instances.
  Create a simoke flow od serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  create all classes used for AirBnb ()User, state , city, Place ..) that inherit from BaseMode1.
  create the first abstracted storage engine of the project: file Storage.
  create a data model
  Manage (create, update, destroy, etc) objects via a console/command interpreter, store and persit object to the files (JSON files).
