from fastapi import FastAPI, APIRouter
from database import Database
from schemas import *
from routes import us_states, genre

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

db = Database()
app = FastAPI(openapi_tags = tags_metadata)

app.include_router(us_states.router)
app.include_router(genre.router)

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

""" Users CRUD """

@app.get("/users", tags = ["users"])
def get_user():
    users = db.get_table("app_user")
    return users

@app.post("/users", tags = ["users"], status_code = 201)
def create_user(user: User):
    db.create_user(user.f_name, user.l_name, user.email, user.state_id)

@app.put("/users/{user_id}", tags = ["users"])
def update_user(user_id: int, user: User):
    db.update_user(user_id, user.f_name, user.l_name, user.email, user.state_id)

@app.delete("/users/{user_id}", tags = ["users"])
def delete_user(user_id: int):
    db.delete_user(user_id)

""" Favorite Artists CRUD """

@app.get("/users/{user_id}/favorite_artists", tags = ["users"])
def get_user_favorite_artist(user_id: int):
    favorite_artists = db.get_user_favorite_artist(user_id)
    return add_details(favorite_artists, ("artist_id", "artist_name", "rating"))

@app.post("/users/{user_id}/favorite_artists", tags = ["users"])
def create_favorite_artist(user_id: int, favorite_artist: CreateFavoriteArtist):
    db.create_favorite_artist(user_id, favorite_artist.artist_id, favorite_artist.score)

@app.put("/users/{user_id}/favorite_artists/{artist_id}", tags = ["users"])
def update_favorite_artist(user_id: int, artist_id: int, favorite_artist: UpdateFavoriteArtist):
    db.update_favorite_artist(user_id, artist_id, favorite_artist.score)

@app.delete("/users/{user_id}/favorite_artists/{artist_id}", tags = ["users"])
def delete_favorite_artist(user_id: int, artist_id: int):
    db.delete_favorite_artist(user_id, artist_id)

""" Festivals CRUD """

@app.get("/festivals", tags = {"festivals"})
def get_festival():
    festivals = db.get_table("festival")
    return festivals

@app.post("/festivals", tags = {"festivals"})
def create_festival(festival: Festival):
    db.create_festival(festival.festival_name, festival.price, festival.state_id)

@app.put("/festivals/{festival_id}", tags = {"festivals"})
def update_festival(festival_id, festival: Festival):
    db.update_festival(festival_id, festival.festival_name, festival.price, festival.state_id)

@app.delete("/festivals/{festival_id}", tags = {"festivals"})
def delete_festival(festival_id):
    db.delete_festival(festival_id)

""" Artists CRUD """

@app.get("/artists", tags = ["artists"])
def get_artist():
    artists = db.get_table("artist")
    return artists

@app.post("/artists", tags = ["artists"])
def create_artist(artist: Artist):
    db.create_artist(artist.artist_name, artist.genre_id)

@app.put("/artists/{artist_id}", tags = ["artists"])
def update_artist(artist_id: int, artist: Artist):
    db.update_artist(artist_id, artist.artist_name, artist.genre_id)

@app.delete("/artists/{artist_id}", tags = ["artists"])
def delete_artist(artist_id: int):
    db.delete_artist(artist_id)

""" Artist Festivals CRUD """

@app.get("/artists/{artist_id}/festivals", tags = ["artists"])
def get_artist_festival(artist_id: int):
    festivals = db.get_artist_festival(artist_id)
    return add_details(festivals, ("festival_id", "festival_name", "price", "state"))

@app.post("/artists/{artist_id}/festivals", tags = ["artists"])
def create_artist_festival(artist_id: int, artist_festival: CreateArtistFestival):
    db.create_artist_festival(artist_id, artist_festival.festival_id)

@app.delete("/artists/{artist_id}/festivals/{festival_id}", tags = ["artists"])
def delete_artist_festival(artist_id: int, festival_id: int):
    db.delete_artist_festival(artist_id, festival_id)

""" Fun Queries """

@app.get("/users/{user_id}/festival_match", tags = ["users"])
def get_user_festival_match(user_id: int):
    festivals = db.find_potential_festivals(user_id)
    return add_details(festivals, ("festival_name", "favorites_attending"))