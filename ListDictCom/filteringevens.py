list_of_strings = input().split(",")

# list comprehension to convert strings to integers
numbers = [int(x) for x in list_of_strings]

# list comprehensio to filter on even numbers
result= [num for num in numbers if num%2==0]



print(result)