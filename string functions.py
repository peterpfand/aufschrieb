#String Functions

#join - joins a list of strings with another string as a separator.

#Example
a = ""


a.join(('M','C','U'))

print(a)






#replace - replaces one substring in a string with another.

#startswith and endswith - determine if there is a substring at the start and end of a string, respectively.

#lower and upper – changes the case of a string

#SPLIT -the opposite of join, turns a string with a certain separator into a list. str.split(separator)
#Example:
Variable_Text = "Du kleines stück Scheisse lern mehr tu es für den 34er Skyline"
print (Variable_Text.split(" "))      #Output:['Du', 'kleines', 'st�ck', 'Scheisse', 'lern', 'mehr', 'tu', 'es', 'f�r', 'den', '34er', 'Skyline']


'''format

The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.'''
