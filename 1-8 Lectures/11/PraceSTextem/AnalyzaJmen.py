import csv
from collections import Counter

def most_common_names(filename: str, count: int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        names = [row[0] for row in reader]

    name_counts = Counter(names)

    most_common = name_counts.most_common(count)

    print(f"{count} most common names:")
    for name, occurrences in most_common:
        print(f"{name}: {occurrences} occurrences")

# Test the function
most_common_names('jmena.csv', 10)
