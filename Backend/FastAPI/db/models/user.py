from pydantic import BaseModel

class User(BaseModel):
	id: str | None
	namename: str
	email: str
