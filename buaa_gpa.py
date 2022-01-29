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

import src.Calculator

calculator = src.Calculator.Calculator("gradebook.txt")

print(calculator.calculate())