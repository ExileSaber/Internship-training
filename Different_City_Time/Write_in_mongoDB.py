import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

def write_in_mongoDB(Time_list, keyword):

    city = keyword + "房价时间分布"
    db = client[city]
    string = 'two_year'
    collection = db[string]
    flag_1 = 0
    flag_2 = 0
    for time in Time_list:
        flag_1 = flag_1 + 1
        if collection.insert_one(time):
            flag_2 = flag_2 + 1
    print('Time list saved to Mongo')
    print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

