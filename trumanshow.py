
def change_to_lowercase(txt):
    return txt.lower()

with open("trumanshowscript") as f:
    a=f.read()

a=(change_to_lowercase(a))

#word = input("Enter the word you want to look for in the text: ")


#for word in word:
    # if word.isupper():
      # word=word.lower()

def look_for_word():
    word = input("Enter the word you want to look for in the text: ")
    for word in word:
        if word.isupper():
            word = word.lower()

    if word in a:
        print("The string you are looking "
          "for is in TrumanShow.")
    else:
        print("string you look for is not in the text file.")


    print(a.count(word,0,len(a)))

print(look_for_word())


