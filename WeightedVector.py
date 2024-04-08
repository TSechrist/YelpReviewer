import json
from TextParser import TextParser
import math

#                           average                   min                       max
# 5star -        7.9     3.204176265824693      -13.028643924917958        16.88578222214421
# 4star -        6.6     1.986488533999484      -17.01176984015702         14.129129977512243
# 2star -       -4.5    -9.19865360868044       -34.297560069624424        3.1208862013592356
# 1star -       -7.9    -12.6266329264273       -46.05009804491635         0.9829178989403702

class WeightedVector:

    def __init__(self):
        self.compareVector = {}

    def eval(self, review):
        pReview = TextParser(review).sortByAlphaNGram(2)
        total = 0
        for terms in pReview:
            if (terms[0][0] + " " + terms[0][1]) in self.compareVector:
                temp = 0
                if (self.compareVector[(terms[0][0] + " " + terms[0][1])]) < 0:
                    temp = (self.compareVector[(terms[0][0] + " " + terms[0][1])] * -1) ** (1. / 5)
                    temp = temp * -1
                else:
                    temp = (self.compareVector[(terms[0][0] + " " + terms[0][1])]) ** (1. / 5)
                print(str(temp) + " : " + terms[0][0] + " " + terms[0][1])
                total += (temp * terms[1])
        print("Total score before normalizing: " + str(total))
        return (total / len(pReview) ** (1. / 2)) + 4.7

    def predict_dec(self, review):
        num = self.eval(review)
        print("5 star: score >= 7.25")
        print("4 star: 7.25 > score >= 3.6")
        print("3 star: 3.6 > score >= -2.25")
        print("2 star: -2.25 > score >= -6.2")
        print("1 star: -6.2 > score")
        print("Score: " + str(num))
        if num >= 7.25:
            return 5
        elif 7.25 > num >= 3.6:
            return 4
        elif 3.6 > num >= -2.25:
            return 3
        elif -2.25 > num >= -6.2:
            return 2
        else:
            return 1

    def predict(self, review):
        num = self.eval(review)
        if num >= 7.25:
            prediction = 5
        elif 7.25 > num >= 3.6:
            prediction = 4
        elif 3.6 > num >= -2.25:
            prediction = 3
        elif -2.25 > num >= -6.2:
            prediction = 2
        else:
            prediction = 1
        print("5 star: score >= 7.25")
        print("4 star: 7.25 > score >= 3.6")
        print("3 star: 3.6 > score >= -2.25")
        print("2 star: -2.25 > score >= -6.2")
        print("1 star: -6.2 > score")
        print("Score: " + str(num))
        print("Predicted star: ",  prediction)
        
        return prediction


    def displayTable(self, table, stars):
        for key in table:
            print(key, end='')
            print(" : " + str(table[key]))

    def displayVector(self):
        for key in sorted(self.compareVector):
            if abs(self.compareVector[key]) > 500: #positive and negative
            # if self.compareVector[key] > 500:    #positive only
                print(key, end='')
                print(" : " + str(self.compareVector[key]))

    def updateVector(self, table, mod):

        for key in sorted(table):
            if mod < 0:
                if key not in self.compareVector:
                    self.compareVector[key] = (table[key] * mod)
                else:
                    self.compareVector[key] += (table[key] * mod)
            else:
                if key not in self.compareVector:
                    self.compareVector[key] = (table[key] * mod)
                else:
                    self.compareVector[key] += (table[key] * mod)

    def loadVector(self):
        with open('weighted_vector.json') as json_file:
            self.compareVector = json.load(json_file)

    def saveVector(self):
        with open('weighted_vector.json', 'w') as json_file:
            json.dump(self.compareVector, json_file)
