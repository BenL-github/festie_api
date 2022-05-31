from fastapi import FastAPI
from database import Database
from pydantic import BaseModel

db = Database()
app = FastAPI()

"""
STATE
"""

class State(BaseModel):
    state_name: str

"""
GENRE 
"""
class Genre(BaseModel):
    genre_name: str

"""
USER
"""
class User(BaseModel):
    f_name: str
    l_name: str
    email: str
    state_id: int

"""
FESTIVAL
"""
class Festival(BaseModel):
    festival_name: str
    price: int
    state_id: int

"""
ARTIST
"""
class Artist(BaseModel):
    artist_name: str
    genre_id: int

@app.on_event("shutdown")
def shutdown():
    db.close_connection()
    print("FastAPI shutdown")

""" States CRUD """

@app.get("/us-states")
def get_us_state():
    states = db.get_table("us_state")
    return states

@app.post("/us-states", status_code = 201)
def post_us_state(state: State):
    db.insert_us_state(state.state_name)
    return {"Entry":state.state_name}

@app.delete("/us-states")
def delete_us_state(state: State):
    db.delete_us_state(state.state_name)
    return {"Delete":state.state_name}

""" Genres CRUD """

@app.get("/genres")
def get_genre():
    genres = db.get_table("genre")
    return genres

@app.post("/genres", status_code = 201)
def post_genre(genre: Genre):
    db.insert_genre(genre.genre_name)
    return {"Entry":genre.genre_name}

@app.put("/genres/{genre_id}", status_code = 204)
def update_genre(genre_id: int, genre: Genre):
    db.update_genre(genre_id, genre.genre_name)

@app.delete("/genres/{genre_id}", status_code = 200)
def delete_genre(genre_id: int):
    db.delete_genre(genre_id)

""" Users CRUD """

@app.get("/users")
def get_user():
    users = db.get_table("app_user")
    return users

@app.post("/users", status_code = 201)
def create_user(user: User):
    db.create_user(user.f_name, user.l_name, user.email, user.state_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    db.update_user(user_id, user.f_name, user.l_name, user.email, user.state_id)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db.delete_user(user_id)

""" Festivals CRUD """

@app.get("/festivals")
def get_festival():
    festivals = db.get_table("festival")
    return festivals

@app.post("/festivals")
def create_festival(festival: Festival):
    db.create_festival(festival.festival_name, festival.price, festival.state_id)

@app.put("/festivals/{festival_id}")
def update_festival(festival_id, festival: Festival):
    db.update_festival(festival_id, festival.festival_name, festival.price, festival.state_id)

@app.delete("/festivals/{festival_id}")
def delete_festival(festival_id):
    db.delete_festival(festival_id)

""" Artists CRUD """

@app.get("/artists")
def get_artist():
    artists = db.get_table("artist")
    return artists

@app.post("/artists")
def create_artist(artist: Artist):
    db.create_artist(artist.artist_name, artist.genre_id)

@app.put("/artists/{artist_id}")
def update_artist(artist_id, artist: Artist):
    db.update_artist(artist_id, artist.artist_name, artist.genre_id)

@app.delete("/artists/{artist_id}")
def delete_artist(artist_id):
    db.delete_artist(artist_id)

""" Favorite Artists CRUD """

""" Artist Festivals CRUD """
