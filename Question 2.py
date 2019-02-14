tuplist = [( "John", ("Physics", 80)) , ("Daniel", ("Science", 90)), ("John", ("Science", 95)), ("Mark",("Maths", 100)), ("Daniel",
("History", 75)), ("Mark", ("Social", 95))]

print ("Sort these list of tuples: ",tuplist, "\n")

Students = {}

for k,v in tuplist:
  if k in Students: # Checks if the key is already existing in dictionary then appends.
    Students[k].append(v)
  else: #
    Students[k] = [] # To bypass single key - value relationship, make the value a list and append as needed.
    Students[k].append(v)

for k,v in Students.items():
    print(k,v)
    input()
