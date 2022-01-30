class DB:
    "A container class for database-related errors"
    class MultipleObjectsReturnedException(Exception):
        "Raise it if a method excepted to return one, returned two"
        pass