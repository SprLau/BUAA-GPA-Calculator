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
import sys

try:
    calculator = src.Calculator.Calculator(sys.argv[1])
    calculator.calculate()
except IndexError:
    print("*** Please Specify a Gradebook File!!! ***")
