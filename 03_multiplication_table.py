number = int(input("Enter the number: "))

#i = 0  - range(1, 11) creates a sequence:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#"Is 0 in [1, 2, 3, ..., 10]?" Answer: No → So the loop never runs.

i = 1


while i in range(1, 11):
    if i ==5:
        i += 1
        continue
    print(number, "*", i, "=", number*i)
    i += 1
    
    #for i in range(1, 11):
    #print(number, "*", i, "=", number*i)