# here we just write a small code to giving the user give their information.


a = int(input("Enter your body weigt in KG:-"))
b = int(input("Enter your height in cm :-"))


# we just convert cm --> m
c = b / 100

#Here we make square  of height
d = c * c

#Here we use BMI formula
x = a / d

#Here X is for BMI And here we just print it

print (x)

#From here we stard using IF,ELIF,ELSE concept
if x < 18.5 :
    print("Underweight")
elif x <= 24.9 :
    print("Healthy Weight")
elif x <=  29.9 :
    print("Overweight")
elif x <= 34.9 :
    print("Obesity (Class I)")

elif x <= 39.9 :
    print("Obesity (Class II)")

else:
    print("Severe Obesity (Class III)")





    # thank you :) to vist my github . 
    