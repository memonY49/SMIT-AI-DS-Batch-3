# data = ["Yasir","abc@gmail.com","abc123"]

# useremail = input("Enter your Email: ")

"""
if useremail == data[1]:
    for i in range(0,3):
        userpass = input("Enter your Pass: ")
        if userpass == data[2]:
            print(f"Name: {data[0]}\nEmail: {data[1]}")
        else:
            print("Incorrect Password")
    else:
        print("You are blocked now!!!")
else:
    print("Invailed user")
"""

# functionname()
data = [1,3,4,6,7,8,0,78,0,0,0,0,0,0,0,0]

print(data)

# data.append(100)
# data.clear()

# data.insert(4,10000)
#re_element = data.pop(3)
# data.remove(0)
# data.reverse()
# data.sort(reverse = True)
# print(len(data))
#print(f"Poped {re_element} from data list")

#for i in range(0,data.count(0)):
#    data.remove(0)


for i in range(0,len(data)):
    if data[i] == 0:
        print(i, end = ",")
























