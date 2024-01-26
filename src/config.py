from os import getenv
from dotenv import load_dotenv

load_dotenv()

PORT = int(getenv("PORT", "5000"))
APP_KEY = getenv("APP_KEY")
DATABASE_URL = getenv("DATABASE_URL")
