from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional,NamedTuple
@dataclass
class Category:
    name: str 
    description: Optional[str] = None 
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda:datetime.now())
#create
# Fazendo com NamedTuple a mesma coisa que se faz com dataclass 
# class Product(NamedTuple):
#     id:str
#     name:str
# Product()
#estado da categoria