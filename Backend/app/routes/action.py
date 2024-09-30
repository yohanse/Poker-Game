from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.action.allin import AllInAction
from app.action.bet import BetAction
from app.action.burn import BurnAction
from app.action.call import CallAction
from app.action.check import CheckAction
from app.action.deal import DealAction
from app.action.rraise import RaiseAction
from app.dtos.params import Params
from app.database import get_db
from app.exceptions.game_exception import ActionCanNotPerformException, InvalidInputException
from app.repositories.action import ActionRepository
from app.repositories.hand import HandRepository
from app.service.action import ActionService
from app.service.over import OverService
from app.service.start import StartService
from app.action.fold import FoldAction


router = APIRouter()

class ActionRequest(BaseModel):
    action_type: str
    hand_id: Optional[str] = None
    stack: Optional[int] = None
    amount: Optional[int] = None


@router.get("/game/over", response_model=Dict[str, Any])
def over_game(hand_id: str, db=Depends(get_db)) -> List[Dict[str, Any]]:
    try:
        service: OverService = OverService(HandRepository(db))
        return service.over(hand_id)
    
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"Error: {error}")


@router.post("/game/start", response_model=Dict[str, Any])
def start_game(stack: int, db=Depends(get_db)) -> List[Dict[str, Any]]:
    service: StartService = StartService(HandRepository(db))
    return service.start_game(stack)


@router.post("/game/actions", response_model= Dict[str, Any])
def perform_action(action: ActionRequest, db=Depends(get_db)) -> Dict[str, Any]:

    action_type: str = action.action_type
    stack: Optional[int]  = action.stack
    amount: Optional[int] = action.amount
    hand_id: Optional[str] = action.hand_id
    
    try:
        params: Params = Params(stack=stack, amount=amount, hand_id=hand_id, action_string=action_type)
        service: ActionService = ActionService(action_repository=ActionRepository(db), hand_repository=HandRepository(db))

        if action_type == "fold":
            return service.process_game(params, FoldAction())
        
        if action_type == "call":
            return service.process_game(params, CallAction())
        
        if action_type == "check":
            return service.process_game(params, CheckAction())
        
        if action_type == "burn":
            return service.process_game(params, BurnAction())
        
        if action_type == "deal":
            return service.process_game(params, DealAction())
        
        if action_type == "bet":
            return service.process_game(params, BetAction())
        
        if action_type == "raise":
            return service.process_game(params, RaiseAction())
        
        if action_type == "allin":
            return service.process_game(params, AllInAction())
            
        
        raise InvalidInputException(f"Invalid action_type: {action_type}")

    except ActionCanNotPerformException as error:
        raise HTTPException(status_code=400, detail=f"Action cannot be performed: {error.message}")
    
    except InvalidInputException as error:
        raise HTTPException(status_code=422, detail=f"Invalid input: {error.message}")



@router.get("/game/actions", response_model=dict[str, bool])
def avaliable_actions(hand_id: str, db=Depends(get_db)) -> dict[str, bool]:
    service: ActionService = ActionService(action_repository=ActionRepository(db), hand_repository=HandRepository(db))
    over: OverService = OverService(HandRepository(db))
    return {
        "check": service.is_process_game_available(hand_id, CheckAction()),
        "call": service.is_process_game_available(hand_id, CallAction()),
        "bet": service.is_process_game_available(hand_id, BetAction()),
        "raise": service.is_process_game_available(hand_id, RaiseAction()),
        "burn": service.is_process_game_available(hand_id, BurnAction()),
        "fold": service.is_process_game_available(hand_id, FoldAction()),
        "gameOver": over.is_over(hand_id),
        "allIn": service.is_process_game_available(hand_id, AllInAction()),
        "deal": service.is_process_game_available(hand_id, DealAction())
    }