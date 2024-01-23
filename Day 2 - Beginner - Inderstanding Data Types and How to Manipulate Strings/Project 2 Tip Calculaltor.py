
print("Welcome to the tip calculator.")
total_pay = float(input("What was the total bill? "))
percentage = int(input("What percentage tip wuld you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))


tips_as_percent = percentage / 100
total_tip_amount = total_pay * tips_as_percent
total_bill = total_pay + total_tip_amount
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

print(final_amount)