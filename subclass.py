class User:
    def __init__(self, first_name, last_name, email, password="asdasbd76sadg76asd"):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email


class Animal:
    def _init_(self, legs, eyes, hair_color):
        self.legs = legs
        self.eyes = eyes
        self.hair_color = hair_color


class Human(Animal):
    def _init_(self, hair_color, eye_color):
        super()._init_(2, 2, hair_color)
        #  You can't access properties before initiailization
        self.eye_color = eye_color


class Spider(Animal):
    def _init_(self, hair_color):
        super()._init_(8, 8, hair_color)
        print(self.eyes)