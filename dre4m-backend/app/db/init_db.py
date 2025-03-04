# From imports
from .utils.utils_db import create_db_user
from .utils.utils_db import create_table

if __name__ == "__main__":
    create_db_user()
    create_table()
