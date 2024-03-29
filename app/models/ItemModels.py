from pydantic import BaseModel
from app.models.ItemFields import LogoFields

class ItemModel(BaseModel):
    """Implements the model for the items.
    
    Args:
        BaseModel (pydantic.BaseModel): BaseModel from pydantic
    """
    __root__: list[list[LogoFields]]
