#coding=utf-8
import random
import configparser
import sys
import os
os.system("chcp 65001")
###################################################
def mainblock():
    global d,lines,m,mlines,strike,maxstrike,dictname
    num_all=num_correct=0
    if MODE=="1":#中译英
        print("======中译英======\n")
        count=flag
        for line in lines[flag:]:
            flagwrite(count)
            cf.read("config.conf")
            s=line.find(";")
            print(line[s+1:])
            INPUT=input("请输入英文：")
            if INPUT=="MODE":
                break
            if INPUT==line[:s]:
                strike+=1
                maxstrike=max(maxstrike,strike)
                num_all+=1
                num_correct+=1
                print("正确 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                print("已经完成了^^^"+str(strike)+"连击！^^^最高连击数："+str(maxstrike))
            else:
                strike=0
                num_all+=1
                if line not in mlines:
                    m.write(line)
                    m.flush()
                    mr.flush()
                    mlines=mr.readlines()
                print("错误！ 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                while INPUT!=line[:s]:
                    print(line)
                    INPUT=input("请再试一次：")
                    if INPUT=="MODE":
                        break
                if INPUT=="MODE":
                    break
            print("-----------------------------------")
            count+=1
    elif MODE=="2":#英译中
        print("======英译中======\n")
        count=flag
        for line in lines[flag:]:
            flagwrite(count)
            s=line.find(";")
            print(line[:s])
            INPUT=input("请输入中文：")
            if INPUT=="MODE":
                break
            if INPUT in line[s+1:]:
                strike+=1
                maxstrike=max(maxstrike,strike)
                num_all+=1
                num_correct+=1
                print(line[s+1:-1]+";"+line[:s])
                print("正确 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                print("已经完成了^^^"+str(strike)+" 连击！^^^最高连击数："+str(maxstrike))
            else:
                strike=0
                num_all+=1
                if line not in mlines:
                    m.write(line)
                    m.flush()
                    mr.flush()
                    mlines=mr.readlines()
                print("不正确！ 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                while INPUT not in line[s+1:]:
                    print(line[s+1:-1]+";"+line[:s])
                    INPUT=input("请再试一次：")
                    if INPUT=="MODE":
                        break
                if INPUT=="MODE":
                    break
            print("-----------------------------------")
            count+=1
    elif MODE=="3":
        print("======错词本======\n")
        for mline in mlines:
            if random.random()<=0.5:#中译英
                s=mline.find(";")
                print(mline[s+1:])
                INPUT=input("请输入英文：")
                if INPUT=="MODE":
                    break
                if INPUT==mline[:s]:
                    num_all+=1
                    num_correct+=1
                    print("正确 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                else:
                    num_all+=1
                    print("错误！ 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                    while INPUT!=mline[:s]:
                        print(mline)
                        INPUT=input("请再试一次：")
                        if INPUT=="MODE":
                            break
                    if INPUT=="MODE":
                        break
                print("-----------------------------------")
            else:#英译中
                s=mline.find(";")
                print(mline[:s])
                INPUT=input("请输入中文：")
                if INPUT=="MODE":
                    break
                if INPUT in mline[s+1:]:
                    num_all+=1
                    num_correct+=1
                    print(mline[s+1:-1]+";"+mline[:s])
                    print("正确 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                else:
                    num_all+=1
                    print("不正确！ 正确率："+str(num_correct)+r"/"+str(num_all)+" "+str(num_correct/num_all*100)+r"%")
                    while INPUT not in mline[s+1:]:
                        print(mline[s+1:-1]+";"+mline[:s])
                        INPUT=input("请再试一次：")
                        if INPUT=="MODE":
                            break
                    if INPUT=="MODE":
                        break
                print("-----------------------------------")
    elif MODE=="4":
        m.close()
        mr.flush()
        m=open("mistakes.txt","w",encoding='utf-8')
        m.write("")
        m.close()
        m=open("mistakes.txt","a+",encoding='utf-8')
        mlines=m.readlines()
    elif MODE=="5":
        dictname_old=dictname
        print("当前字典为："+dictname_old)
        dictname=input("请输入新字典文件名称，留空则不变：")
        if dictname=="":
            dictname=dictname_old
            return
        elif not dictname[-4:]==".txt":
            print("\n居然不是txt文件\n兄弟你这样搞是会出事情的")
            return
        elif dictname=="buffer.txt" or dictname=="mistakes.txt":
            print("\n哇你为啥要拿我的文件当字典？！")
            return
        d.close()
        try:
            d=open(dictname,"r",encoding= 'utf-8')
            cf.read("config.conf")
            print("try")
            cf.set("d","dictname",dictname)
            with open("config.conf","w") as f:
                cf.write(f)
        except:
            dictname=dictname_old
            d=open(dictname,"r",encoding= 'utf-8')
            print("\nFNNDP,根本就找不到这个屌字典")
        lines=d.readlines()
    else:
        print("\n模式错误啊兄弟")
###################################################
def flagwrite(flagging):
    cf.read("config.conf")
    cf.set("d","flag",str(flagging))
    with open("config.conf","w") as f:
        cf.write(f)
###################################################
def sizewrite(sizing):
    cf.read("config.conf")
    cf.set("d","size",str(size))
    with open("config.conf","w") as f:
        cf.write(f)
###################################################
while True:
    print("\n欢迎使用傻瓜单词机")
    print("可在软件根目录下添加字典文件")
    print("输入“MODE”可以返回模式选择菜单")
    try:
        cf=configparser.ConfigParser()
        cf.read("config.conf")
        strike=maxstrike=0
        dictname=cf.get("d","dictname")
        d=open(dictname,"r",encoding= 'utf-8')
        m=open("mistakes.txt","a+",encoding='utf-8')
        mr=open("mistakes.txt","r",encoding='utf-8')
        mlines=mr.readlines()
        size=cf.getint("d","size")
        flag=cf.getint("d","flag")
        if flag:
            INPUT=input("\n上次似乎没背完，背了"+str(flag)+"个，还剩"+str(size-flag)+"个，是否继续？[Y/n]:")
            if INPUT=='n' or INPUT=='N':
                pass
            else:
                if not (INPUT=='y' or INPUT=='Y' or INPUT==""):
                    print("\n不对应该输入y或n你个二货\n就当你要继续吧O_o\n")
                b=open("buffer.txt","r",encoding='utf-8')
                lines=b.readlines()
                MODE=cf.get("d","mode")
                mainblock()
                b.close()
        lines=d.readlines()
###################################################
        while True:
            flag=0
            flagwrite(0)
            size=len(lines)
            sizewrite(size)
            print("\n词库："+str(size)+",错词："+str(len(mlines)))
            MODE=input("请输入模式（1为中译英，2为英译中,3为错词本，4为清空错词，5为选择字典）：")
            cf.read("config.conf")
            cf.set("d","mode",str(MODE))
            with open("config.conf","w") as f:
                cf.write(f)
            random.shuffle(lines)
            b=open("buffer.txt","w",encoding='utf-8')
            b.writelines(lines)
            b.close()
            mainblock()
    except:
        info=sys.exc_info()
        print("\nBOOOOOOOOOOOOOOOM!!!!!!!!!!!!!\n")
        print("哇你搞出了一个bug耶！好像错误原因是：")
        print(info)
        input()