try:
    raise Exception('span', 'eggss')
except Exception as a:
    print(a)
    print(type(a))