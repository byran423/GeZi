import json,requests
from lesson4.base import BaseObj




def to_dict(obj):
	try:
		return obj.__dict__
	except Exception as e:
		return obj


def obj_to_json(obj):
	""" """
	return json.dumps(obj, default=to_dict)


def to_obj(j):
	try:
		return BaseObj(**j)
	except Exception as e:
		return j


def json_to_obj(j):
	""" """
	return json.loads(json.dumps(j), object_hook=to_obj)


def print_json(j):
	print(json.dumps(j,
					 indent=4,
					 ensure_ascii=False))





