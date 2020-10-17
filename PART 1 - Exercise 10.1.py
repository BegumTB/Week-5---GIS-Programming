
#Write a function called nested_sum that takes a
#list of lists of integers and adds up the elements
#from all of the nested lists.

t = [[1, 5], [6], [7, 8, 9]]
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total




