number = []
n = int(input('Total input: '))

for i in range(n):
    x = int(input('Enter the numbers: '))
    number.append(x)

print('initial list: ', number)

number = list(set(number))
print("without duplicates: ", number)

number.sort(reverse=True)
print('sorted in descending order', number)

result = []
for num in number:
    if num % 3 != 0:
        result.append(num)
print("without the numbers that are divisible by 3: ", number)


print('modified list: ', result)



