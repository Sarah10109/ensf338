import timeit

wordcount = 0
vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

array_lines = []

start_loading = False

with open('moby_dick.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        if line.strip() == 'CHAPTER 1. Loomings.':
            start_loading = True
        if start_loading:
            array_lines.append(line.strip())

def calc_avg_vowels():
    wordcount = 0
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for i in array_lines:
        for word in i.split():
            wordcount += 1
            for char in word:
                if char.isalnum():
                    if char.isdigit():
                        pass
                    elif char.lower() in vowels:
                        vowel_count += 1
                    else:
                        pass
    avg_vowel_per_word = vowel_count/wordcount
    return avg_vowel_per_word

print('Average number of vowels per word: ', calc_avg_vowels())

# Takes sum of calculating average vowels per word 100 times
sum_time_elapsed = 0
for num in range(100):
    time_elapsed = timeit.timeit(lambda: calc_avg_vowels(), number = 1)
    sum_time_elapsed += time_elapsed

# Calculate average time elapsed across the 100 iterations
avg_time_elapsed = sum_time_elapsed/100
print('Average time elapsed: ', avg_time_elapsed)