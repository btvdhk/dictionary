import json

#load json data
data = json.load(open("data.json"))

#take word from user
word = input("Enter Your Word: ")

#function to return meaning of the word from data
def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    #if-else to check word exist in our data or not
    if w in data:
        return data[w]
    else:
        return("Word is not exist! please try again.")

#function call to get meaning of word entered by user
meaning = getMeaning(word)

if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)