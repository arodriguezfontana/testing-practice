from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

class UserModel:
    STANDARD_USER = User(username="standard_user", password="secret_sauce")
    PROBLEM_USER = User(username="problem_user", password="secret_sauce")
    ERROR_USER = User(username="error_user", password="secret_sauce")
    ADMIN_USER = User(username="admin_user", password="secret_sauce")