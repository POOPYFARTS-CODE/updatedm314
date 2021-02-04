info = open("info.txt").readlines()
info = list(map(lambda x:x.strip(),info))
first_n = info[1]
last_n = info[2]
addres_line1 = info[3]
addres_line2 = info[4]
city = info[6]
zip = info[5]
phone_no = info[6]
paypal_pass = info[7]



print(first_n)
print(last_n)
print(addres_line1,addres_line2)
print(city)
print(zip)
print(phone_no)
print(paypal_pass)