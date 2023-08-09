# 打好python基础很重要！

# 练习时间：2022/8/12 15:46

# 学生信息管理系统设计
import os.path

filename = "student.txt"
def main():
    while True:
        menu()
        choice =  int(input("请选择"))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("您确定要退出系统吗？y/n")
                if answer =="y" or answer=="Y":
                    print("谢谢您的使用！！")
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def menu():
    print("=====================学生信息管理系统=======================")
    print("----------------------功能菜单----------------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出")
    print("--------------------------------------------------------")

def insert():
    student_list=[] #用于存储录入的学生
    while True: #循环录入
        id=input("请输入ID（如1001）")
        if not id:  #空字符串的bool值为False，前面加not，就是True
            break
        name = input("请输入姓名：")
        if not name:
            break

        try:
            english = int(input("请输入英语成绩"))
            python = int(input("请输入python成绩"))
            java = int(input("请输入java成绩"))
        except:
            print("输入无效，不是整数类型，请重新输入")
            #将录入的学生信息保存到字典中
        student={"id":id,"name":name,"english":english,"python":python,"java":java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input("是否继续添加？y/n\n")
        if answer=="y":
            continue
        else:
            break

    #调用save()函数
    save(student_list)
    print("学生信息录入完毕！！！")
def save(lst):
    try:
        stu_txt=open(filename,"a",encoding = "utf-8")
    except:
        stu_txt=open(filename,"w",encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item)+"\n")
    stu_txt.close()





def search():
    student_query=[]
    while True:
        id=""
        name=""

        if os.path.exists(filename):
            mode=input("按ID查找请输入1，按姓名查找请输入2")
            if mode=="1":
                id=input("请输入学生id:")
            elif mode=="2":
                name=input("请输入学生姓名:")
            else:
                print("指令输入有误，请重新输入！")
                search()
            with open(filename,"r",encoding="utf-8") as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!="":
                        if d["id"]==id:
                            student_query.append(d)
                    elif name!="":
                        if d["name"]==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input("是否继续查询?y/n\n")
            if answer=="y":
                continue
            else:
                break
        else:
            print("未找到学生信息文件")
            return
def show_student(lst):
    if len(lst)==0:
        print("没有查询到学生信息，无数据显示！！")
        return
    #定义标题显示格式
    format_title="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    print(format_title.format("ID","姓名","英语成绩","Python成绩","Java成绩","总成绩"))
    #定义内容的显示格式
    format_data="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    for item in lst:
        print(format_data.format(item.get("id"),item.get("name"),item.get("english"),item.get("python"),item.get("java"),int(item.get("english"))+int(item.get("python"))+int(item.get("java"))))



def delete():
    while True:
        student_id=input("请输入ID（如1001）")
        if student_id!="":
            if os.path.exists(filename):
                with open(filename,"r",encoding="utf-8") as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag = False  #标记是否删除
        if student_old:
            with open(filename,"w",encoding="utf-8") as w_file:
                d = {}
                for i in student_old:
                    d = dict(eval(i) )
                    if d["id"]!=student_id:
                        w_file.write(str(d)+"\n")
                    else:
                        flag =  True  #表示已删除
                if flag:
                    print("id为{}的学生信息已删除".format(student_id))
                else:
                    print("没有找到id为{}的学生信息".format(student_id))
        else:
            print("无学生信息")
            break
        show()
        answer=input("是否继续删除？y/n\n")
        if answer=="y":
            continue
        else:
            break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
            student_old=rfile.readlines()
    else:
        print("学生信息文件不存在")
        return
    student_id=input("请输入要修改的学生id:")
    with open(filename,"w",encoding="utf-8") as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d["id"]==student_id:
                print("找到学生信息，可以修改当前学生信息了！")
                while True:
                    try:
                        d["name"]=input("请输入姓名:")
                        d["english"]=input("请输入英语成绩:")
                        d["python"]=input("请输入python成绩:")
                        d["java"]=input("请输入java成绩:")
                    except:
                        print("当前输入有误，请重新输入!!!")
                    else:
                        break
                wfile.write(str(d)+"\n")
                print("学生id为{}的信息修改成功！".format(student_id))
            else:
                wfile.write(str(d)+"\n")
        answer=input("是否继续修改其他学生信息？y/n\n")
        if answer=="y":
            modify()

def sort():
    show()
    if os.path.exists(filename):

        with open(filename,"r",encoding="utf-8") as rfile:
           lst= rfile.readlines()
        student_list = []
        for i in lst:
            student_list.append(dict(eval(i)))
        mode=input("请选择(0.升序 1.降序):")
        if mode=="0":
            flag=False
        elif mode=="1":
            flag=True
        else:
            print("您的输入有误，亲重新输入！")
            sort()
        way=input("请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序):")
        if way=="1":
            student_list.sort(key=lambda x:int(x["english"]),reverse=flag)
        elif way=="2":
            student_list.sort(key=lambda x:int(x["python"]),reverse=flag)
        elif way=="3":
            student_list.sort(key=lambda x:int(x["java"]),reverse=flag)
        elif way=="0":
            student_list.sort(key=lambda x:int(x["english"])+int(x["python"])+int(x["java"]),reverse=flag)
        else:
            print("您的输入有误，请重新输入！！")
            sort()
        show_student(student_list)

    else:
        return
def total():
       if os.path.exists(filename):
           with open(filename,"r",encoding="utf-8") as rfile:
               all_student=rfile.readlines()
               if not all_student:
                   print("还未录入学生信息")
               else:
                   print("一共有{}名学生".format(len(all_student)))

       else:
           print("暂未保存数据信息")

def show():
    student_list=[]  #存储学员信息
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
           lst=rfile.readlines()
        for i in lst:
            student_list.append( dict(eval(i)))
        if student_list:
            show_student(student_list)
    else:
        print("暂未保存数据信息")

if __name__ =="__main__":
    main()