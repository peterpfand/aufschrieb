#list =["erik","musik","nudelsuppe"]            #schreibweise 1
list = [                                        #schreibweise 2 kann auch eingerückt sein, sieht dann halt besser aus
"erik",
"musik",
"nudelsuppe"
]
print(list)

l = [0,1,2,3]
l.append(4)
l.append(6)
l.extend([7,8,9])
l.insert(5,5)
l.extend([15])
l = l + [16,17]

l[1] = 100

print (l[0])

print(l[1])

print (l[-1])

print (l)

list_1 = ['c','b','a']
list_2 = [2,1,0]
ultimative_liste = [list_1,list_2]

print (ultimative_liste)

print("_______________________________________________________")

letters = ["a", "b", "c"]
letters += ["d"]
print(len(letters))     #answer is 4

#max(list): Returns the maximum value.
#min(list): Returns the minimum value.
#list.count(item): Returns a count of how many times an item occurs in a list.
#list.remove(item): Removes an item from a list.
#list.reverse(): Reverses items in a list.

#s.append(x)
#Hängt x ans Ende der Liste s an

#s.pop(i)
#Gibt das i-te Element von s zurück und entfernt es dabei aus der Liste, Ist i nicht angegeben, wird das letzte Element genommen
