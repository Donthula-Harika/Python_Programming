def apply_discount(price,dis_per):
    dis_price = price-(dis_per*0.01*price)
    return dis_price

def gst(price,gst_per=18):
    new_price = price+(gst_per*0.01*price)
    return new_price

def generate_invoice(cart,dis_per=0,gst_per=18):
    dash="-"
    print(f"{dash*10}INVOICE{dash*10}")
    tot=0
    for k,v in cart.items():
        print(f"{k}    : Rs {v}")
        tot+=v
    print(f"{dash*27}")
 
    print(f"Subtotal: Rs.{tot}")
    discounted_price=apply_discount(tot,dis_per)
    print(f"After {dis_per}% dicount: Rs.{discounted_price}")
    print(f"After {gst_per}% GST: Rs.{gst(discounted_price,gst_per)}")
    
    print(f"{dash*27}")

    print("Thank you for shopping")



