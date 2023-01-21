from typing import List, Optional
from pydantic import BaseModel

class UsuarioUpdate(BaseModel):
    email: Optional[str] = None
    telefone: Optional[str] = None  


    