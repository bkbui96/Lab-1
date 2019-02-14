#Question 6
import requests
from bs4 import BeautifulSoup
import os

opened = open("file_to_write.txt", "w") #Creates the file to write
html = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")
parsed = BeautifulSoup(html.content, "html.parser")
table = parsed.find('table') #"table" keyword is used for tables in HTML
table_rows = table.find_all('tr') #tr means table rows

m = 0
state_names_list = []
for tr in table_rows:
    Th = tr.find_all('th') #Gets the headers which are the names of the states
    row = [i.text for i in Th]
    if m in range(2,52): #To avoid first 2 blank header cells
        state_names_list.append(row)
    m += 1

opened.write("Names of the states\n")
opened.write(str(state_names_list))
opened.write("\nInformation about the states\n")

for tr in table_rows:
    Td = tr.find_all('td') # To get the table cells
    row = [i.text for i in Td]
    for c in row:
        opened.write(c)
    opened.write("\n")

opened.close()

