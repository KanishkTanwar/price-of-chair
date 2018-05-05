import os


DEBUG = True
ADMINS = frozenset([os.environ.get("ADMINS")])

'''frozen set is a set that cannot change'''
