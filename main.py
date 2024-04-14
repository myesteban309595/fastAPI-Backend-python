from fastapi import FastAPI

app = FastAPI()  #llamamos una clase de fastapi es un contexto inicial

#def es para definir una funcion
# con @app. accedemos al contexto app y podemos comunicar ocn las rutas de la app
@app.get('/')  
async def root():  
    return "hola mundo"

@app.get('/saludo')  
async def root():  
    return "estoy saludando"

@app.get("/url")
async def root():
    return {"url_curso": "https://youtube.com"}


