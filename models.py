class Person:
    def __init__(self, id_p, name, gender, age, picture_url, position, skills):
        self.id_p = id_p
        self.name = name
        self.gender = gender
        self.age = age
        self.picture_url = picture_url
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f'{self.name}'

    def __len__(self):
        return len(self.id_p)
