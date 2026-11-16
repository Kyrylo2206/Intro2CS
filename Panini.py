words = {"apple" : "jabłko", "orange" : "pomarańcza", "book": "książka", "table": "stół"}
print("The translation of orange:" , words["orange"])
print("Number of pairs:", len(words))
words["cat"] = "kot"
words["book"] = "książeczka"
print("Updated dictionary:", words)
words.update({"water": "woda", "sun": "słońce"})
print("Dictionary with two new words:", words)
print("Keys:", list(words.keys()))
print("Values:", list(words.values()))
print("Pairs:", list(words.items()))