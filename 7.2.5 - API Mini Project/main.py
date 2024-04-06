import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API-KEY')

print(f'MY API Key is {api_key}')