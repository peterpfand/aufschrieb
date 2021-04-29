#print("{0}{1}{0}".format("abra", "cad"))

#ANSWER IS :: abracadabra
#Explanation:: first the program places "abra" to {0} And then it places " cad" to {1} And lastly it places " abra" again to {0}
#Hence the answer is ::: abracadabra

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
