

list = [1, 3 ,6, 9, 12]
def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)


    return res


r = get_filter(list, lambda x: x )
print(r)