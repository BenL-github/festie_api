from fastapi import FastAPI
import database
from schemas import *
from routes import festival, us_states, genre, user, artist

# tags for documentation
tags_metadata = [
    {
        "name": "users",
        "description": "Manage users and their favorite artists"
    },
    {
        "name": "genres",
        "description": "Manage genres"
    },
    {
        "name": "artists",
        "description": "Manage artists and the festivals they play at"
    },
    {
        "name": "us_states",
        "description": "Manage States"
    },
    {
        "name": "festivals",
        "description": "Manage festivals and their prices"
    }
]

# init connection to PostgreSQL database
database.init()

# create FastAPI app
app = FastAPI(openapi_tags = tags_metadata)

# routes
app.include_router(us_states.router)
app.include_router(genre.router)
app.include_router(user.router)
app.include_router(festival.router)
app.include_router(artist.router)

@app.on_event("shutdown")
def shutdown():
    database.db.close_connection()
    print("FastAPI shutdown")
