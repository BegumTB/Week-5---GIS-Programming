file = open("words.txt","r")

fin = open('words.txt')
fin.readline()

line = fin.readline()
word = line.strip()
word



#Write a program that reads words.txt and prints only the words with
#more than 20 characters (not counting whitespace)

#1.option
fin = open('words.txt')
line = fin.readline()
word = line.strip()
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print (word)

        
#2.nd option
fin = open('words.txt')
line = fin.readline()        
words = line.strip()
for line in fin:
    words = line.strip()
    if len(words) > 20:
        print (words)

#Result:
#counterdemonstrations
#hyperaggressivenesses
#microminiaturizations

#this code lists/writes ALL words in the list.
#Don't run randomly, it may take long. 
#     fin = open('words.txt')
#     for line in fin:
    #     word = line.strip()
    #     print(word)

    

    



            
