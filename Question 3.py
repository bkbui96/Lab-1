#Question 3
user_input1 = input("Enter the names of the students attending Python class (separated by comma): ")
user_input2 = input("Enter the names of the students attending Web Application class (separated by comma) : ")

splitted_python = [p.strip() for p in user_input1.split(',')] #Comprehension to split the names by comma and get rid of the whitespace before and after the names to have accurate results
python_list = []
for i in splitted_python:
    python_list.append(i)

splitted_web_application = [l.strip() for l in user_input2.split(',')] #Comprehension to split the names by comma and get rid of the whitespace before and after the names to have accurate results
web_application_list = []
for k in splitted_web_application:
    web_application_list.append(k)

#Getting names on both lists
both_list = []
for t in python_list:
    if t in web_application_list:
        both_list.append(t)
print("List of students who are attending both classes : ", both_list)

#Getting names that are not common on both
not_common_list = []
for y in python_list:
    if y not in web_application_list:
        not_common_list.append(y)

for u in web_application_list:
    if u not in python_list:
        not_common_list.append(u)
print("List of students who are not common in both classes : ",not_common_list)
input()
