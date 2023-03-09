import random
s=" qwertyuiopasdfghjklzxcvbnm"
print("1-crypt, 2-uncrypt, 3-stop")
b=input()
if b=="1":
    print("Word that you need to crypt")
    key=random.randint(100, 999)
    print("key = ", key)
    a=input()
    code=" "
    for i in range(len(a)):
        k = a[i]
        cod=key*s.find(a[i])
        code+=str(cod)
    print(code)
elif b=="2":
    print("Insert crypt key")
    key=int(input())
    a=input()
    counter=""
    m=""
    for i in range(len(a)):
        counter+=str(a[i])
        if int(counter)%key!=0:
            continue
        elif int(counter)%key==0:
            k=int(counter)//key
            m+=str(s[k])
            counter = ""
    print(m)
else:
    print("no")