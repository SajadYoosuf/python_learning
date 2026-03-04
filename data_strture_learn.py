#this for string variblae creation syntax  in python
name:str="sajad"


print(name.upper())
age:int=25
print(age.is_integer())
hieght:float=25.0
married:bool=False
#creating a varibal ewith name and assing value
names:list=["asd","bsd","sajad"]
# this for indexing from first index to second index
# bsd

print(names[0:2])
print(names[-1])
names.append("ajaddfs")
nums=["sdafd","djafhkd"]
names.extend(nums)

print(names[-1])
#this is a tuple data struture this only create
#once not able to add another item in tuple
numbers:tuple=(1,2,3,4,5)
nums=(6,8,9)
tub=numbers+nums
# numbers[1]=7
# numbers.__add__(1)
print(type(numbers))
#this is accessing o'th index from to the remining 
#index
print(tub)
print(numbers[0:])




