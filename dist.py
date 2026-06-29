# student = {
#     "name" : "Himanshu",
#     "age" : 29,
#     "course" : "python",
#     "passsed" : True,
#     # "subjects" : ("python", "react", "node", "mongodb", "rtk", "express", "nextjs"),
#     # "address" : {
#     #     "pincode" : 281003,
#     #     "house" : "D39",
#     #     "city" : "Mathura",
#     #     "state" : "UP"
#     # }
# }
# student["marks"] = 45
# student["age"] = 56

# # del student["course"]
# # student.pop("age")

# student.clear()

# print ("Students detail: ", student)
# # print(student.get("notexists"))
# # print(student["subjects"])

users = {
    "user1" : {
        "name" : "Himanshu",
        "age" : 28
    },
    "user2" : {
        "name" : "Sumitra",
        "age" : 21
    }
}

print(users["user1"]["name"] + " " + users["user2"]["name"])