from app.routes.action import router as action_router
from app.routes.history import router as hand_history_router
from app.middlware.cors import add_cors

from fastapi import FastAPI

app = FastAPI()
add_cors(app)

app.include_router(hand_history_router, tags=["Hand History"])
app.include_router(action_router, tags=["Actions"])
