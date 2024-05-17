import os
import csv

input_file = "./budget_data.csv"
output_file = "./output.txt"


total_months = 0
month_of_change = []
net_change_list = []
graetest_increase = ["",0]
greatest_decrease = ["",9999999999]
total_net = 0

with open(input_file) as f:
    reader = csv.reader(f)
    header = next(reader)
    first_row = next(reader)
    total_months += 1

    total_net = int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > graetest_increase[1]:
            graetest_increase[1] = net_change
            graetest_increase[0] = row[0]
      
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]
net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Month : {total_months}\n"
    f"-------------------------\n"
    f"Total: {total_net}\n"
    f"----------------------\n"
    f"Average Change {net_monthly_avg:.2f}\n"
    f"--------------------------------------\n"
    f"Greatest increase in profits : $ {graetest_increase[1]} in month {graetest_increase[0]}\n"
    f"Greatest decrease in profits: $ {greatest_decrease[1]} in month {greatest_decrease[0]}\n"
)

print(output)

with open(output_file, "w") as file:
    file.write(output)
