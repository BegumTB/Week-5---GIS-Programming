#Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

#Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage
#of words in the list that have no “e”.
#First Part
fin = open('words.txt')
line = fin.readline()
word = line.strip()
num_of_words = 0

for line in fin:
        word = line.split()
        num_of_words = num_of_words+1

print(num_of_words)
#RUN it. #Results in 113808.

#Second Part
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
        
fin = open('words.txt')
count = 0
num_of_words = 113808

for line in fin:
    word = line.strip()
    if has_no_e(word) == True :
        count += 1
        print(word)

#Third Part
print(count / num_of_words * 100, '%')
