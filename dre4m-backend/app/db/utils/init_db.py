"""
This script is used to create the database user and the table in the database.
"""

# From imports
from .utils_db import create_db_user
from .utils_db import create_table


if __name__ == "__main__":
    # Missing db creation
    create_db_user()
    create_table()
