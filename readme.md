- ### <u>Auth:</u>
    - /auth/users/ - POST - Register new user
    - /auth/users/me/ - GET - See user details
    - /auth/token/login/ - POST - Get token  

- ### <u>Bookings:</u>
    ###### Must be logged in to access these endpoints
    - /api/bookings/ - GET - List of reservations
    - /api/bookings/ - POST - Reserve a table
    - /api/bookings/:id/ - GET - Table reservation details  

- ### <u>Menu:</u>
    ###### Must not be logged in to access
    - /api/menu/ - GET - List of Menu Items