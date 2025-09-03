con_num = int(input("Enter consumer number:"))
con_name = input("Enter consumer name:")
pmr = int(input("Enter present month reading:"))
lmr= int(input("enter last month reading:"))

tot_units = pmr-lmr

bill = tot_units*3.80 #amt per unit  is 3.80

print("\nConsumer Details:")

# print("Consumer name:"+con_name + "\n" + "consumer number:" + str(con_num)+ "\n"+ "current bill:" + str(bill))


print(f"consumer name: {con_name} \nconsumer number: {con_num} \nBill: {bill:.2f}")