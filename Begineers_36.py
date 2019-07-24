string = raw_input()
count = 0
for i in string:
    if not(i.isdigit()):
        if not(i.isalpha()):
            count = count + 1
print count
