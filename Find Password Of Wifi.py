import subprocess
x=subprocess.check_output(["netsh","wlan","show","profiles"])
x=x.splitlines()
t=list()
for i in x:
    t.append(i.decode().split(":"))
while(1):
    try:
      t.remove([''])
    except:
        break
name=list()
for i in range(6,len(t)):
    name.append(t[i][1][1:])

print("\n\033[1;32m--------Saved Wifi----------\n")    
for Name in name:
    try:
        password=subprocess.check_output(["netsh","wlan","show","profile",f"{Name}","key=clear"])
        password=password.decode()
        password=password.split("\n")
        for i in password:
            if "Key Content" in i:
                print(f"\033[1;36m{Name} : \033[1;31m{i[29:]}")
    except:
        break
print("\033[0m")