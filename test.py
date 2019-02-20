from collections import OrderedDict

a = [{'name':'zhangsan', 'score': 20}, {'name':'lisi', 'score':25}, {'name':'zhangsan', 'score':30}]
b = OrderedDict()

for item in a:
	b.setdefault(item['name'], {**item})

print(list(b.values()))