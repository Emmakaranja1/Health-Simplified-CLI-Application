"""
contains database configuration
"""
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql:Emma@2025@localhost:5432/health_simplified_db")