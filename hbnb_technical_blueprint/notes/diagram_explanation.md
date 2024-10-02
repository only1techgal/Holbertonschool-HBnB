# Explanatory Notes for High-Level Package Diagram


- **Purpose of the Diagram**: This diagram illustrates the layered architecture of the HBnB application, highlighting the interaction between the presentation, Business Logic, and Persistance Layers. 
- **Key Components**:
    - **PresentationLayer**: Acts as an interface for the Service API.
    - **BusinessLogicLayer**: Contains core business entities such as User, Place, Review, and Amenity.
    - **PersistenceLayer**: Responsible for the database access.
    - **Design Decisions**: The use of the Facade Pattern simplifies interactions between layers, promoting a clean separation of concerns.
    