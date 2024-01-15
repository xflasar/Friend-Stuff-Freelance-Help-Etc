import csv

def process_rows(file_name: str) -> None:
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            row = ''.join(row).split(';')
            if len(row) >= 4:
                id_number = row[1]
                semester = row[4].split('[')[1].split(' ')[1]
                cycle = row[4].split('[')[1].split(' ')[3].split(']')[0]

                print(f"{id_number}: {semester}. semestr {cycle} rocniku")

# Example usage
process_rows("students.csv")
