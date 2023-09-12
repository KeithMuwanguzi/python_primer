def do():
    data = [1,'sdome',2,3,4,'1',3,'a','fjyasdc',12,'dfgdf']
    newList = []
    for n in data:
        if not isinstance(n,str):
            newList.append(n)
    return newList

print(do())