import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

def write_in_mongoDB(House_list, keyword, price_1, price_2):

    city = keyword + "房价区间"
    db = client[city]
    string = keyword + "房价位于[" + price_1 + ',' + price_2 + ']'
    collection = db[string]
    flag_1 = 0
    flag_2 = 0
    for house in House_list:
        flag_1 = flag_1 + 1
        if collection.insert_one(house):
            flag_2 = flag_2 + 1
    print('House list saved to Mongo')
    print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

