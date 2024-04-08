import json
from WeightedVector import WeightedVector

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


# 5 Star pho
# "My go to place. Food is always good and everything is homemade. I'd highly recommend the pho as well as the fried rice, but everything here is delicious! Place has limited seating and can be busy, but it's worth it!"


# Old testing
# with open(f"sample_review_1_{star}.json", 'r', encoding="utf8") as f:
# data = json.load(f)
# sample = data[2]
# print(sample['date'])
