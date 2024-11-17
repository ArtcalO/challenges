""""
Write a function called convert_add that takes a list of strings 
as an argument and converts it to integers and sums the list.

"""
from typing import List


def convert_add(data:List[str]):
    sum=0
    for x in data:
        try:
            sum+=int(x)
        except ValueError:
            continue    
    return sum

print(convert_add(['01','3','5','d']))


