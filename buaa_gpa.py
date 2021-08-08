#########################################################
#           --- BUAA GPA Calculator, 2021 ---           #    
#   The calculating method strictly obeys the           #
#   official published one which can be found on BUAA   #
#   Computer Science Department site.                   #
#=======================================================#
#   Please do report any issue you found to             #
#   github.com/SprLau                                   #
#=======================================================#
#   Please refer to README.md for user guidance.        #
#########################################################

class FourGrade():
    def convert_mark(cls, score):
        if score == "A\n":
            gpa_score = 4
        elif score == "B\n":
            gpa_score = 3.5
        elif score == "C\n":
            gpa_score = 2.8
        elif score == "D\n":
            gpa_score = 1.7
        elif score == "E\n":
            gpa_score = 0
            
        return gpa_score

class GPA():
    def get_gpa(cls, score):
        if float(score) < 60:
            gpa_score = 0
        else:
            gpa_score = 4 - 3 * (100 - float(score)) ** 2 / 1600
        return gpa_score

    def cal_score(cls, score_arr, point_arr):
        converted_score_arr = []
        for score in score_arr:
            if score == 'A\n' or score == 'B\n' or score == 'C\n' or score == 'D\n' or score == 'E\n':
                converted_score_arr.append(FourGrade.convert_mark(FourGrade, score))
            else:
                converted_score_arr.append(GPA.get_gpa(GPA, score))
        products = 0
        for score, point in zip(converted_score_arr, point_arr):
            products += float(score) * float(point)
        sum_point = 0
        for point in point_arr:
            sum_point += float(point)
        gpa = 0 if sum_point == 0 else products / sum_point
        return gpa

class GradeBook:
    def __init__(self):
        self.scoreList = []
        self.weightList = []

    def add(self, score, weight):
        self.scoreList.append(score)
        self.weightList.append(weight)

    def weightedAve(self):
        res = 0
        addup = 0
        w = 0
        for num, weight in zip(self.scoreList, self.weightList):
            if num == 'A\n':
                addup += 100 * float(weight)
            elif num == 'B\n':
                addup += 83.67 * float(weight)
            elif num == 'C\n': 
                addup += 74.70 * float(weight)
            elif num == 'D\n':
                addup += 64.98 * float(weight)
            elif num == 'E\n':   
                addup += 0
            else:
                addup += float(num) * float(weight)
            w += float(weight);
        res = addup / (1 if w == 0 else w);
        return res
    
    def rawAve(self):
        addup = 0
        for num in self.scoreList:
            if num == 'A\n':
                addup += 100
            elif num == 'B\n':
                addup += 83.67
            elif num == 'C\n': 
                addup += 74.70
            elif num == 'D\n':
                addup += 64.98
            elif num == 'E\n':   
                addup += 0
            else:
                addup += float(num)
        return addup / (1 if len(self.scoreList) == 0 else len(self.scoreList))
    
    def addSeries(self):
        print("To end, input a pair of -1")
        newScore = float(input("Score: "))
        newWeight = float(input("Weight: "))
        while newScore != -1 and newWeight != -1:
            newScore = float(input("Score: "))
            newWeight = float(input("Weight: "))
            self.add(newScore, newWeight)

    def getScoreList(self):
        return self.scoreList

    def getWeightList(self):
        return self.weightList

class Start:
    def __init__(self):
        self.gradebook = GradeBook()

    def options(self):
        print("#######################################")
        print("# 1. Add a series of scores;          #")
        print("# 2. Add a single score;              #")
        print("# 3. Get Weighted Average;            #")
        print("# 4. Get Raw Average;                 #")
        print("# 5. Get BUAA GPA;                    #")
        print("# 6. Exit.                            #")
        print("#######################################")
        opt = int(input("Option: "))
        while opt != 7:
            if opt == 1:
                print("#######################################")
                print("# 1. Manuelly add;                    #")
                print("# 2. Add from an existed file.        #")
                print("#######################################")
                subopt = int(input("Option: "))
                if subopt == 1:
                    self.gradebook.addSeries()
                elif subopt == 2:
                    filename = input("Filename: ")
                    try:
                        readin = open(filename, "r")
                    except FileNotFoundError:
                        print("*** No Such File Founded! ***")
                    else:
                        storeFile = readin.readlines()
                        for i in range(len(storeFile)):
                            if i % 3 == 0:
                                continue
                            elif i % 3 == 2:
                                continue
                            else:
                                self.gradebook.add(storeFile[i], storeFile[i + 1])
                        print("*** File Successfully Added. ***")
                        readin.close()
                else:
                    print("Invalid Option.")
            elif opt == 2:
                newScore = float(input("Score: "))
                newWeight = float(input("Weight: "))
                self.gradebook.add(newScore, newWeight)
            elif opt == 3:
                print("The Weighted Ave. : {:5.4f}".format(self.gradebook.weightedAve()))
            elif opt == 4:
                print("The Raw Ave. : {:5.4f}".format(self.gradebook.rawAve()))
            elif opt == 5:
                print("The GPA is: {:5.4f}".format(GPA.cal_score(GPA, self.gradebook.scoreList, self.gradebook.weightList)))
            elif opt == 6:
                break
            else:
                print("Invalid Option.")
            
            opt = int(input("Option: "))

        outFile = open("store.txt", "a+")
        for score, weight in zip(self.gradebook.getScoreList(), self.gradebook.getWeightList()):
            print(score, file=outFile)
            print(weight, file=outFile)
        outFile.close()

start = Start()
start.options()