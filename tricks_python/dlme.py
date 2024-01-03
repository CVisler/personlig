import csv
import collections

long_string: str = ''
with open('1.txt', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        long_string = row[0]


""" Dictionary trick """
my_dict = {
    'square' + '_' + str(i): i**2 
    for i in range(5)
}

# print(my_dict)

""" Create chunks of the Dictionary """
def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

sample: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# long_string = 'AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG'

chunked = list(chunks(sample, 2))

# print(chunked[2])

""" Use Counter to count occurrences of chars in iterable """

tester = {}
long_string_out = long_string.count('AGATC')
long_string_out_2 = collections.Counter(long_string)
print(long_string)
