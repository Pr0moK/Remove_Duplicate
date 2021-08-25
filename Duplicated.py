numbers = [5, 3, 2, 1, 10, 15, 3]
uniq = []

for number in numbers:
   if number not in uniq:
       uniq.append(number)
uniq.sort()
print(uniq)