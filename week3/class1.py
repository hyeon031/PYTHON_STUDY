def test1():
    f=open("dream.txt","r")
    contents = f.read()
    print(contents)
    f.close()
# test1()


def test2():
    with open("dream.txt", "r") as f:
        contents_list = f.readlines()
        print(contents_list)
        
        for item in contents_list:
            print(item, end = "")
            
# test2()


def test3():
    import csv
    seung_nam_data =[]
    header = []
    rownum =1
    
    with open("korea_floating_population_data.csv","r",encoding = "cp949") as r_file:
        csv_data = csv.reader(r_file)
        for row in csv_data:
            if rownum == 1:
                header = row
            location = row[7]
            if location.find("성남시") != -1:
                seung_nam_data.append(row)
                rownum += 1 
    # print(seung_nam_data)
    with open("seung_nam_data.csv","w",encoding = "utf-8") as s_file:
        writer = csv.writer(s_file, delimiter = "\t" ,quotechar = '"', quoting=csv.QUOTE_NONE)
        writer.writerow(row)
        for row in seung_nam_data:
            writer.writerow(row)
# test3()


def test4():
    import csv
    item_list = []
    header = ["name",'age']
    for i in range(1,6):
        item ={}
        item['name'] = f"홍길동{i}"
        item['age'] = 20+i
        item_list.append(item)
        
    with open("test.csv","w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quotechar='"', quoting = csv.QUOTE_NONNUMERIC)
        writer.writerow(header)
        for item in item_list:
            #row = ['홍길동1', 21]
            row = [item["name"], item["age"]]
            writer.writerow(row)
# test4()

def test5():
    import csv
    
    item_list = []
    header = []
    with open("test.csv",encoding="utf-8") as f:
        reader = csv.reader(f, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_NONNUMERIC)
        row =1
        for item in reader:
            if row == 1:
                header = item
            else:
                dic = {}
                dic[header[0]] = item[0]
                dic[header[1]] = item[1]
                item_list.append(dic)
                
            row+=1
            
    print(item_list)
    
test5()
