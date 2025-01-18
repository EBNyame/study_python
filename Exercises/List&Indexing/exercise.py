numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd_numbers = [0 if num % 2 != 0 else num for num in numbers]
print(odd_numbers)