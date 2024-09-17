lst1 = [int(i) for i in input().split()]

def get_rec_sum(lst):
    head, *tail = lst
    return head + get_rec_sum(tail) if tail else head

print(get_rec_sum(lst1))