import csv
from collections import Counter
from typing import List

def most_common_names_years(filename: str, count: int, years: List[int]) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        name_year_dict = {row[0]: int(row[2]) for row in reader if row[2].isdigit()}

    filtered_names = [name for name, year in name_year_dict.items() if year in years]

    name_counts = Counter(filtered_names)

    most_common = name_counts.most_common(count)

    print(f"{count} most common names in years {years}:")
    for name, occurrences in most_common:
        print(f"{name}: {occurrences} occurrences")

# Test the function
most_common_names_years('jmena.csv', 10, [2005, 1996, 2003])
