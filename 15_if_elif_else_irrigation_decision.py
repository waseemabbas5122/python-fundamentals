moisture = int(input("Enter the soil moisture: "))

if moisture < 30:
    print("Irrigate now")
elif moisture <= 60:
    print("Keep monitoring")
else:
    print("Skip today")