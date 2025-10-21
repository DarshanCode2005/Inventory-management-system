from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

# Read password and URL-encode it to safely include any special characters such as @ or :
db_password = os.getenv("DB_PASS", "")
db_password_quoted = quote_plus(db_password)

# You can also split these into DB_USER/DB_HOST/DB_PORT/DB_NAME env vars if preferred
db_url = f"postgresql://postgres:{db_password_quoted}@localhost:5432/fastapiproj"

engine = create_engine(db_url)

# SQLAlchemy Base for declarative models
Base = declarative_base()

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLalchemy indepth learn.