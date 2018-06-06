# _*_coding:utf-8_*_
# Author:len liu
# _*_coding:utf-8_*_
# Author:len liu
name = ["zs","ls",["xxx","yyy","zzz"],"we","mz"]
#name.insert(1,"xx")
#name[1] = "hh"
#name2 = ["zz","yy","xx"]
#del name[1]
#name.remove("we")
#name.pop(0)
#print(name.index("ls"))
#name.append("ls")
#print(name.count("ls"))
#name.extend(name2)
#name.insert(2,name2)
#name[1] = "oo"
name3 = name.copy()
#name[2] = ["a","b","c"]
name[0] = "ZS"
name[2][0] = "B"
print(name)
print(name3)

#print(name[name.index("hh")])