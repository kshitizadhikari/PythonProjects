from database.db import Base, engine
from models.models import User

Base.metadata.create_all(bind=engine)

print("Tables created successfully")