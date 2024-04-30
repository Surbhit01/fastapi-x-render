from fastapi import FastAPI, HTTPException

app = FastAPI()



@app.get("/", status_code=201)
async def say_hello():
    return {"response": "Homepage"}

@app.get("/hello", status_code=201)
async def say_hello():
    return {"response": "Hello"}
