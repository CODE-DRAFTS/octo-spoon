from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.routes import economics , currencys, fundamentals, news, users
import psycopg2
from  psycopg2.extras  import RealDictCursor
from app import env
from time import sleep


#seeting db connections
while True:
    try:
        #postgress db
        conn = psycopg2.connect( host= env.POSTGRES_DATABASE_HOST,port=env.POSTGRES_DATABASE_PORT, user= env.POSTGRES_DATABASE_USER , database= env.POSTGRES_DATABASE_NAME , password= env.POSTGRES_DATABASE_PASSWORD , cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print(" db connection ok") #TODO: replace (ln15) with logging
        
        #mongodb database


        break
    except Exception as error:
        print(error )
        print("db connection failed retrying")
        sleep(1)

app = FastAPI()

origins =["*"]   #domains allowed to access the api
app.add_middleware( CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router( economics.router)
app.include_router( currencys.router)
app.include_router( fundamentals.router)
app.include_router( news.router)
app.include_router( users.router)

@app.get("/")
async def root():
    return {"api devs"}

