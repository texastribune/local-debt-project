from boot import engine, Base
from models import *

Base.metadata.create_all(engine)
