import Spider_city_allow
import Spider_by_price
import time
import Write_in_mongoDB

print('搜集初始数据,leading.......')
time.sleep(2)

url = 'https://bj.5i5j.com/'
City = Spider_city_allow.spider_city_allow(url)

print("搜集完成")
city = input("输入你要查询的城市：")

keys = list(City.keys())

if city in keys:
    price_1 = input("输入最低价（万）：")
    price_2 = input("输入最高价（万）：")
    number = int(input("输入你需要查看的房子数量:"))
    url_city = City[city]
    House_list = Spider_by_price.spider_by_price(url_city, price_1, price_2, number)

    save = input("是否存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(House_list, city, price_1, price_2)

else:
    print("你输入的城市我爱我家网中没有，暂无其他网站可以进行操作")
