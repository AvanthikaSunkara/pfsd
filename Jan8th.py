import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
myList=["Avanthika","Nithya","Gaythri","Vishnu"]
dict={"name":"avanthika","age":17}
myList1={"Avanthika","Nithya","Gaythri","Vishnu"}
print(random.choice(myList))
print(random.choice(list(dict)))
random.shuffle(myList)
