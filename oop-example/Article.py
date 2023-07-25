import file_manager
import os


current_path = os.path.dirname(__file__)
ARTICLE_FILE_NAME = "article.json"
ARTICLE_FILE_PATH = current_path + f"/{ARTICLE_FILE_NAME}"


class Article:
    def __init__(self, title, content, status, image, created_by):
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by

    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "status": self.status,
            "image": self.image,
            "created_by": self.created_by,
        }

    def get_all(self):
        return file_manager.read_json_file(ARTICLE_FILE_PATH)

    def save(self):
        dict_article = self.as_dict()

        try:
            file_manager.get_is_file_exist(ARTICLE_FILE_PATH)
            file_manager.update_json_file(ARTICLE_FILE_PATH, dict_article, True)

        except FileNotFoundError:
            file_manager.create_json_files(ARTICLE_FILE_PATH, [dict_article])