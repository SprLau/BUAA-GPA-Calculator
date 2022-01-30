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
        self.quadra_scores = {
            'A': 100, 
            'B': 83.67, 
            'C': 74.70, 
            'D': 64.98, 
            'E': 0
        }
        self.gradebook = Gradebook()

    def convert_score(self, _):
        try:
            return float(_)
        except:
            return self.quadra_scores[_]

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
        wa_nume = 0
        uwa_sum = 0
        denom = 0
        for grade in self.gradebook.grades:
            nume += grade.get_point() * self.single_gpa(grade.get_grade(), grade.get_mode())
            wa_nume += grade.get_point() * self.convert_score(grade.get_grade())
            uwa_sum += self.convert_score(grade.get_grade())
            denom += grade.get_point()
        
        final_gpa = nume / denom
        weighted_ave = wa_nume / denom
        unweighted_ave = uwa_sum / len(self.gradebook.grades)

        print("====================== BUAA GPA Calculator ======================")
        print("  GPA: {:4.2f}     Weighted Ave.: {:5.2f}     Unweighted Ave.: {:5.2f}  ".format(final_gpa, weighted_ave, unweighted_ave))
        print("=================================================================")