def get_data_fig(*args, **kwargs):
    d = ['type', 'color', 'closed', 'width']
    c = []
    for i in d:
        if i in kwargs:
            c.append(kwargs[i])

    return (sum(args),) + tuple(c)

#-----------------------------------------

def get_data_fig1(*args, **kwargs):
    d = ['type', 'color', 'closed', 'width']
    c = []
    for i in d:
        if i in kwargs:
            c.append(kwargs[i])

    return (sum(args),) + tuple(c)
