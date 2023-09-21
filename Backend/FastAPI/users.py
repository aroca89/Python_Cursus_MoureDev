### Users API###

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#  Inicia el server: uvicorn users:app --reload

class User(BaseModel):
	id: int
	name: str
	surname: str
	url: str
	age: int

users_list = [User(id= 1, name= "Aritz", surname= "Roca", url= "https://aroca.dev", age= "33"),
		 User(id= 2, name= "Miriam", surname= "Guti", url= "https://miri.dev", age= "31"),
		 User(id= 3, name= "Joel", surname= "Saiz", url= "https://joel.dev", age=  "19")]

@app.get("/usersjson")
async def usersjson():
	return [{"name": "Aritz", "surname": "Roca", "url": "https://aroca.dev", "age":"33"},
		 	{"name": "Miriam", "surname": "Guti", "url": "https://miri.dev", "age":"31"},
		 	{"name": "Joel", "surname": "Saiz", "url": "https://joel.dev", "age":"19"}]

@app.get("/users")
async def users():
	return users_list

@app.get("/user/{id}")
async def user(id: int):
	users = filter(lambda user: user.id == id, users_list)
	try:
		return list(users)[0]
	except:
		return {"Error": "NO se a encontrado el usuario"}
