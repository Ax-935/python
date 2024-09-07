#https://www.youtube.com/watch?v=epj-iWZcZSw&list=PLfBerWI98PypjENkNu0K27C7b6J40LAT6&index=10
jomle = "Dorood Bar Kuroosh Bozorg"
sentence = "aliRezA"
jomle_2 = "hi my name is alireza and im learning python with kaisen on Youtube"
space = "               "
# Upper : Write the string in capital
print("Upper do this :> ", jomle.upper()) 
jomle_capital = jomle_2.upper()
#lower : will write the string lowercase
print("Lower do this :> ", jomle.lower())
#Center : Write the string in the center and, put the thing in '' or ""  in right and left
print("Center do this :> ", sentence.center(25,':')) #The character between "" or '' will be repeated instead of space ::: by default sentence is written
#Count : Count a specific string in another string 
print("Count do this :> ", sentence.count("A")) #for e.g.:this will count A in the "Alireza" variable
print("Specified Count do this:>  ", jomle.count("o",15)) #This will count the given string from 15
print("Spesified Count do this :> ", jomle.count("o",1 ,15)) #This will count from 1 [not 0] to 15
#Index Will do this : find which [Number] is the given string starts from 
print("Index do this :> ", sentence.index("R")) #e.g.: The "R" is started from 3rd character in the given variable
print(jomle[11:11 + len("Bar")]) #Will print from 11 to 
#Capatalize : will wrtie the first character of the given string in capital :|
print(sentence.capitalize())
#Title : will write every first letter of the given string in capital
print(jomle_2.title())
#Replace : will replace the given string with the second given string
print("Replace do this :> ", jomle.replace("Bar", "Beh")) #("This", "With that")
#Casefold : will write the given variable (string of course) into lowercase
print("Casefold will do this :> ", jomle_capital.casefold()) #not much useful :(
#Endswith : will check if the given variable ends with the second given variable
print("Endswith do this :> ", jomle.endswith("Bozorg"))
#Startswith : will check if the mentioned (given) variable contains the given string
print("Startswith do this :> ", jomle.startswith("salam"))
#Find : will output the number of the given string , into the mentioned(given) variable
print("Find do this :> ", jomle.find("hola !")) #The output will be a int(number)
# print("The number is: ", jomle_2[jomle.index("Bar") + len("bo") ])

#Isalnum : will check if all the characters are alphanumeric(either alphabet or numbers nothing else even space) and outputs the result with True or False
print("Isalnum do this :> ",sentence.isalnum())
#Isdigit : will check if the given variable contains digit(number)
print("Isdigit do this :> ", sentence.isdigit())
#Isalpha : will check if the given variable contains alphabet(abcdefg...)
print("Isalpha do this :> ", sentence.isalpha())
#IsAcii : will check if the mentioned(given) variable contains ascii character or not 
print("IsAscii do this :> ", jomle.isascii())
#Islower : will chek if all the characters in mentioned(given) variable are lowercase 
print("Islower will do this :> ", sentence.islower())
#Isupper : will chek if all the characters in mentioned(given) variable are uppercase 
print("Isupper will do this :> ", sentence.isupper())

#Isspace : will chek if all the characters in mentioned(given) variable are space(s) 
print("Isspace will do this :> ", space.isspace())
print("Isspace will do this :> ", sentence.isspace())

#Zfill : {ZeroFill} will right the given number zero(S) before the text(string or smth) of the mentioned(given) variable :| :/
print("Zfill do this :> ", sentence.zfill(24))
#Ljust :  will Return a [Number] characters (U R input) long, left justified for the mentioned(given) variable 
print("Ljust do this :> ", sentence.ljust(10, "-")) # Variable.ljust(number)
#Rjust :  will Return a [Number] characters (U R input) long, right justified for the mentioned(given) variable 
print("Rjust do this :> ", sentence.ljust(100, "-")) # Variable.Rjust(number)
#Spilt : will Return a list from the mentioned(given)variable each word is thing in list (seperated words (space by default) in variable will be each a list part)
print("Spilt will do this :> ", jomle.split())
Kentence = "This-Is-sEntenCe-bEtWeeN-DaSheS-JoOn"
print("Spilt by - will do this :> ", Kentence.split("-")) #will recognize the things in given variable that have dash ( - ) between them

