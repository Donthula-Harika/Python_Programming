import ecomerce_utils
cart ={"laptop":55000,"phone":30000, "HeadPhones":2000}
dis_per = int(input("Enter dicount percentage: "))
gst_per = int(input("Enter GST percentage: "))
ecomerce_utils.generate_invoice(cart,dis_per,gst_per)