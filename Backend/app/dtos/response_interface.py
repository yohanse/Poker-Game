from abc import ABC, abstractmethod
from typing import Any, Dict

class IReponse(ABC):
    @abstractmethod
    def to_json(self) -> Dict[str, Any]:
        pass