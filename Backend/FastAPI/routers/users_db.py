### Users DB API###

from http import client
from fastapi import APIRouter, HTTPException
from db.models.user import User
from db.client import db_client

router = APIRouter(prefix="/userdb", 
				   tags=["userdb"], 
				   responses={404: {"message": "No encontrado"}})

users_list = []


@router.get("/")
async def users():
	return users_list

@router.get("/{id}")
async def user(id: int):
	users = filter(lambda user: user.id == id, users_list)
	try:
		return list(users)[0]
	except:
		return {"Error": "NO se a encontrado el usuario"}

# Path

@router.get("/{id}")
async def user(id: int):
	return search_user(id)

# Query

@router.get("/")
async def user(id: int):
	return search_user(id)
	
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
	#if type(search_user(user.id)) == User:
	#	raise HTTPException(
	#		status_code=404, detail="El usuario ya exite")
	
	user_dict = dict(user)
	del user_dict["id"]

	id = db_client.local.users.insert_one(user_dict).inserted_id

	new_user = db_client.local.users.find_one({"_id":id})

	users_list.append(user)
	return user

@router.put("/")
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
	
@router.delete("/{id}")
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