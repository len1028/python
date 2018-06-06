# _*_coding:utf-8_*_
# Author:len liu
shop_list = [
("iphone",5000),
("mac",8000),
("coffer",50),
("bike",500),
("book",100),
("cake",80),
]
buy_list = []
saraly = input("pls input your saraly:")

if saraly.isdigit():
    saraly = int(saraly)
    while True:
        for i in shop_list:
            print(shop_list.index(i),i)
        choice = input("pls input your choice:")
        if choice.isdigit():
            choice = int(choice)
            if choice < len(shop_list) and choice >= 0:
                p_info = shop_list[choice]
                print(p_info[1])
                if p_info[1] <= saraly:
                    buy_list.append(p_info[0])
                    saraly -= p_info[1]
                    print("you got %s , your balance is %s"%(p_info[0],saraly))
                else:
                    print("you not enough moneny! show your buylist %s and your balance is %s!"%(buy_list,saraly))
            else:print("no this product")
        elif choice == 'q':
            print("show your buylist %s and your balance is %s!" % (buy_list, saraly))

            exit()
        else:
            print("invaid option,if want complete buy anything pls enter 'q'")





