from fastapi import APIRouter
from schemas import State
import festie_api as api

router = APIRouter()

@router.get("/us_states", tags = ["us_states"])
def get_us_state():
    states = api.db.get_table("us_state")
    return states

@router.post("/us_states", tags = ["us_states"], status_code = 201)
def post_us_state(state: State):
    api.db.insert_us_state(state.state_name)
    return {"Entry":state.state_name}

@router.delete("/us_states", tags = ["us_states"])
def delete_us_state(state: State):
    api.db.delete_us_state(state.state_name)
    return {"Delete":state.state_name}