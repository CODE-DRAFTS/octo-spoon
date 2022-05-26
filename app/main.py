from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.routes import economics , currencys, fundamentals, news, users
import psycopg2
from  psycopg2.extras  import RealDictCursor
from app import env


#seeting db connections
while True:
    try:
        conn = psycopg2.connect( host= env.DATABASE_HOST, user= env.DATABASE_USER , database= env.DATABASE_NAME , password= env.DATABASE_PASSWORD , cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print(" db connection ok")
        break
    except Exception as error:
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

