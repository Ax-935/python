#if you wanna use 2 double qoutes in one sentence ::
# print ("Hello dear "Python learners") # it will give error
sentence = "The 7st episode of PyTh0N"
print("Hello dear \"Python\" learners") # we can use back-slash ( \ ) 
# \"Second Qoute\"
# One before the start of second qoute and on in the ending of first Qoute 
print("The text next to this will be on the next line\nHello dear from\t AliRezA") #\n means next line #\t means tab (for spaces)


#To count the lentgh of string we use len
print(len(sentence)) #len("Name of Variable")

#To slice {use a part of a variable} we use [fromTHisNumberTO:ThisNumber] e.g.: [1:10] from 1 t o10
print(sentence [0:8]) # from the 0st letter of variable to 8th letter of variable
print(sentence[0:10:2]) #from 0 to 10 move 2 by 2 
print(sentence[:12]) #If you let the first index , """"""By defalut the first number is 0 """""
# ""By defalut the first number of [] is 0 ""

print(sentence[:]) #If you let the both indexes empty , """" By defalut [:] means from start to end
#""""By defalut the [:] means from first to end