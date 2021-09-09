myDict={}
myDict["one"]=1 
myDict["two"]=2
myDict[3]="three"
myDict["four"]=4

print(myDict);
print(myDict.get(3))

for key in myDict:
    print(str (key) +' : ' + str( myDict.get(key)))