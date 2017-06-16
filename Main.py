import urllib.request
import csv
import datetime
import operator

input1 = input("Enter Minimum Prevalence: ")

# Inport Excel File From FiveThirtyEight's GitHub
file_import = urllib.request.urlretrieve("https://raw.githubusercontent.com/fivethirtyeight/data/master/unisex-names/unisex_names_table.csv",
                           "unisex_names_table.csv")

# Open the file and convert it to a list
with open("unisex_names_table.csv", 'r') as file:
    reader = csv.reader(file)
    raw_list = list(reader)

# Scrap the first line from the list
list = raw_list[1:-1]

# Build the List of Names
output_list = []
for entry in list:
    if entry[2] >= input1:
        output_list.append(entry[1:3])

# Convert the List of Names to a Dictionary of Names
dictNames = {}
for entry in output_list:
    dictNames[entry[0]] = float(entry[1])

# Convert the dictionary into a sorted list
output_list = sorted(dictNames.items(), key=operator.itemgetter(1))

print(output_list)

# Write the list to a text file
file_output_name = datetime.datetime.now().strftime("%Y-%m-%d-%H%M") + " Output"
file_output = open(file_output_name, 'w')
for entry in output_list:
    file_output.write(entry[0] + ": " + str(entry[1]))

# Write the list to an excel file
with open(file_output_name+".csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(output_list))
    