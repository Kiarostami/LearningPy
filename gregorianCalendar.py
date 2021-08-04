# Not Fully Correct!  (2100 is wrong) 

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0: 
        leap = True
    elif year % 100 == 0: 
        return leap 
    elif year % 400 == 0: 
        leap = True
    else:
        return leap
    
    return leap

year = int(input())
print(is_leap(year))
