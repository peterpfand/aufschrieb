weight = float(input("""Gib hier dein Gewicht ein...
"""))
height = float(input("""
Gib hier dein Alter ein
"""))

bmi = weight/ height **2
#print (bmi)
if bmi <18.5:            #define underweight
    print("""
You are Underweight""")

elif bmi >=25 and bmi <30:      #define overweight
    print ("""
You are Overweight""")

elif bmi >=18.5 and bmi <25:  #define normal
    print ("""
You are Normal""")

elif bmi >=30:                   #define obesity
    print ("""
You are Obesity""")
