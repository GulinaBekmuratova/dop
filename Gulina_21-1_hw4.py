data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
letters.reverse()
numbers.sort()
letters[1] = 'G'
letters[7] = 'c'
for i in range (len(numbers)):
    numbers[i] *= numbers[i]
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)