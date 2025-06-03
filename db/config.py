"""
contains database configuration
"""
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL",
                         "postgresql://postgres:Emma2025@localhost:5432/health_simplified_db")