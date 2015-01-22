#json 模块常用函数整理

    >>> import json

###json.dumps()
Python 转换为 Json

![](/static/img/json_dumps.png)

json.dumps() 常用可选参数介绍：

* `indent` 缩进，即在输出 json 格式数据时添加缩进，以便阅读。有效取值为非负整数
* `separators` 元组 (tuple) 类型，默认值为 `(', ', ': ')` （注意空格）
* `encoding` 字符串编码，默认为 UTF-8
* `sort_keys` 默认为 False，当设置为 True 时，那么字典将以其 key 值进行排序后输出。

```
>>> dict_data = {'Plant':[{'species':'tree','age':100},{'species':'grass','age':0.5}], 'Animal':[{'species':'cat','age':1},{'species':'dog','age':2}]}
>>> print json.dumps(dict_data)
{"Plant": [{"age": 100, "species": "tree"}, {"age": 0.5, "species": "grass"}], "Animal": [{"age": 1, "species": "cat"}, {"age": 2, "species": "dog"}]}

>>> print json.dumps(dict_data, separators=(',',':'))
{"Plant":[{"age":100,"species":"tree"},{"age":0.5,"species":"grass"}],"Animal":[{"age":1,"species":"cat"},{"age":2,"species":"dog"}]}

>>> print json.dumps(dict_data, sort_keys=True)
{"Animal": [{"age": 1, "species": "cat"}, {"age": 2, "species": "dog"}], "Plant": [{"age": 100, "species": "tree"}, {"age": 0.5, "species": "grass"}]}

>>> print json.dumps(dict_data, indent=4)
{
    "Plant": [
        {
            "age": 100,
            "species": "tree"
        },
        {
            "age": 0.5,
            "species": "grass"
        }
    ],
    "Animal": [
        {
            "age": 1,
            "species": "cat"
        },
        {
            "age": 2,
            "species": "dog"
        }
    ]
}
```

###json.loads()
Json 转换为 Python

![](/static/img/json_loads.png)

    >>> json_data = json.dumps(dict_data)
    >>> dict_data = json.loads(json_data)
    >>> print dict_data
    {u'Plant': [{u'age': 100, u'species': u'tree'}, {u'age': 0.5, u'species': u'grass'}], u'Animal': [{u'age': 1, u'species': u'cat'}, {u'age': 2, u'species': u'dog'}]}

###参考
[https://docs.python.org/2/library/json.html](https://docs.python.org/2/library/json.html)