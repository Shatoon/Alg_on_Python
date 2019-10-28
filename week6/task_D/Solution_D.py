import sys

def num_list():
    while True:
        x = input()
        if x == '#':
            break
        
        if x.isdigit() == True:
            x = int(x)
        else:
            x = list(map(int, x.split())) # Создаем список из полученной строки
            x = x[1:] + x[:1]
            x1 = [str(a) for a in x]
            print(" " . join(x1))
            sys.exit()
            
        L.append(x)
    return L

def mean(L):
    return round(sum(L) / float(len(L)), 3)

def val_4(list_name, size):
     L1 = []
     while len(list_name) > 0:
         pice = list_name[:size]
         L1.append(sum(pice) % pice[len(pice) - 1])
         list_name   = list_name[size:]
     return sum(L1)


L = []

num_list()

print (mean(L), max(L), min(L), val_4(L, 3))
