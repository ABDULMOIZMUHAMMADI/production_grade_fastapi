from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


database_url = "postgresql://postgres:0800@localhost:5432/user_management"

connect_eng = create_engine(database_url)

sessionlocal = sessionmaker(bind=connect_eng)

Base = declarative_base()