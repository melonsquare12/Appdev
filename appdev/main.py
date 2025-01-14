import random

thesaurus = {
    "hot": ['summer' , "boiling"],
    "cold": ['chill' , "freeze"],
    "happy": ["merry" , "cheer"]
}

print("Choose a word")
for key in thesaurus.keys():
    print("t-" + key)

choice = input("Enter a word:").lower().strip()

if choice in thesaurus:
    synonym = random.choice(thesaurus[choice])
    print(f"A synonym for {choice} is {synonym}.")
else:
    print("Sorry, not in thesaurus.")    