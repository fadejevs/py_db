from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/random')
async def get_random():
    rn:int= random.randint(0, 100)
    return {'number': rn, 'limit': 100}
