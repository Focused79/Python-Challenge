# Name Analysis, followed by line seperator: 

print("Financial Analysis:")
print("---------------------------")

# Import os and csv modules:

import os
import csv

# Set path for file to be analyzed:

csvpath = os.path.join("c:/Users/Albrecht/Desktop/BC Class Repo/SMU-VIRT-DATA-PT-12-2023-U-LOLC/Python-Challenge/PyBank/Resources/budget_data.csv")

# Set output path for analysis file: 

output_path = "analysis.txt"

# Set-up variables to store the number of months, the total of the "Profit/Losses" column, the sum of of the "Profit/Losses" column, and the index of the "Profit/losses" column:

number_months=0 
total=0
column_sum = 0
column_to_sum_index = 1

# Use with open to open csv file to count and print number of months:
    
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    number_months = len(list(csvreader))
    print(f"Total number of months: {int(number_months)}")

# Use with open to open csv file to calculate and print the sum of the "Profit/Losses" column:

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        column_sum += float(row['Profit/Losses'].replace(',',''))
    print(f'Total: ${int(column_sum)}')

# Use with open to open csv file to calculate the mean of the differences in the "Profit/Losses" column:

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    previous_value = None
    differences =[]

    for row in csvreader:
        current_value = int(row['Profit/Losses'])

        if previous_value is not None:
            difference = current_value - previous_value
            differences.append(difference)
        
        previous_value = current_value

if differences:
    mean_difference = sum(differences)/len(differences)
    print(f"Average Change: ${round(mean_difference, 2)}")

# Use with open to open csv file to determine the greatest increase in profits:

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    previous_date = None
    previous_value = None
    max_difference = float('-inf')
    max_difference_date = None

    for row in csvreader:
        current_date = row['Date']
        current_value = int(row['Profit/Losses'])

        if previous_value is not None:
            difference = current_value - previous_value 

            if difference > max_difference:
                max_difference = difference
                max_difference_date = current_date
        
        previous_date = current_date
        previous_value = current_value

if max_difference_date is not None:
    print(f"Greatest Increase in Profits: ${max_difference} (Date: {max_difference_date})")

# Use with open to open csv file to determine the greatest decrease in profits:
    
with open(csvpath) as csvfile:
        csvreader = csv.DictReader(csvfile)

        prev_date = None
        prev_value = None
        min_difference = float('inf')
        min_difference_date = None

        for row in csvreader:
            cur_date = row['Date']
            cur_value = int(row['Profit/Losses'])

            if prev_value is not None:
                diff = cur_value - prev_value

                if diff < min_difference:
                    min_difference = diff
                    min_difference_date = cur_date
            
            prev_date = cur_date
            prev_value = cur_value

if min_difference_date is not None:
    print(f"Greateest Decrease in Profits: ${min_difference} (Date: {min_difference_date})")

# Use with open to write results to output file:

with open(output_path, 'w') as output_file:
    print("Financial Analysis:", file=output_file)
    print("----------------------------", file=output_file)
    print(f"Total number of months: {int(number_months)}",file=output_file)
    print(f"Total: ${int(column_sum)}", file=output_file)

    if differences:
        print(f"Average Change: ${round(mean_difference, 2)}", file=output_file)
    if max_difference_date is not None:
        print(f"Greatest Increase in Profits: ${max_difference} (Date: {max_difference_date})", file=output_file)
    if min_difference_date is not None:
        print(f"Greatest Decrease in Profits: ${min_difference} (Date: {min_difference_date})", file=output_file)

# Use print function to verify that results have been exported to analysis.txt file:

print(f"The results have been written to: {output_path}")