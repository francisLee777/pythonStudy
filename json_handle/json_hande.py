import json

# json 处理

# json.dumps() python 对象转 json 对象     json.load() 相反

dict_data = {"a": 1, "b": 2}

dump_data = json.dumps(dict_data)   # 输出字符串
load_data = json.loads(dump_data)  # 输入字符串,  str() 方法会把字典的key转成单引号

# 打印转换结果
print(type(dict_data), dict_data)
print(type(dump_data), dump_data)
print(type(load_data), load_data)

dump_data = """{
    "animals": {
        "dog": [
            {
                "name": "Rufus",
                "age":15
            },
            {
                "name": "Marty",
                "age": null
            }
        ]
    }
}"""

load_data = json.loads(dump_data)
data = load_data.get("animals").get("dog")
result1 = []
for item in data:
    result1.append(item.get("age"))
print(result1)
