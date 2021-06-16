import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
   
    if word in data:
        return (data[word])
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s ?"%get_close_matches(word,data.keys())[0])
        decide=input("Y for yes n for no>>")
        if(decide=='y'):
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return ("Not found")

    else:
        print("Word Not found")     
print("Enter the word you want to search")
word=input()

ans = translate(word)
if type(ans)==list:
    for item in ans:
        print(item)
else:
    print(ans)

