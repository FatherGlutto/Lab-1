numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_numbers = [i for i in numbers if i is not None]
a = sum(new_numbers)/(len(new_numbers)+1)
for i in range (len(numbers)):
    if numbers[i] is None:
        numbers[i]=a
print('Измененный список:', numbers)
