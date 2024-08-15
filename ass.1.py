total_money = 50
item_cost = 15
tax_item = item_cost*0.03
total_item_cost = float(item_cost) + float(tax_item)
money_left = float(total_money) - float(total_item_cost)
print(money_left)

