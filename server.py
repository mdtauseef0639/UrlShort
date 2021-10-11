import os
from app import setup_server

_load_env = os.environ.get('FLASK_ENV') == 'development'
if _load_env:
    from dotenv import load_dotenv
    load_dotenv()


server = setup_server()
