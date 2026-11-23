word = "play"
irregular_plurals = {"child" : "children", "mouse" : "mice"}
if word in irregular_plurals:
    print(irregular_plurals[word])
elif word[-1] in ("s", "x", "z"):
    print(word + "es")
elif word[-1] == "y" and word[-2] not in ("a", "e", "i", "o", "u"):
    print(word[:-1] + "ies")
else:
    print(word + "s")
