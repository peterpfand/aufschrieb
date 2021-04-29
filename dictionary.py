#erik = {"name" : "erik", "age" : "18", "courses": ["python_beginner","python_intermediate"]}    #schreibweise 1
erik = {                                                                                        #schreibweise 2
    "name" : "erik",
    "age" : "18",
    "courses": ["python_beginner","python_intermediate"]
}



def things_erik():
    for things in erik:
        print(things)
things_erik()

print('')                   #produces one empty line of code because of reasons
print(erik['name'])
print(erik['age'])
print(erik['courses'])


print(erik.get('phone'))                                                #prints default "None" instead of an error if the iten you wanted to print does not exist
                                                                        #but you can determine a custom error massage like this:
                                                                        #print(erik.get('item', 'error massage'))
