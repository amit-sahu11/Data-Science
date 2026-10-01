# mydict.keys()    # returns a list of all the keys
# mydict.values()  # returns a list of all the values
# mydict.itmes()   # returns a list of all the key-value pairs
# mydict.get("key") # returns the value of the key
# mydict.update(newdict) # updates the dictionary with new key-value pairs


info = {
    "name" : "amit",
    "roll_no" : 20,
    "subject" : ["maths","physics"]
}

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
print(info.get("na"))
print(info["name"])

# so here is a question why we use .get instid of sqaure brackets
# so if we don't get the item in dictionary .get dosen't throw error it simply return none

info1 = {
    "gender" : "male",
    "profession" : "student"
}

info.update(info1)
print(info)