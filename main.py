from fastapi import FastAPI, APIRouter
from database import Database
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
db = Database()
# create FastAPI app
app = FastAPI(openapi_tags = tags_metadata)

# routes
app.include_router(us_states.router)
app.include_router(genre.router)
app.include_router(user.router)
app.include_router(festival.router)
app.include_router(artist.router)

def add_details(query_result, details):
    """
    Add details to the results of a database query

    :query result: result of the database query
    :details: a tuple containing attribute names for each item in query result
    """
    detailed_list = []
    for item in query_result:
        detailed_item = {}
        for i, value in enumerate(item):
            detailed_item[details[i]] = value
        detailed_list.append(detailed_item)
    return detailed_list

@app.on_event("shutdown")
def shutdown():
    db.close_connection()
    print("FastAPI shutdown")
