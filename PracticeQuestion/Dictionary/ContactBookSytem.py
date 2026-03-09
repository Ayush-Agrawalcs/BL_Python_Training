dict={"Ayush":"8393872897","Rahul":"9045735010","Vikash":"8439645109"}

def addContact(dict):
    key=input()
    value=input()
    dict[key]=value

def SearchContact(dict):
    key=input()
    if key in dict:
        print("True")
    else:
        print("false")

def deletecontact(dict):
    key=input()
    dict.pop(key)
    print(dict)

deletecontact(dict)
# addContact(dict)
SearchContact(dict)





