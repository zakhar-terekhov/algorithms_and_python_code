from collections import defaultdict,OrderedDict


plain = {"a": 1, "b": 2, "c": 3}
fancy = OrderedDict([("a",1),("b",2),("c",3)])
dict_of_list = defaultdict(list)
dict_of_list["a"].append("something")
