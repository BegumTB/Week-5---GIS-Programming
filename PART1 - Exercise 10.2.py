#Write a function called cumsum that takes a list of numbers
#and returns the cumulative sum; that is, a new list where the ith element
#is the sum of the first i + 1 elements from the original list.

t = [3, 8, 4]

def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res



    
        
        
        
  


