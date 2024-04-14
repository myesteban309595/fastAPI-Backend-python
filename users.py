from fastapi import FastAPI

app = FastAPI()

#para iniciar el servidor (nodemon)  uvicorn users:app --reload

@app.get("/user")
async def users():
    return "hola usuarios"



