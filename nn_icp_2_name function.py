def fullname(frst_name, lst_name):
    return (frst_name+" "+lst_name)

def string_alternative(fname):
    lst=[]
    for i in range(len(fname)):
        if(i%2==0):
            lst.append(fname[i])
    return lst

frst_name=input("enter your first name:")
lst_name=input("enter your last name:")

fname=fullname(frst_name,lst_name)
print(fname)
print("".join(string_alternative(fname)))

