# Microservices Workshop

The following apply to all APIs except the quote API.

The quote API simply returns the quote itself as the entire response body. It should be returned with the content type `text/plain`.

All other APIs should reply with the content type `application/json`.

## Object schemas

### User

    {
        "id": "user id",
        "name": "user name"
    }

### Room

    {
        "id": "room id",
        "name": "room name",
        "title": "room title"
    }

### Message

    {
        "id": "message id",
        "user": "user id",
        "room": "room id",
        "text": "message text"
    }

## API Conventions

### Collections

Collection APIs should return a JSON object containing a property at the root named after the object being returned. That property should contain an array of objects.

The URL should be the plural objects name.

Example:

    GET /users

    {
        "users": [
            {
                "id": "user id",
                "name": "user name"
            }
        ]
    }

Collections that allow filtering should do it through a query string.

Example: `/messages?room=<room id>`

### Items

APIs that return a single item should return the item directly.

Example:

    {
        "id": "user id",
        "name": "user name"
    }
