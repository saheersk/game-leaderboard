from pydantic import BaseModel


class ContestantCreate(BaseModel):
    username: str
    age: int


class ContestantResponse(BaseModel):
    id: int
    username: str
    age: int

    model_config = {"from_attributes": True}
