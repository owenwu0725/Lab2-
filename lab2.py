table=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","stastic","struct","switch","typedef","union","unsigned","void","volatile","while"]


# number total keywords
def get_key(infile):
    global count
    count = 0
    for line in infile.readlines():    # 对每行元素操作
        line = line.strip()         # 将每行字符串的头尾空行符去除
        line = line.replace(",", " ").replace(".", " ").replace("{", " ").replace("}", " ").replace(":", " ").replace(";", " ").replace("?", " ").replace("(", " ").replace(")", " ").replace("!", " ").replace(">"," ").replace("<", " ").replace("=", " ")
        words = line.split()    # 将每行按空格划分为单词，做成单词列表
        for word in words:
            for keyword in table:
                if word == keyword:
                    count = count+1
    return count


# number switch&case
def get_switch(infile):
    global count_2, count_3
    count_2 = 0
    count_3 = 0
    flag=0
    cable=[]
    for line in infile.readlines():  # 对每行元素操作
        line = line.strip()  # 将每行字符串的头尾空行符去除
        line = line.replace(",", " ").replace(".", " ").replace("{", " ").replace("}", " ").replace(":", " ").replace(";", " ").replace("?", " ").replace("(", " ").replace(")", " ").replace("!", " ").replace(">", " ").replace("<", " ").replace("=", " ")
        words = line.split()  # 将每行按空格划分为单词，做成单词列表
        for word in words:
            if word == "switch":
                count_2 = count_2+1
                flag=1    # 有一个switch前提
            elif word == "case" and flag == 1:
                count_3 = count_3+1
            elif word=="default":
                cable.append(count_3)
                count_3 = 0
                flag = 0
    print("switch num: %d" % count_2)
    print("case num:")
    length=len(cable)
    index = 0
    while index < length:
        print(cable[index])
        print(" ")
        index += 1


# function mode selection
def file_mode(path, mode):
    infile = open(path,"r")
    if mode == 1:
        total=get_key(infile)
        print("total num: %d" % total)

    elif mode == 2:
        total = get_key(infile)
        print("total num: %d" % total)
        get_switch(infile)

    infile.close()
    return 0


# main function
def main():
    mode=input("please select the mode from 1 to 4:")
    path_find=input("please input the test file path:")    # path for my computer is 'D:\Python\code file.txt'
    mode_num=int(mode)
    file_mode(path_find, mode_num)


main()


