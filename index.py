#SLICE A STRING

x="python compiler"
print(x[1:3])

print(x[:3])
print(x[1:])

#NEGATIVE INDEX

print(x[-8])

print(x[-4:-2])


# MODIFY THE STRINGS

x="new python code"

print(x.upper())
print(x.lower())

x="hello coders!"

splittedText = x.split()

print(splittedText[1])

#REPLACE A STRINGS WITH ANOTHER ONE

x = "Hello python"
print(x.replace("o", "A"))

a='hello'
b='coders'
c=a+b

print(c)
  

  #BOOLEANS

print(4>6)
print(6>4)
print(4>=6)


print(bool(4))
print(bool(6))
print(bool())


mylist=[10,20,40]
print(mylist)

mylist=('katty','peter',400,"apple")
print(mylist[0])
print(mylist[3])


mylist=(1,3,5,6,1,3,5)
print(mylist)


#EXTEND()

list1 = [1,2,0,3]   
list2 = [4,6,8,7]  
print(list1)
print(list2)
list1.extend(list2)

print("After Extend:",list1)


#REMOVE LIST ITEMS

list1 = ["java","python","css","html"]
del list1[-1]
print(list1)








