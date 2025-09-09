
def bill(con_num,con_name,pmr,lmr):
    tu = pmr-lmr
    
    if tu<=50:
        b=3.80*tu
    elif tu<=100:
        b= 3.80*50 + (tu-50)*4.20
    elif tu<=200:
        b= 3.80*50 + (50)*4.20 + (tu-100)*5.10
    elif tu<=300:
        b= 3.80*50 + (50)*4.20 + 50*5.10 + (tu-150)*6.30
    else:
        b= 3.80*50 + (50)*4.20 + 50*5.10 + (50)*6.30 + (tu-200)*7.50

    print("\nConsumer Details:")
    print(f"consumer name: {con_name} \nconsumer number: {con_num} \nBill: {b:.2f}")


con_num = int(input("Enter consumer number:"))
con_name = input("Enter consumer name:")
pmr = int(input("Enter present month reading:"))
lmr= int(input("enter last month reading:"))
bill(con_num,con_name,pmr,lmr)

