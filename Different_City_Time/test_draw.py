import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import pandas as pd

##绘图代码省略，坐标轴设置如下
ax = plt.gca()  # 表明设置图片的各个轴，plt.gcf()表示图片本身
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 横坐标标签显示的日期格式
plt.xticks(pd.date_range('2018-9-1', '2018-11-30', freq='10d'))  # 横坐标日期范围及间隔
plt.yticks(range(20, 110, 10))  # 设置纵坐标，使用range()函数设置起始、结束范围及间隔步长

plt.plot()