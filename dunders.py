# File copied from ./homework

import file_manager
import os

current_path = os.path.dirname(__file__)
USER_FILE_NAME = "users.json"
USER_FILE_PATH = current_path + f"/{USER_FILE_NAME}"


class User:
    def __init__(self, first_name, last_name, email, password="asdasbd76sadg76asd"):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def ___str__(self):
        return f"{self}"

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
        }

    def get_all(self):
        return file_manager.read_json_file(USER_FILE_PATH)

    def save(self):
        dict_user = self.as_dict()

        try:
            file_manager.get_is_file_exist(USER_FILE_PATH)
            file_manager.update_json_file(USER_FILE_PATH, dict_user, True)

        except FileNotFoundError:
            print("File not found")
            file_manager.create_json_files(USER_FILE_PATH, [dict_user])