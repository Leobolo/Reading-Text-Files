# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file_content= open(filename, "r")
    file=file_content.read()
    punc= '''!<>;./,"'@#$%^*_-~`:?[]{}\|()'''
    no_punc= ""
    for char in file:
        if char not in punc:
            no_punc = no_punc + char
    return no_punc


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    newDict= {}
    myText=text.lower().split()
    #for line in text:
      #  line= line.strip().lower
      #  words= line.split(" ")
    for word in myText:
        if word in newDict:
            newDict[word]+= 1
        else: newDict[word]= 1
      
    return newDict

print(count_words())

