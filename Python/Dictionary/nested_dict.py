company = {
    "owner" : "abdfhkshd",
    "phone_no" : 1213546332,
    "employee" : {
        "name" : "amit",
        "age" : 21,
        "gender" : "male"
    }
}

print(company)
print(company["employee"])
print(company["employee"]["name"])
for i,j in company.items():
    print(i,j)