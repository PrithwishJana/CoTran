import json

with open("io_testcases_codejam-valid.json", 'r') as j:
    jsonDict_valid = json.loads(j.read())
with open("io_testcases_codejam-test.json", 'r') as j:
    jsonDict_test = json.loads(j.read())
with open("io_testcases_codejam-train.json", 'r') as j:
    jsonDict_train = json.loads(j.read())

merged_dict = {key: value for (key, value) in (list(jsonDict_valid.items()) +\
                                                 list(jsonDict_test.items()) +\
                                                 list(jsonDict_train.items()))}

with open("io_testcases_codejam.json", 'w') as fp:
    json.dump(merged_dict, fp, indent=4)