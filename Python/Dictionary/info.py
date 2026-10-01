info = {
    "key" : "value",
    "name" : "amit kumar sahu",
    "roll_no" : 20,
    "subjects" : ["maths","physics","chemistry","python"],
    "gender" : "male",
    "age" : 21,
    "is_adult" : True
}

print(info)
print(info["age"])
for i,j in info.items():
    print(i,j)