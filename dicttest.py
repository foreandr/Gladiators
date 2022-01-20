import json
def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    return str

def binary_to_dict(the_binary):
    d = json.loads(the_binary)
    return d

my_dict = {'key' : [255,255,255]}

bin = dict_to_binary(my_dict)
print(bin[0])
print(type(bin))

dct = binary_to_dict(bin)
print(dct)