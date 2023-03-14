from pydantic import BaseModel

class LogoFields(BaseModel):
    """Implements the fields for the logos.
    
    Args:
        BaseModel (pydantic.BaseModel): BaseModel from pydantic
    """
    id: str
    logo_direct_url: str
    optimized_direct_url: str | None
