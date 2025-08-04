#student score
score = float(input("enter a score:"))
if score >= 70 and score <= 100:
	print("A")
elif score >= 60 and score <= 70:
	print("B")
elif score >= 40 and score <= 50:
	print("C")
elif score >= 30 and score <= 40:
	print("D")
elif score >= 0 and score <= 30:
	print("F")
else:
	print("invalid Range")

customer = {
	"name": "Godiya", "order_amount": 25000, "Loyalty_card": True, "is_student": False
}

print(customer["Loyalty_card"])
print(customer["is_student"])
print(customer["order_amount"])

discount_percentage = 0
order_amount = customer["order_amount"]
if customer["Loyalty_card"]:
     discount_percentage += 10


if order_amount > 20_000:
    if customer["Loyalty_card"]:
       discount_percentage += 5

else:
	print("Free Drink")

if customer["is_student"]:
    discount_percentage += 5

discount = (discount_percentage / 100) * order_amount
customer.update({
	"discount": discount,
	"discount_percentage": discount_percentage,
	"amount_to_pay": order_amount - discount
})
print(customer)

order_summary = {"customer1": customer}


