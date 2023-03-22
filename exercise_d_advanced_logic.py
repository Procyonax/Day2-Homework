# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []

for number in numbers:
        if number % 2 == 0:
                even_numbers.append(number)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:

numbers.sort()

print(numbers)
print(len(numbers))

largest = numbers[len(numbers) - 1]
smallest = numbers[0]
difference = largest - smallest

print(difference)

## ALTERNATIVE
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for num in numbers:
        if num == 2 and numbers[num + 1] == 2:
                print(True)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

sum = 0
is_true = False
for number in numbers:
        if is_true == True:
                if number == 7:
                        is_true = False
        elif number == 6:
                is_true = True
        else: 
                sum += number

print(sum)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

index = 0
total = 0
for number in numbers:
        if number == 13 or numbers[index - 1] == 13:
            pass
        else:
            total += number
        index += 1
print(total)







