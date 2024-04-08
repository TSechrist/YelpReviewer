import re
import Stem
from operator import itemgetter
from StopList import StopList

class TermFrequencyTable:

    def __init__(self):
        self.termFreqTable = {}
        self.listOfReviews = []
        self.termList = []


    def addList(self, newList):
        self.listOfReviews.append(newList)

    def getTable(self):
        return self.termFreqTable

    def getTermList(self):
        return self.termList

    def displayList(self):
        print(self.listOfReviews)

    def displayTermList(self):
        print(self.termList)

    def formatTable(self):

        self.termList = []
        for currList in self.listOfReviews:
            for currItem in currList:
                if currItem[0] not in self.termList:
                    self.termList.append(currItem[0])
                    self.termFreqTable[currItem[0][0] + " " + currItem[0][1]] = 0

        self.termList.sort()

        for currList in self.listOfReviews:
            for term in currList:
                if (term[0][0] + " " + term[0][1]) in self.termFreqTable:
                    self.termFreqTable[term[0][0] + " " + term[0][1]] += term[1]

        # print(self.termFreqTable)


        # for currList in self.listOfReviews:
        #     print(currList)
        #     total = 0
        #     tempList = []
        #     for term in self.termList:
        #         for currItem in currList:
        #             # print(currItem)
        #             if term == currItem[0]:
        #                 total += currItem[1]
        #         tempList.append(term)
        #         tempList.append(total)
        #         # print(tempList)

    def display(self):

        for term in self.termList:
            print(term + " ", end='')
        print()

        for tempList in self.termFreqTable:
            for num in tempList:
                print(num, end='')
                print(" ", end='')
            print()

    def displayVert(self):

        count = 0
        for term in self.termList:
            total = 0
            tempList = []
            tempList.append(term)

            for listNum in self.termFreqTable:
                # tempList.append(listNum[count])
                total += int(listNum[count])
            count += 1

            if total > 9:
                print(tempList[0], end='')
                # for num in tempList:
                #     print(num, end='')
                #     print(" ", end='')
                print("\t\ttotal: " + str(total))

