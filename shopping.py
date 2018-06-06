# _*_coding:utf-8_*_
# Author:len liu

shop_list = [("iphone",5000),("mac",8000),("bike",600),("coffer",30),("book",80),("water",10)]
salary = input("pls input your salary: ")
buy_list = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for i in shop_list:
            print(shop_list.index(i),i)
        choice = input('pls input your choice:')
        if choice.isdigit():
            choice = int(choice)
            if choice < len(shop_list) and choice >= 0:
                shop_info = shop_list[choice]
                if shop_info[1] <= salary:
                    buy_list.append(shop_info[0])
                    salary -= shop_info[1]
                    print("you add %s to shop cart,your balance is \033[31;1m%s\033[0m" %(shop_info[0],salary))
                else:
                    print("\033[32;1mno enough moneny!your balance is %s\033[0m" %(salary))
            else:
                print("no this product")

        elif choice == "q" :
            print("your shop_list is %s and your balance is %s,thanks for you coming, welcome you next time,bye!"%(buy_list,salary))
            exit(0)
        else:
            print("if you want continue ,pls input 0 to %s,if you want finish buy somthing pls enter 'q' "%(shop_list.index(i)))
else:
    print("pls input digit!")