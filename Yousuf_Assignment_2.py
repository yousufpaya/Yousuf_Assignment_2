# Question 1

age = int(input("Enter your Age: "))

if (age >= 0 and age <= 12):
    print("You are a Child")
elif (age >= 13 and age <= 19):
    print("You are a Teenager")
elif (age >= 20 and age <= 64):
    print("You are an Adult")    
else:
    print("You are a Senior")
	

# Question 2: Checking for Eligibility for Discount

cust_mem = input("Enter your Membership Status:")
pur_amt = int(input("Enter your Purchase Amount: "))

cust_mem = cust_mem.upper()

if ((cust_mem) == "PREMIUM") and (pur_amt >= 1000):
    print("You are eligible for discount")
elif ((cust_mem) == "REGULAR") and (pur_amt >= 2000):
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")
    


# Question 3: Voting Eligibility Check

citizen = input("Enter your Citizenship Status:")
age = int(input("Enter your Age: "))
region = input("Are you from a Special region where voting is allowed from age 16? Enter Yes or No:")

citizen = citizen.upper()
region = region.upper()

if (citizen == "CITIZEN") and (age >= 18):
    print("You are eligible for vote")
elif (citizen == "CITIZEN") and (age >= 16) and region == "YES":
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")


# Question 4: Employee Salary Bonus Eligibility

rating = input("Enter your Performance Rating:")
service = int(input("Enter your Years of Service: "))

rating = rating.upper()

if ((rating) == "EXCELLENT") and (service >= 5):
    print("You are eligible for Salary Bonus")
elif ((rating) == "GOOD") and (service >= 10):
    print("You are eligible for Salary Bonus")
elif ((rating) == "SATISFACTORY") and (service >= 15):
    print("You are eligible for Salary Bonus")
else:
    print("You are not eligible for Salary Bonus")


# Question 5. 

input_text = input ("Enter your text to replace spaces with underscores")
input_text = input_text.replace(" ", "_")
count = input_text.count("_")
position = input_text.index("_")
print ("New text is: "+ input_text)
print("Total underscores are: "+ str(count))
print ("The position of first underscore is: "+ str(position))


#Question 6: 


string_data = input("Enter your string data: ")
print("String data without the last 3 characters are:", string_data[:-3])
print("Every second character of the string is:", string_data[::2])
print("String data in reverse:" + string_data[::-1])



# Question 7. 

sentence = "Hello World, We are learning Python"
reverse_order = sentence.split()
reverseWord = reverse_order[::-1]
reversesentence = " ".join(reverseWord)
print("Reverse sentence is:" + reversesentence)


# Question 8. 

pcode = "SKU-12345-XYZ"
firstindex = pcode.find('-') + 1
lastindex = pcode.rfind('-')
num = pcode[firstindex:lastindex]
print("The product number is: " + num)




# Question 9. 

user_password = input("Enter your password")
 
res = any(ele.isupper() for ele in user_password)

print("String contains uppercase character : " + str(res))

res1 = any(ele.islower() for ele in user_password)

print("String contains lowercase character : " + str(res1))



# Question 10: Find the Longest Word

input_text = input("Enter your sentence: ")
data = input_text.split()  
longestword = max(data, key=len)
print("Longest word is: " + longestword)
