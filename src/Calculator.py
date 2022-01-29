from curses import raw

from src.Gradebook import Gradebook
from src.Grade import Grade
import config

class Calculator():
    def __init__(self, filename):
        self.raw = open(filename, "r").readlines()
        for _ in range(len(self.raw)):
            length = len(self.raw[_])
            if self.raw[_][length - 1] == '\n':
                self.raw[_] = self.raw[_][:length - 1]
        self.quadra_marks = {
            'A': 4.0, 
            'B': 3.5, 
            'C': 2.8, 
            'D': 1.7, 
            'E': 0
        }
        self.gradebook = Gradebook()

    def single_gpa(self, score, mode):
        if mode == 'bin':
            return (4 - 3 * (100 - score) ** 2 / 1600) if config.count_binary else 0
        elif mode == 'qua':
            return self.quadra_marks[score];
        elif float(score) < 60:
            return 0;
        else:
            return 4 - 3 * (100 - score) ** 2 / 1600

    def calculate(self):
        for i in range(0, len(self.raw), 4):
            tem = Grade(self.raw[i], self.raw[i + 1], self.raw[i + 2], self.raw[i + 3])
            self.gradebook.add_grade(tem)

        nume = 0
        denom = 0
        for grade in self.gradebook.grades:
            nume += grade.get_point() * self.single_gpa(grade.get_grade(), grade.get_mode())
            denom += grade.get_point()
        return nume / denom