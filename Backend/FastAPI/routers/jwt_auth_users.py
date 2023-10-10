from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "ee329cc4ebade0db6e663c3a14472748bee4b66253d1905eaea238f18909a291"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
	username:	str
	full_name:	str
	email:		str
	disabled:	bool

class UserDB(User):
	password: str

users_db = {
	"aroca-pa": {
		"username": "aroca-pa",
		"full_name": "Aritz Roca",
		"email": "arocapazos@gmail.com",
		"disabled": False,
		"password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
	},
	"migutier": {
		"username": "migutier",
		"full_name": "Miriam Gutierrez",
		"email": "migutierrez1991@gmail.com",
		"disabled": True,
		"password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S"
	},
}

def search_user_db(username: str):
	if username in users_db:
		return UserDB(**users_db[username])
	
@app.post("/login")
async def login (form: OAuth2PasswordRequestForm = Depends()):
	user_db = users_db.get(form.username)
	if not user_db:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
	
	user = search_user_db(form.username)

	if not crypt.verify(form.password, user.password):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

	access_token = { "sub": user.username, 
					"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
	
	return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}
