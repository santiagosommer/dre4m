# From imports
from app.db.utils.utils_db import (
    create_db_user,
    create_tables,
    create_db
)
"""
This script is used to create the database user and the table in the database.
"""

if __name__ == "__main__":
    create_db_user()
    create_db()
    create_tables()
