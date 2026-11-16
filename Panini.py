mine = {"pizza", "pasta", "salad", "sandwich", "fries"}
friend = {"burger", "fries", "salad", "sushi", "pizza"}
print("All foods:", mine | friend)
print("Food we both like:", mine & friend)
print("Food  only I like:", mine - friend)
print("Food only one of us likes:", mine ^ friend)