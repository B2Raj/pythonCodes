str1="B2 \n"
str2='b2\n'
str3="""bittu\t"""
print(str1,str2,str3)


# summation of string
str4="Bittu"
str5=" Raj"
sum=(str4+str5)
print(sum)
print(len(str4))
print(len(str5))
print(len(sum))


#indexes of string

str6="Bittu"
print(str6[4])
print(str6[3])


# Slicing of string using indexes

str7="Bittu Raj"
print(str7[2:7])
print(str7[0:3])
print(str7[0:6])
print(str7[0:11])
print(str7[0:])
print(str7[0:len(str7)])
print(str7[:len(str7)])
print(str7[:11])
# backword indexing is also possible in Python only
print(str7[-6:-1])


# some Built-in function

str="my name is Bittu Raj"
print(str)
print(str.endswith("Raja"))
print(str.endswith("Raj"))
print(str)
print(str.capitalize())
print(str.replace("Bittu","B2"))
print(str.replace("name","Name"))
print(str.find("t"))
print(str.find("aman"))
print(str.count("t"))
print(str.count("Bittu"))



#   WAP to input user's first name and print its length and find the occurence of some words or letter in it



name=input("Enter your name: ")
print(name)
print("Length of name keyword is: ",len(name))
print("Total occurence of letter u is: ", name.count("u"))
print("Total occurence of letter t is: ", name.count("t"))







