class Grade:
    def __init__(self, subject, grade, point, mode):
        self.subject = subject
        self.grade = grade
        self.point = point
        self.mode = mode

    def get_subject(self):
        return self.subject

    def get_grade(self):
        try:
            return float(self.grade)
        except:
            return self.grade
            
    def get_point(self):
        return float(self.point)

    def get_mode(self):
        return self.mode
