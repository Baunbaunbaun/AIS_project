### FUNCTIONS ###

def print_dict(dict):
    for d in dict.items():
        print(d)

def print_lst(lst):
    for d in lst:
        print(d)

def print_queue(q):
        for n in list(q.queue):
                print(n, end=" ")

# convert list of tuples to list of values 
# (Because SQLite returns list of tuples)
def tuples_to_values(tup):
    out = []
    for t in tup:
        out.append(t[0])
    return out

# convert list to tuple 
def lst_to_tuple(lst): 
    if(len(lst)==1):
        return "(" + str(lst[0]) + ")"
    return tuple(lst)

# extract list from list
def lst_minus_lst(lst1,lst2):
    for v in lst2:
        while(True):
            try: 
                lst1.remove(v)
            except:
                break
    # this line is taken from – https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    lst1 = list(dict.fromkeys(lst1))
    return lst1