from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

# Check if DATABASE_URL is set (Render provides this automatically)
database_url = os.getenv("DATABASE_URL")

if not database_url:
    # Fallback to individual environment variables for local development
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASS", "")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "fastapiproj")
    
    db_password_quoted = quote_plus(db_password)
    database_url = f"postgresql://{db_user}:{db_password_quoted}@{db_host}:{db_port}/{db_name}"

# Handle Render's postgres:// URL (needs to be postgresql://)
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(database_url)

# SQLAlchemy Base for declarative models
Base = declarative_base()

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)