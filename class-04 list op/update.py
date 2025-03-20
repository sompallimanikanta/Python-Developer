ename=['Rahul Gandhi','Sonia','Priya','Modi']
#index        0          1       2       3
#-veIndex     -4         -3       -2      -1

print(ename)
#How to read list elements - using indexing
#update list elements
ename[3] ='PM Naredra Modi'
print(ename)

# delete list elements
ename.pop()     #['Rahul Gandhi', 'Sonia', 'Priya', 'PM Naredra Modi']
print(ename)    #['Rahul Gandhi', 'Sonia', 'Priya']
