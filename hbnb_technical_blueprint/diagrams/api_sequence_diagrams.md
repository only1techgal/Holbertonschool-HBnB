``` mermaid

sequenceDiagram
    participant Client
    participant API_Server
    participant Database

    Client->>API_Server: POST /users/login (Credentials)
    API_Server->>Database: Validate credentials
    Database-->>API_Server: Success (User ID)
    API_Server-->>Client: 200 OK (Auth Token)

    Client->>API_Server: POST /places (Place Data, Auth Token)
    API_Server->>Database: Insert Place Record (With User ID)
    Database-->>API_Server: Success (Place ID)
    API_Server-->>Client: 201 Created (Place ID)

    Client->>API_Server: GET /places/:id (Auth Token)
    API_Server->>Database: Fetch Place Details (Place ID)
    Database-->>API_Server: Place Details
    API_Server-->>Client: 200 OK (Place Details)

    Client->>API_Server: DELETE /places/:id (Auth Token)
    API_Server->>Database: Delete Place (Place ID)
    Database-->>API_Server: Success
    API_Server-->>Client: 204 No Content
```

API INTERACTION FLOW.

The Project Phase: The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, We will:

  Put in place a parent class(BaseMode) to take care of the intialization, serializatin and the deserialization of our future instances.
  Create a simoke flow od serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  create all classes used for AirBnb ()User, state , city, Place ..) that inherit from BaseMode1.
  create the first abstracted storage engine of the project: file Storage.
  create a data model
  Manage (create, update, destroy, etc) objects via a console/command interpreter, store and persit object to the files (JSON files).
