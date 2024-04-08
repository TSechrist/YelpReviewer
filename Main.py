
from WeightedVector import WeightedVector
from TextParser import TextParser
from TermFrequencyTable import TermFrequencyTable
import json
import gui as gui_window
import tkinter as tk
import argparse

def arguments_parse( ):
	"""Returns parsed arguments as dictionary
	"""
	parser = argparse.ArgumentParser(
		description='Runs yelp predictor program.')

	parser.add_argument('--demo', '-d', help='Displays sample 1-star and 5-star review',
		action='store_true')
	
	parser.add_argument('--gui', '-g', help='Loads up GUI component',
		action='store_true')
	
	parser.add_argument('--vector_display', '-v', help='Displays first 2000 weights in weighted vector',
		action='store_true')

	args = parser.parse_args()
	returndict = dict()
	returndict.update(demo=args.demo)
	returndict.update(gui=args.gui)
	returndict.update(vector_display=args.vector_display)
	return returndict


# tft1 = TermFrequencyTable()
# tft2 = TermFrequencyTable()
# tft3 = TermFrequencyTable()
# tft4 = TermFrequencyTable()
# tft5 = TermFrequencyTable()



# ***********************
# The range of the tests
# ***********************
#
# w = WeightedVector()
# w.loadVector()
# star = 5
#
# with open(f"sample_reviews_100_{star}.json", 'r', encoding="utf8") as f:
#     data = json.load(f)
#
# total = 0
# difference = 0
#
# for i in range(100):
#     score = w.predict(data[i]['text'])
#     print(score, end='')
#     print(" " + str(w.eval((data[i]['text']))))
#     total += score
#     difference += abs(score - star)
#
# print(total / 100)
# print(difference / 100)



# 1308077 terms in the weighted vector

# ***********************
# Cutting the massive reviewfile
# ***********************

# review_list1 = []
# review_list2 = []
# review_list3 = []
# review_list4 = []
# review_list5 = []
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0

# data = [json.loads(line) for line in open('yelp_academic_dataset_review.json', 'r', encoding="utf8")]
#
# for i in range(1000000, 1010000):
#     if data[i]['stars'] == 1:
#         count1 += 1
#         if count1 <= 100:
#             review_list1.append(data[i])
#     elif data[i]['stars'] == 2:
#         count2 += 1
#         if count2 <= 100:
#             review_list2.append(data[i])
#     elif data[i]['stars'] == 3:
#         count3 += 1
#         if count3 <= 100:
#             review_list3.append(data[i])
#     elif data[i]['stars'] == 4:
#         count4 += 1
#         if count4 <= 100:
#             review_list4.append(data[i])
#     elif data[i]['stars'] == 5:
#         count5 += 1
#         if count5 <= 100:
#             review_list5.append(data[i])
#
#
# with open('sample_reviews_100_1.json', 'w') as json_file:
#     json.dump(review_list1, json_file)
#
# with open('sample_reviews_100_2.json', 'w') as json_file:
#     json.dump(review_list2, json_file)
#
# with open('sample_reviews_100_3.json', 'w') as json_file:
#     json.dump(review_list3, json_file)
#
# with open('sample_reviews_100_4.json', 'w') as json_file:
#     json.dump(review_list4, json_file)
#
# with open('sample_reviews_100_5.json', 'w') as json_file:
#     json.dump(review_list5, json_file)


# *************************************
# Text averages
# *************************************

# with open('sample_reviews_10000_25000_1.json', 'r', encoding="utf8") as f:
#     data = json.load(f)
#
# average = 0
# count = 2000
# high = w.eval(data[0]['text'])
# low = w.eval(data[0]['text'])

# for i in range(count):
#     average += w.eval(data[i]['text'])
#     if w.eval(data[i]['text']) > high:
#         high = w.eval(data[i]['text'])
#     if w.eval(data[i]['text']) < low:
#         low = w.eval(data[i]['text'])
#
# print(average / count)
# print(low)
# print(high)

#                           average                   min                       max
# 5star -            3.204176265824693      -13.028643924917958        16.88578222214421
# 4star -            1.986488533999484      -17.01176984015702         14.129129977512243
# 2star -           -9.19865360868044       -34.297560069624424        3.1208862013592356
# 1star -           -12.6266329264273       -46.05009804491635         0.9829178989403702



# *************************************
# Add terms to the weighted vector
# *************************************

# for i in range(13000, 15000):
#     tft1.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_2.json', 'r', encoding="utf8") as f2:
#     data = json.load(f2)
#
# for i in range(13000, 15000):
#     tft2.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_4.json', 'r', encoding="utf8") as f4:
#     data = json.load(f4)
#
# for i in range(13000, 15000):
#     tft4.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))
#
# with open('sample_reviews_10000_25000_5.json', 'r', encoding="utf8") as f5:
#     data = json.load(f5)
#
# for i in range(13000, 15000):
#     tft5.addList(TextParser(data[i]['text']).sortByAlphaNGram(2))

# tft1.formatTable()
# tft2.formatTable()
# tft4.formatTable()
# tft5.formatTable()
#
# w.updateVector(tft1.getTable(), -2)
# w.updateVector(tft2.getTable(), -1)
# w.updateVector(tft4.getTable(), 1)
# w.updateVector(tft5.getTable(), 2)
#
# w.saveVector()

# w.loadVector()
# print(len(w.compareVector))


# *************************************
# Print first 2000 terms of weighted vector
# *************************************
def display_vector():
	w = WeightedVector()
	w.loadVector()
	w.displayVector()

# *************************************
# Print a sample 1-star and 5-star review
# *************************************
def print_demo():
# 1308077 unique terms

	w = WeightedVector()
	w.loadVector()

	sample_text_1 = "My family and i thought we would try this place out bad idea. I dont recommend this place. Lets start with the food not being fresh most the food was a bit cold not even room temperature. Then the selection was poor few items where put out at a time and the food was bland no flavor. Last but not least we all had an upset stomach the following day. Dont waste your time! Buffet @Asia is a few blocks away sometimes there busy but worth the short wait."

	sample_text_5 = "When I walked in, I saw many tables were occupied, including sushi bar. This is a good sign. We were offered to the table on the patio. Luckily the weather was already cooled off at night. The service is nice and the food came out very fast even though the restaurant was packed. I love their pork Katsu curry. The rice is perfectly cooked. The pork Katsu is perfectly deep fried and has great texture. The curry is the best one I ever have. It is simple but complex in flavor. The pickle helps put all the flavor together. We ordered some nigiri and rolls. The scallop nigiri is so good. The scallop is firm and dry. It is hard to find other place that can prepare the scallop like this. Thumb up! The plum and shiso roll is interesting. It is tasty and refreshing. The tsubugai shellfish nigiri is also good. It is so crunchy good. We were full so we got matcha marron cake to go. The tiny cake with red bean, cream, and match cream on top is so delicious. I like their indoor water fountain, and they have many Tanuki in different size around the restaurant."

	print("************ 1 star review *************")
	print(w.eval(sample_text_1))
	print(w.predict(sample_text_1))
	print("************ 5 star review *************")
	print(w.eval(sample_text_5))
	print(w.predict(sample_text_5))



# *************************************
# GUI component
# *************************************
def launch_gui():
	window = tk.Tk()
	window.title("Yelp Sentiment Analyzer")
	gui = gui_window.MainApplication(window)
	gui.grid(row=0, column=0)
	tk.mainloop()


if __name__ == '__main__':

	args = arguments_parse()
	if args['demo']:
		print_demo()
	if args['gui']:
		launch_gui()
	if args['vector_display']:
		display_vector()

