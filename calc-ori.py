import csv
# 科目情報のCSV
subpath = ["./csv/science.csv", "./csv/system.csv", "./csv/resource.csv"]
# 自分の履修状況のCSV
userpath = ["./usr/aa.csv", "./usr/ab.csv", "./usr/ac.csv", "./usr/sa.csv", "./usr/sb.csv", "./usr/sc.csv"]
def read_csv(path):
    mylist = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        content = [row for row in reader]
    return content

def cat(lis):
    content = []
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            content.append(lis[i][j])
    return content

def id_cat(mylist):
    res = []
    for i in mylist:
        res = res + i
    return res

def return_id(userpath):
    mylist = []
    for i in userpath:
        mylist.append(cat(read_csv(i)))
    myid = id_cat(mylist)
    return set(myid)

def science(path, mylist):
    content = read_csv(path[0])
    num = 0.0
    for sci in mylist:
        if sci[2] == "6":
            #print(sci)
            for i in content:
                #print(list(i[0]), list(sci))
                if sci == i[0][:-1]:
                    #print(i[2])
                    num = num + float(i[2][:-1])
    return num
def system(path, mylist):
    content = read_csv(path[1])
    num = 0.0
    for sci in mylist:
        if sci[2] == "7":
            for i in content:
                #print(list(i[0]), list(sci))
                if sci == i[0][:-1]:
                    #print(i[2])
                    num = num + float(i[2][:-1])
    return num
def resource(path, mylist):
    content = read_csv(path[2])
    num = 0.0
    for sci in mylist:
        if sci[2] == "8":
            #print(sci)
            for i in content:
                #print(list(i[0]), list(sci))
                if sci == i[0][:-1]:
                    #print(i[2])
                    num = num + float(i[2][:-1])
    return num
mylist = return_id(userpath)
print(mylist)
sci = science(subpath, mylist)
sys = system(subpath, mylist)
res = resource(subpath, mylist)
22
idx = int(input("自分の主専攻に応じて番号を入力してください\n1:知識科学\n2:システム\n3:資源\n"))
print(f"専門科目の合計単位数: {sci + sys + res}")

if idx == 1:
    print(f"他主専攻の単位数：{sys + res}")
    print(f"残り：{8-sys-res}")
if idx == 2:
    print(f"他主専攻の単位数：{sci + res}")
    print(f"残り：{8-sci-res}")
if idx == 3:
    print(f"他主専攻の単位数：{sys + sci}")
    print(f"残り：{8-sys-sci}")