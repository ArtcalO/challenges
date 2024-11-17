"""
Write a function called divide_or_square that takes one 
argument (a number), and returns the square root of the number 
if it is divisible by 5, returns its remainder if it is not divisible by 
5. 
"""
def divide_or_square(number):
    return number**(1/2) if number % 5 == 0  else number%5

print(divide_or_square(10))

def first_longest_value(data:dict):
    values = [value for value in data.values()]
    longest_value = values[0]
    for x in range(0,len(values)):
        if( x+1<len(values) and len(values[x+1])>len(longest_value)):
            longest_value = values[x+1]
            break
    return longest_value     

print(first_longest_value({'fruit': 'apple', 'color': 'green'}))