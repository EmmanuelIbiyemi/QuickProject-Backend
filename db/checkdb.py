from sqlalchemy import inspect
from connectiondb import engine
inspector = inspect(engine)
print("Table Created:" ,inspector.get_table_names())
