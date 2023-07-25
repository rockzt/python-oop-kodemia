# Create a function that create a file, create a function that update a file, create an option that delete a file


# File can have content, or not
import os
import json

JSON_ACCEPTED_TYPES = (list, dict)


def is_content_valid(content, *types):
    types_to_use = types if len(types) > 0 else (str)

    is_content_valid_type = isinstance(content, types_to_use)

    if is_content_valid_type:
        return is_content_valid_type
    else:
        raise ValueError


def get_is_file_exist(file_path):
    is_file_exists = os.path.exists(file_path)

    if is_file_exists:
        return True
    else:
        raise FileNotFoundError


def create_json_files(file_name: str, content=None):
    with_content = is_content_valid(content, *JSON_ACCEPTED_TYPES)

    try:
        open_mode = "x" if with_content else "x"

        new_file = open(file_name, open_mode)

        if with_content:
            json_formatted_content = json.dumps(content)
            new_file.write(json_formatted_content)

        new_file.close()
    except ValueError as error:
        raise IOError(f"You need to include some content to create a file") from error


def create_file(file_name: str, content=None):
    with_content = is_content_valid(content)

    try:
        open_mode = "w" if with_content else "x"

        new_file = open(file_name, open_mode)

        if with_content:
            new_file.write(content)

        new_file.close()
    except ValueError as error:
        raise IOError(f"You need to include some content to create a file") from error


def update_file(file_name: str, content: str, overwrite: bool = False):
    try:
        open_mode = "w" if overwrite else "a"

        file = open(file_name, open_mode)

        file.write(content)

        file.close()
    except FileExistsError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error
    except PermissionError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error


def update_json_file(file_name: str, content=None, overwrite: bool = False):
    try:
        open_mode = "w" if overwrite else "a"

        is_content_valid(content, *JSON_ACCEPTED_TYPES)

        file = open(file_name, "r")

        file_content = file.read()

        file_content_json = json.loads(file_content)

        file.close()

        is_content_valid(file_content_json, *JSON_ACCEPTED_TYPES)

        if isinstance(file_content_json, list):
            if isinstance(content, list):
                file_content_json = file_content_json + content
            elif isinstance(content, dict):
                file_content_json.append(content)

        elif isinstance(file_content_json, dict) and isinstance(content, dict):
            if isinstance(content, list):
                for item, index in content:
                    file_content_json[index] = item

            elif isinstance(content, dict):
                for key in list(content.keys()):
                    file_content_json[key] = content[key]

        file_content_string = json.dumps(file_content_json)

        updatable_file = open(file_name, open_mode)

        updatable_file.write(file_content_string)

        updatable_file.close()

    except FileExistsError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error
    except PermissionError as error:
        raise IOError(
            f"You don't have permissions to update the {file_name} file, please update your permissions and try again"
        ) from error
    except ValueError as error:
        raise IOError(
            f"The content you're tring to write into the file ${file_name} is not of type list or dict"
        ) from error


def delete_file(file_path):
    try:
        get_is_file_exist(file_path)
        os.remove(file_path)
    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error
    except PermissionError as error:
        raise IOError(f"You don't have permissions to delete this file") from error


def read_file(file_path):
    try:
        get_is_file_exist(file_path)
        file = open(file_path)
        file_stream = file.read()
        print(file_stream)

        return file_stream

    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error

    except PermissionError as error:
        raise IOError(f"You don't have permissions to delete this file") from error


def read_json_file(file_path):
    try:
        get_is_file_exist(file_path)
        file = open(file_path)
        file_stream = file.read()
        file_content_json = json.loads(file_stream)
        print(file_content_json)

        return file_content_json

    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error

    except PermissionError as error:
        raise IOError(f"You don't have permissions to delete this file") from error