import csv

file_path = 'data/country.csv'

with open(file_path, encoding='utf8') as f:
    csv_reader = list(csv.reader(f, delimiter=","))  # read while file is open


    # Print the csv_reader object (shows it's a reader)
    print(csv_reader)

    # Example 1: Skip the first line using next()
    # next(csv_reader)

    # Example 2: Basic printing of all rows/records
    # for line in csv_reader:
    #     print(line)

    # Example 3: Access index numbers and headers
    # for each row, get row number and line data
    # for line_no, line in enumerate(csv_reader, 1):
    #     # If line 1, print separately as headers
    #     if line_no == 1:
    #         print("Header:")
    #         print(line)
    #         print("Data:")
    #     else:
    #         print(line)

#  Opening csv as a dictioanry
# with open(file_path, encoding='utf8') as f:
#     csv_reader = csv.DictReader(f)

#     next(csv_reader)

#     for dict in csv_reader:
#         # print(f'The area of {dict['name']} is {dict['area']} km2')
#         print(dict)

# opening as dictionary but with customer field names
field_names = ['Country name', 'Area', 'Code2', 'Code3']

with open(file_path, encoding='utf8') as f:
    csv_reader = csv.DictReader(f, field_names)

    for dict in csv_reader:
        print(dict)