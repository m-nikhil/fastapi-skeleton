from sqlalchemy.ext.declarative import declarative_base

# To be inherited by all the models
# Pass this Base.metadata to Albemic
Base = declarative_base()

# Register all the models below so Albemic will discover
from app.models.userModel import User
