import timeit

book = open("pg2701.txt", mode="r", encoding="latin-1")   

lines = []

for rows in  book:
    lines.extend([rows])

def findcon(lines):
    vowels = ["aeiouy"]
    i = 842

    consonants = 0
    words = 0

    while(i != 22315):
        line = lines[i].lower()
        oneline = (line.split(" "))


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

    return (consonants / words)

time = timeit.timeit(lambda: findcon(lines), number=100)

averagetime = time / 100

print(averagetime)

book.close()






    
        

    
