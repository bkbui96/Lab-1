# Program will prompt user to input a string. It will then find the longest string without repeating characters
# along with the length of that string.

x = input("Please input a string: ")

print("User's string: ", x)

mylist = [] # list to compare each character in for loop

temp_answer = ''
final_answer = ''

temp_length = 0
final_length = 0

for i in x:

    if i not in mylist: # if i is not in mylist
        mylist.append(i)    # add character in to mylist[] for future comparisons

        temp_length += 1 # increase temp_length by 1
        temp_answer = temp_answer + i # add i to temp_answer

    # resets temp_length and temp_answer
    elif i in mylist:
        temp_length = 1
        temp_answer = i

    # compare length of temporary answer to final answer, if the length is greater, then it updates the final answer

    if len(temp_answer) > len(final_answer):
        final_answer = temp_answer

    # compare length of temporary length to final length, updates length if temp_length is greater than final length
    if temp_length > final_length:
        final_length = temp_length

print('\n')
print(mylist)
print('\n')
print("Longest substring w/o repeating characters: ", final_answer)
print("Length of substring: ", final_length)
input()
