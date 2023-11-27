import re

def search_in_file(pattern: str, file_name: str) -> None:
    with open(file_name) as f:
        lines = f.read().split('\n')
        for line in lines:
            if re.search(pattern, line):
                print(line)

# Pattern: contains 'oo'
search_in_file(r'oo', 'names.txt')

# Pattern: contains at least 3 'o' (not necessarily consecutive)
search_in_file(r'o.*o.*o', 'names.txt')

# Pattern: contains only vowels
search_in_file(r'^[aeiouyAEIOUY]+$', 'names.txt')

# Pattern: contains only consonants
search_in_file(r'^[^aeiouyAEIOUY\s]+$', 'names.txt')

# Pattern: starts with B or D and ends with w or z
search_in_file(r'^[BD].*[wz]$', 'names.txt')

# Pattern: contains 'inf' or 'rec'
search_in_file(r'inf|rec', 'names.txt')

# Pattern: contains only vowels (excluding first and last letter), exactly 5 letters
search_in_file(r'^[^aeiouyAEIOUY].*[aeiouyAEIOUY][^aeiouyAEIOUY]$', 'names.txt')

# Pattern: starts and ends with A, at most 4 letters
search_in_file(r'^A[A-Za-z]{0,2}A$', 'names.txt')

# Pattern: starts with N or M, contains at least 5 vowels
search_in_file(r'^[NM].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY]', 'names.txt')

# Pattern: contains at most 2 characters other than 'a', 'l', 'm', 'n'
search_in_file(r'^[almn]{0,2}$', 'names.txt')
