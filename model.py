from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    id: Optional[int] = None
    desc: str
    quant: Optional[int] = None
                



