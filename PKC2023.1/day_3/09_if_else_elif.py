asif_age = input("How old is asif ...?")
asif_age = int(asif_age)            # Conversion of input
print(asif_age,type(asif_age))               # check type
required_age_for_coding = 33
# print(asif_age==asif_age_for_coding)

if asif_age == required_age_for_coding:
    print("You are Ready for Coding Enjoy......")
elif asif_age > required_age_for_coding:
    print("Congragulation You are Selected for Coding in Google......")
else: 
    print("You are Not Ready for Coding..... Better Luck Next Time")