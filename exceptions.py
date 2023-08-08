try:
    print(x)
except:
    print("an eerror ocuured")  

try:
    print(y)
except NameError:
    print("undefined variable")
except:
    print("an error")    

#with else
try:
    print("fat head")
except:
    print("a big fat head")
else:
    print("everything is good") 

#with finally
try:
    print(t)
except:
    print("undefined variable")
finally:
    print("its done")     

#raising exceptions.
w=10
if w >20:
    raise Exception("all numbers are above 20")              