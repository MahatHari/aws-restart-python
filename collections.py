myFruitList= ["apple", "babana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[1])
print(myFruitList[2])


# change values in list

myFruitList[2]='Orange'
print(myFruitList)

#Introducing Tuple,
myFinalAnserTupe=("apple", "banana", "pineapple")
print(myFinalAnserTupe)
print(type(myFinalAnserTupe))

# accessing typle elements is same as list(array)
print(myFinalAnserTupe[1])
print(myFinalAnserTupe[0])

# Creating Dictionary
myFavoriteFruitDictionary={
    "Akua": 'Apple',
    "Saanvi":"Banana",
    "Paulo":"Pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#accessing a dictonary by name
print(myFavoriteFruitDictionary["Akua"])
#accessing keys of dictionary
print(myFavoriteFruitDictionary.keys())
keys= myFavoriteFruitDictionary.keys()
print(keys)

j=0;
for i in myFavoriteFruitDictionary:
    if (j==1):
        print('2nd key using loop: ' +i)
    j=j+1
print('2nd key using keys (): '+ str (type(myFavoriteFruitDictionary.keys())))