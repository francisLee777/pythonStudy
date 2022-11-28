# 基本语法

# 字符串
str = """123
456"""

print(str, "\n name:%s, age:%d" % ("haoyu", 25))

# 列表
list1 = [1, "hello", (4, 5), {"a": 4}]
list1.append(5.51)
list1.insert(2, "insert1")
list1.pop(2)
# list1.sort()
list1.reverse()
list1.reverse()
list1 = list1[:len(list1) - 1]
print("定位方法: ", list1.index((4, 5)), "计数：", list1.count(9.9))

# 统一遍历方法
for index, item in enumerate(list1):
    print(index, item, type(item))


# tuple   元组， 不可更改
tuple = ('runoob', 786, 2.23, 'john', 70.2)

# map 字典
dic = {"1": "Beijing", "2": "Shanghai", "3": "Chengdu"}
del (dic["2"])
for key in dic:
    print("key:", key, "value", dic[key])
print(type(dic.keys()), dic.values())
