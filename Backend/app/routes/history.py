from fastapi import APIRouter, Depends
from app.database import get_db
from app.repositories.history import HistoryRepository
from app.service.history import HistoryService

router = APIRouter()

@router.get("/hand-history")
def get_actions(db=Depends(get_db)):
    service: HistoryService = HistoryService(HistoryRepository(db))
    return service.fetch_all_history()