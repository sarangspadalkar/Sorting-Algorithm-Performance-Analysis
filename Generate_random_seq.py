import random
rand_seq=[]
def gen_random_input(str,size):
    rand=[random.randint(0,1000) for i in range(size)]
    if str == 'best':
        return sorted(rand)
    elif str == 'worst':
        return sorted(rand,reverse=True)
    else:
        return rand
