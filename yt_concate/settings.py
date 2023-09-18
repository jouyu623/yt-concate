from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os

API_KEY= os.getenv('API_KEY') #os.getenv讀取API的方式
