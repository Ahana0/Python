#LIST IS MUTABLE, WHICH MEANS IT CAN BE CHANGED
grocery = ["biscuits", "hand wash", "jam", "peanut butter", "juice", "powder", "body mist"]
print(grocery)
print(grocery[2])
numbers = [3,5,7,5,23,12]
#numbers.sort()    #for sorting a list
#numbers.reverse() #for reversing a string
print(numbers)
#slicing
print(numbers[0:5])
print(numbers[:5])
print(numbers[1:4])
print(numbers[:6:])

#length of a list, max min

print(len(numbers))
print(max(numbers))
print(min(numbers))

#append = adding stuffs in the end of a list
numbers.append(78)
print(numbers)

#inserting numbers
#numbers.insert(index,number to put in)
numbers.insert(1,68)

#removing a number from the list
numbers.remove(23)

#removing last number from the list
numbers.pop()

#changing the list
numbers[1] = 98
print(numbers)
