from pydantic import BaseModel

class LogoFields(BaseModel):
    """Implements the fields for the logos.
    
    Args:
        BaseModel (pydantic.BaseModel): BaseModel from pydantic
    """
    
    id: str
    filename: str
    gdrive_direct_url: str

class LogoRoot(BaseModel):
    """Implements the root for the logos.
    
    Args:
        BaseModel (pydantic.BaseModel): BaseModel from pydantic
    """
    
    logos: list[LogoFields]
