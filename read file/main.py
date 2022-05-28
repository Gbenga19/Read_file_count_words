# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
file_name = input("Enter the filename: ")
def read_file_content(file_name):
    # [assignment] Add your code here 
    file = open(file_name, "r")
    lines = file.read()
    file.close()
    return lines
print(read_file_content(file_name))


def count_words():
    #text = read_file_content("./story.txt")
    # [assignment] Add your code here
    d = dict()
    f = open("story.txt", "r")
    data = f.read()
    word = data.split()
    for i in word:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])      
    f.close()
    
    
count_words()

  