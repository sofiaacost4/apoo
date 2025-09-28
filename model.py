from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    nome: str
    quantidade: int
    descricao: str
    id: Optional[int] = None
                



