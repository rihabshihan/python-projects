# 3. Consider the following array
# [{id:1, name:"rajesh"}, {id:2, name: "rahul"}, {id:3, name: "sruthi"}]
# Write a program to accept a number and print the name of the student with that id

array=[{'id':1,'name':"Rajesh"},{'id':2,'name':"Rahul"},{'id':3,'name':"Sruthi"}]

def find_id(array,id_num):
    for i in array:
        if i['id']==id_num:
            print("Name of the student with ID",id_num, "is :", i['name'])
            break
    else:
        print("Student not in the above list")
        
id_num=int(input("Enter the id number"))  
find_id(array,id_num)
