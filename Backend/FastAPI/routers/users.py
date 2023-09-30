### Users API###

from fastapi import APIRouter, FastAPI, HTTPException, Query
from httpx import delete
from pydantic import BaseModel

router = APIRouter()

#  Inicia el server: uvicorn users:app --reload

class User(BaseModel):
	id: int
	name: str
	surname: str
	url: str
	age: int

users_list = [User(id= 1, name= "Aritz", surname= "Roca", url= "https://aroca.dev", age= "33"),
			  User(id= 2, name= "Miriam", surname= "Guti", url= "https://miri.dev", age= "31"),
			  User(id= 3, name= "Joel", surname= "Saiz", url= "https://joel.dev", age=  "19"),]

@router.get("/usersjson")
async def usersjson():
	return [{"name": "Aritz", "surname": "Roca", "url": "https://aroca.dev", "age":"33"},
		 	{"name": "Miriam", "surname": "Guti", "url": "https://miri.dev", "age":"31"},
		 	{"name": "Joel", "surname": "Saiz", "url": "https://joel.dev", "age":"19"},]

@router.get("/users")
async def users():
	return users_list

@router.get("/user/{id}")
async def user(id: int):
	users = filter(lambda user: user.id == id, users_list)
	try:
		return list(users)[0]
	except:
		return {"Error": "NO se a encontrado el usuario"}

# Path

@router.get("/user/{id}")
async def user(id: int):
	return search_user(id)

# Query

@router.get("/user/")
async def user(id: int):
	return search_user(id)
	
@router.post("/user/",status_code=201)
async def user(user: User):
	if type(search_user(user.id)) == User:
		raise HTTPException(status_code=404, detail="El usuario ya exite")
		
	users_list.append(user)
	return user

@router.put("/user/")
async def user(user: User):

	found = False

	for index, saved_user in enumerate(users_list):
		if saved_user.id == user.id:
			users_list[index] = user
			found = True

	if not found:
		return {"Error": "No he a actualizado el usuario"}
	else:
		return user
	
@router.delete("/user/{id}")
async def user(id: int):

	found = False

	for index, saved_user in enumerate(users_list):
		if saved_user.id == id:
			del users_list[index]
			found = True

	if not found:
		return {"Error": "No he a actualizado el usuario"}
	

def search_user(id: int):
	users = filter(lambda user: user.id == id, users_list)
	try:
		return list(users)[0]
	except:
		return {"Error": "NO se a encontrado el usuario"}