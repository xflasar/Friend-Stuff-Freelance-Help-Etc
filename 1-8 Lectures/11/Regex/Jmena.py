import re

def search_in_file(pattern: str, file_name: str) -> None:
    with open(file_name) as f:
        lines = f.read().split('\n')
        for line in lines:
            if re.search(pattern, line):
                print(line)

search_in_file(r'oo', 'names.txt')

search_in_file(r'o.*o.*o', 'names.txt')

search_in_file(r'^[aeiouyAEIOUY]+$', 'names.txt')

search_in_file(r'^[^aeiouyAEIOUY\s]+$', 'names.txt')

search_in_file(r'^[BD].*[wz]$', 'names.txt')

search_in_file(r'inf|rec', 'names.txt')

search_in_file(r'^[^aeiouyAEIOUY].*[aeiouyAEIOUY][^aeiouyAEIOUY]$', 'names.txt')

search_in_file(r'^A[A-Za-z]{0,2}A$', 'names.txt')

search_in_file(r'^[NM].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY].*[aeiouyAEIOUY]', 'names.txt')

search_in_file(r'^[almn]{0,2}$', 'names.txt')
