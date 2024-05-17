import os
import csv
#Path to collect data from the Resource Folder 
budget_data_csv='Resources/budget_data.csv'
#budget_data_csv=os.path.join("python-challenge","PyBank","Resources","budget_data.csv")
with open(budget_data_csv) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(csv_file)# Skip the header row if it exists
     print(f"Header: {csv_header}")
    

     months_set = set()  # Using set to store unique month-year combinations
        
     for row in csv_reader:
            # Assuming the column index containing the month-year information is 0
            month_year = row[0]
            months_set.add(month_year)
    

# Call the function to get the total number of unique month-year combinations
     total_months = len(months_set)
     print("Total number of months included in the dataset:", total_months)     

 #The net total amount of "Profit/Losses" over the entire period     
     for row in csv_reader:
     
        profit_loss = int(row[1])  # Convert the value to an integer if it's numeric
        net_total = profit_loss
        print(net_total)