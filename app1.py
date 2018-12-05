import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn=input("Didyou mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys()))
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word does not exist. Please double check it"
        else:
            return "we did not understand your entry"
    else:
        return "The word does not exist. Please double check it"

word=input("Enter the word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)    
