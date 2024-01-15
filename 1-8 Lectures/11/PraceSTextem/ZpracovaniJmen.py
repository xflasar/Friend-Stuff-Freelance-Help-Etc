def process_names(input_filename: str, output_filename: str) -> None:
    # Read names from the input file, process them, and sort
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        names = [name.strip().capitalize() for name in input_file]

    names.sort()

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for name in names:
            output_file.write(name + '\n')

# Test the function
process_names('NAMES.txt', 'names.txt')
