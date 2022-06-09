from fastapi import APIRouter
from schemas import State
import main 

router = APIRouter()

@router.get("/us_states", tags = ["us_states"], status_code=200)
def get_us_state():
    states = main.db.get_table("us_state")
    return states

@router.post("/us_states", tags = ["us_states"], status_code = 201)
def post_us_state(state: State):
    main.db.insert_us_state(state.state_name)
    return {"Entry":state.state_name}

@router.delete("/us_states", tags = ["us_states"])
def delete_us_state(state: State):
    main.db.delete_us_state(state.state_name)
    return {"Delete":state.state_name}
