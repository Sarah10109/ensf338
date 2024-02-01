
wordcount = 0
consonant_count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

array_lines = []

start_loading = False

with open('moby_dick.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        if line.strip() == 'CHAPTER 1. Loomings.':
            start_loading = True
        if start_loading:
            array_lines.append(line.strip())

for i in array_lines:
    for word in i.split():
        wordcount += 1
        for char in word:
            if char.isalnum():
                if char.isdigit():
                    pass
                elif char.lower() not in vowels:
                     consonant_count += 1
                else:
                     pass

avg_consonant_per_word = consonant_count/wordcount
print('Average number of consonants per word: ', avg_consonant_per_word)