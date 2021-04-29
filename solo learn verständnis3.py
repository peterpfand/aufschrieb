list = [5, 2, 3, 4]

if len (list) % 2 == 0:
    print(list[0])     #answer is "5"

print("_______________________________________________________")

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])                   # answer is "y"


print("_______________________________________________________")

list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break                           # answer is "5"

print("_______________________________________________________")

What's the output of this code?
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])                                #answer is [1,25,81]

print("_______________________________________________________")

x = [6, 4, 2, 9]
x = x[::-1] #reverses the list
print(x[0]+x[2])   #reversed list addition           #answer is 13

print("_______________________________________________________")
                        # module quiz üben weil wtf is that
N = int(input())
sum =0
for i in range(1,N+1):
	sum+=i
print(sum)

print("_______________________________________________________")
