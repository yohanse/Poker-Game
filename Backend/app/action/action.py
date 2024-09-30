from abc import ABC, abstractmethod
from pokerkit import State

from app.dtos.params import Params
from app.exceptions.game_exception import ActionCanNotPerformException
from app.models.action import ActionModel


class IAction(ABC):
    @abstractmethod
    def _do_execute(self, state: State, params: Params) -> ActionModel:
        pass
    
    @abstractmethod
    def _is_execute_available(self, params: Params) -> bool:
        pass
    
    @abstractmethod
    def is_execute_available(self, state: State) -> bool:
        pass
    
    def execute(self, state: State, params: Params) -> ActionModel:
        if self._is_execute_available(state, params):
            return self._do_execute(state, params)
        raise ActionCanNotPerformException(f"{params.action_string} can't be performed")