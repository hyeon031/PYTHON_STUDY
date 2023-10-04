# =============================================================================
# jason 으로 저장 
# =============================================================================

def test1():
    import json
    
    item_list = []
    for i in range(1,6):
        dic = {}
        dic["name"] = f"홍길동{i}"
        dic["age"] = 19 + i
        item_list.append(dic)
    print(item_list)
    
    with open("person.json","w", encoding="utf8") as f:
        json.dump(item_list, f, ensure_ascii=False)
        
# test1()

# =============================================================================
# json 으로 읽기 
# =============================================================================

def test2():
    import json
    
    item_list = []
    with open("person.json","r",encoding="utf8") as f:
        item_list = json.load(f)
    
    print(item_list)
    for item in item_list:
        # print(item)
        # for v in item_keys():
        # for v in item.values():
        for k, v in item.items():
            print(k, v)
        print("------------")
test2()
