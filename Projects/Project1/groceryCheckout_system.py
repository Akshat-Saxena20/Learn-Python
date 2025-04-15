# Grocery checkout System mini project
prices={

    "apple":80,
    "banana":60,
    "milk":28,
    "floor":250,
    "rice":50,
    "cheese":120
}

item1_name=input("Enter the name of your first item:").lower()
item1_qty=int(input(f"Enter the qty of {item1_name}"))

item2_name=input("Enter the name of your second item:").lower()
item2_qty=int(input(f"Enter the qty of {item2_name}"))

item3_name=input("Enter the name of your third item:").lower()
item3_qty=int(input(f"Enter the qty of {item3_name}"))

item1_price=prices.get(item1_name,0)
item2_price=prices.get(item2_name,0)
item3_price=prices.get(item3_name,0)

item1_total=item1_qty * item1_price
item2_total=item2_qty * item2_price
item3_total=item3_qty * item3_price

subTotal=item1_total + item2_total + item3_total
tax=subTotal * 0.085
total_amount=subTotal+tax


print("\n------Receipt-----------------")
print("\n*************Menu************************")
print(f"{item1_name.capitalize()} : {item1_qty} @ Rs.{item1_price:.2f}  each = Rs.{item1_total:.2f}")
print(f"{item2_name.capitalize()} : {item2_qty} @ Rs.{item2_price:.2f}  each = Rs.{item2_total:.2f}")
print(f"{item3_name.capitalize()} : {item3_qty} @ Rs.{item3_price:.2f}  each = Rs.{item3_total:.2f}")
print(f"Subtotal: Rs.{subTotal:.2f}")
print(f"Tax: Rs.{tax:.2f}")
print(f"Total Amount: Rs.{total_amount:.2f}")





