#password vs username
import ast
import requests
import json
r = requests.get('https://sheetdb.io/api/v1/z6r0yt1t1fw4x', auth=('**AUTH CODE**', ''))
json_str = json.dumps(r.json())
data=ast.literal_eval(json_str)
username=[]
password=[]
for i in range (len(data)):
    username.append(data[i]['username'])
    password.append(data[i]['password'])
login="yes"
while login=="yes":
    r = requests.get('https://sheetdb.io/api/v1/z6r0yt1t1fw4x', auth=('**AUTH CODE**', ''))
    json_str = json.dumps(r.json())
    data=ast.literal_eval(json_str)
    username=[]
    password=[]
    for i in range (len(data)):
        username.append(data[i]['username'])
        password.append(data[i]['password'])
    inp=input("Do you have an account? (yes/no): ")
    if inp=="no":
        print("----REGISTRATION WINDOW----")
        name=input("Enter a username: ")
        while name in username:
            name=input("Username already exists. Enter a new username: ")
        pwd=input("Enter a password: ")
        new_data=[{'password':pwd,'username':name}]
        requests.post('https://sheetdb.io/api/v1/z6r0yt1t1fw4x', json=new_data)
        authorisation=1
    elif inp=="yes":
        name=input("Enter your username: ")
        pwd=input("Enter your password: ")
        if (name in username) and (pwd in password):
            for j in range(len(username)):
                if name==username[j]:
                    key_name=j
            if pwd==password[key_name]:
                authorisation=1
            else:
                print("The username and password don't match!")
                authorisation=0
        else:
            print("The username or password does not exist")
            authorisation=0
    if authorisation:
        print("Welcome",name)
        usr=open("./log/username.txt","w")
        usr.write(str(username))
        usr.close()
        psd=open("./log/password.txt","w")
        psd.write(str(password))
        psd.close()
        login=input("Do you wish to logout? (yes/no) ")
    else:
        print("Please register.")
        login="yes"