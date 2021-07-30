#Author: Emil
#Description: Body Mass Index Calculator using Imperial system

print("Hello, welcome to your Body Mass Index(BMI) Calculator!\n")

while True:
	try:
		height = float(input("Please enter your height here in inches: "))
		break
	except ValueError: #making sure user entered number correctly
		print("Enter a valid positive number please")

while True:
	try:
		weight = float(input("Please enter your weight here in pounds: "))
		break
	except ValueError:
		print("Enter a valid positive number please")

healthy = False #to provide them relevant articles based on if they are healthy or not

bmi = weight/(height**2) * 703 #body mass index equation for imperial system
bmi = round(bmi, 2) #rounds our bmi value to 2 decimal places

print("Your Body Mass Index is: ", bmi)

if(bmi<=16):
	print("You're Severely Underweight")
elif(bmi<=18.5):
	print("You're Underweight")
elif(bmi<=25):
	print("You're Healthy!")
	healthy = True
elif(bmi<=30):
	print("You're Overweight")
else: 
	print("You're Severely Overweight")

print("\nWhat's next? Check out these resources provided by the CDC and NIH for achieving that healthy lifestyle!\n")
if healthy == True: #if user is in a healthy bmi, we'll provide links about maintaing that
	print("Maintaing that healthy weight: ")
	print("-> https://www.cdc.gov/healthyweight/prevention/index.html")
	print("-> https://www.nhlbi.nih.gov/heart-truth/maintain-a-healthy-weight")
else: #if user is underweight or overweight, we'll provide resources on steps for them to try
	print("-> Achieving that Healthy Weight:https://www.cdc.gov/healthyweight/index.html")
	print("-> Physical Activity: https://www.nhlbi.nih.gov/heart-truth/increase-physical-activity")
	print("-> Healthy diet: https://www.nhlbi.nih.gov/heart-truth/eat-a-heart-healthy-diet")
print()


