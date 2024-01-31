book = open("pg2701.txt", mode="r", encoding="latin-1")   
vowels = ["aeiouy"]
lines = []

for rows in  book:
    lines.extend([rows])

i = 842

consonants = 0
words = 0

while(i != 22315):
    line = lines[i].lower()
    oneline = (line.split(" "))
    

    """
    j = 0
    while(j != (len(oneline) - 1)):
        testword = oneline[j]
        length = len(testword)
        check1 = 0
        check2 = 0
        for letter in testword:
            check1 += 1
            if(letter.isalpha):
                break
            elif(check1 == length):
                check2 = 1
        if(check2):
            oneline.pop(j)
            continue
        else:
            j = j + 1
    """
    #Checks for words containing no letters and removes them. 
    #This code didnt effect the average so im unsure if I even need it


    words += len(oneline)
    
    for word in oneline:
        for letter in word:
            concheck = 1
            for check in vowels[0]:
                if not (letter.isalpha()):
                    concheck = 0
                    break
                elif(letter == check):
                    concheck = 0
                    break
            if(concheck):
                consonants += 1
                
    i = i + 1

average = consonants / words
print(average)


book.close()
    
        

    