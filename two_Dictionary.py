# Loading the data from json file...
import json
data = json.load(open("JsonFiles/Dictionary_data.json"))
# Now Datatype of data is 'dic' .
# print(data) , will print whole dictionary's data. 
# print(data['find out']) , will print meaning of 'find out'


from difflib import get_close_matches
def find_meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
        
    #case: upper,title alphabatic cases problem     
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
        
    #case: getting the closest match of entered word 
           # like for 'abc', closest match in [abcd,abde,bcdf] is 'abcd'.   
    elif len(get_close_matches(word,data.keys())) > 0 :
        closest=get_close_matches(word,data.keys())[0]
        print("Did you mean %s instead"%closest)
        decide=input("Please enter 'y' for yes and 'n' for no : ")
        if decide == 'y' :
            return data[closest]
        elif decide == 'n' :
            return "Ok then, entered word doesn't exist in our Dictionary."
        else:
            return "Please enter only 'y' or 'n'."
            
    #case: if someone entered some inappropriate words that does not exist
    else:
        return "Entered word doesn't exist in our Dictionary."

        
word = input("Enter the the word, which's meaning you want to find : ")
output = find_meaning(word)
if type(output) == list :
    for item in output:
        print(item)
else :
    print(output) # It is used when no match is found.   