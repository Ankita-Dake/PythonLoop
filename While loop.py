# using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# using break statement
i = 1
while i <= 10:
    print(i)
    if i==6:
        break
    i += 1

# using continue statement
i = 1
while i <= 10:
    i += 1
    if i==6:
        continue
    print(i)
