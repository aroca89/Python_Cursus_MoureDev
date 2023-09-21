# Documentacion oficial:  http://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return " Hola FastAPI!"

# Url local: http://127.0.0.1:8000/

@app.get("/url")
async def root():
	return { "url_curso":"https://mouredev.com/python"}





# Inicia el server: uvicorn main:app --reload
# Detener el server: CTR+C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Rodocly: http://127.0.0.1:8000/redoc