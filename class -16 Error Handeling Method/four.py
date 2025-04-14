#print(10/0)
try:
    print(10/0) #program createing Error
    #raise ZeroDivisionError ("Zero Division Error") # we are creating and throwing
except ZeroDivisionError as err:
    print(err)