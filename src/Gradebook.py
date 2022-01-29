from src.Grade import Grade

class Gradebook():
    def __init__(self):
        self.grades = []

    def add_grade(self, grade: Grade):
        self.grades.append(grade)