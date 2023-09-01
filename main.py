
def nepovezani(ime, pojam):
    global matrica

    x = stalni_pojmovi.index(ime)
    print("x: ", x)
    if(pojam in matrica[x]):
        matrica[x].remove(pojam)
        print(matrica)
        return
    pomocni_pojmovi = []
    for i in range(len(pojmovi)):
        pomocni_pojmovi.append(pojmovi[i].copy())
    for i in range(len(pomocni_pojmovi)):
        print(pojam, pomocni_pojmovi[i])
        if(pojam in pomocni_pojmovi[i]):
            pomocni_pojmovi[i].remove(pojam)
            matrica[x].extend(pomocni_pojmovi[i])
            print(matrica)
            return

def brojPojmova(i, j):
    global matrica
    global pojmovi
    br = matrica[i].count(matrica[i][j])
    print("br: ", br)
    return br

def proveraElemenata():
    global matrica
    global pojmovi
    print("Matrica: ", matrica)
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            print("Matrica, pojmovi: ", matrica[i][j], pojmovi[i])
            if(matrica[i][j] in pojmovi[i] and brojPojmova(i, j) == 1):
                x = matrica[i][j]
                for i in range(len(matrica)):
                    if(x in matrica[i] and len(matrica[i]) > 1):
                        matrica[i].remove(x)

def minusCase(pojam):
    global matrica
    br = 0
    index = 0
    for i in range(len(matrica)):
        if(pojam in matrica[i]):
            br += 1
            index = i

    if(br == 1):
        matrica[index] = [pojam]
        return

def povezani(ime, pojam):
    global matrica
    x = stalni_pojmovi.index(ime)
    matrica[x] = [pojam]



def plusCase(pojam, i):
    for j in range(len(matrica)):
        if(j == i): continue
        if(pojam in matrica[j]):
            matrica[j].remove(pojam)

def plus(pojmovi, odnosi):
    global matrica
    for i in range(len(odnosi)):
        for j in range(len(odnosi[i])):
            if odnosi[i][2] == "povezani":
                matrica[i][j] = 1

# region unos podataka


def unos():
    global stalni_pojmovi
    global pojmovi
    global odnosi
    global matrica
    print("╭─────────────────────────────────────────╮")
    print("│     Unesite broj grupa pojmova (M):     │")
    print("╰─────────────────────────────────────────╯")
    print("-> ", end='')

    M = input().strip()
    if(M.isnumeric()): M = (int)(M)
    else:
        print("Uneli ste pogresan format za broj grupa pojmova.")
        return

    print("╭─────────────────────────────────────────╮")
    print("│ Unesite broj pojmova u jednoj grupi (N):│")
    print("╰─────────────────────────────────────────╯")
    print("-> ", end='')

    N = input().strip()
    if (N.isnumeric()):
        N = (int)(N)
    else:
        print("Uneli ste pogresan format za broj pojmova u jednoj grupi.")
        return

    for i in range(M):
        matrica.append([])

    pojmovi = []
    i = 0
    while i < M:
        print("Unesite pojmove u grupi {} (odvojene zarezom):".format(i+1))
        print("-> ", end='')
        grupa = input().strip().split(',')
        if len(grupa) != N:
            print("Broj pojmova u grupi {} nije jednak {}".format(i+1, N))
            i -= 1
        else: pojmovi.append(grupa)
        i += 1

    stalni_pojmovi = pojmovi[0]
    odnosi = []
    brojac = 0
    while True:
        print("({}) Unesite odnos između pojmova u formatu 'pojam1 + pojam2' ili 'pojam1 - pojam2': ".format(brojac+1))
        print("->", end='')
        unos = input().strip()
        brojac += 1
        if not unos:
            break
        reci = unos.split()
        if len(reci) != 3 or reci[1] not in ['+', '-']:
            print("Pogrešan format unosa. Pokušajte ponovo.")
            brojac -= 1
            continue
        string1 = reci[0]
        string2 = reci[2]
        if(reci[1] == '+'):
            povezani(reci[0], reci[2])
            string3 = "povezani"
        else:
            nepovezani(reci[0], reci[2])
            minusCase(reci[2])
            string3 = "nepovezani"
        odnosi.append([string1, string2, string3])
        print("Usao si u provera elementa")
        proveraElemenata()

    return M, N, pojmovi, odnosi
# endregion



class Node:
    def __init__(self, dubina, potomci=None):
        self.dubina = dubina
        if potomci is None:
            self.potomci = []
        else:
            self.potomci = potomci

class StabloIgaraCvor:
    def __init__(self, stanje, vrednost=None, deca=None, left = None, right = None):
        self.stanje = stanje
        self.left = left
        self.right = right
        self.vrednost = vrednost
        self.children = deca if deca is not None else []

    def add_child(self, child):
        self.children.append(child)

    def add_left(self, child):
        self.left = child

    def add_right(self, child):
        self.right = child
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.insert(0, item)

    def delete(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def levelOrder(root):
    next = root

    if next is None:
        return

    q = Queue()
    q.insert(next)

    while not q.is_empty():
        next = q.delete()
        print(next.dubina, end=' ')

        if next.left is not None:
            q.insert(next.left)

        if next.right is not None:
            q.insert(next.right)


def levelOrderIspis(root):
    if root is None:
        return

    queue = Queue()
    queue.insert((root, 0, None))

    while not queue.is_empty():
        next_cvor, dubina, roditelj = queue.delete()
        roditelj_info = " (Otac: {})".format(roditelj.stanje) if roditelj else " (Koren)"
        print("Dubina {}: {}{}".format(dubina, next_cvor.stanje, roditelj_info))

        if next_cvor.left is not None:
            queue.insert((next_cvor.left, dubina + 1, next_cvor))

        if next_cvor.right is not None:
            queue.insert((next_cvor.right, dubina + 1, next_cvor))

def kreirajStablo(root_stanje, max_dubina):
    root = StabloIgaraCvor(root_stanje)
    nodes = [(root, 0)]

    while nodes:
        node, dubina = nodes.pop(0)

        if dubina < max_dubina:
            sinStanje = generisiStanjeDeteta(node.stanje)
            if len(sinStanje) >= 1:
                left_child = StabloIgaraCvor(sinStanje[0])
                node.add_left(left_child)
                nodes.append((left_child, dubina + 1))

            if len(sinStanje) >= 2:
                right_child = StabloIgaraCvor(sinStanje[1])
                node.add_right(right_child)
                nodes.append((right_child, dubina + 1))

    return root


def generisiStanjeDeteta(stanje):
    brojevi = []
    for i in range(1, stanje + 1):
        if stanje % i == 0:
            brojevi.append(i)
    return brojevi[:2]

# region meni opcije

def zavrsetakIgre():
    print("╭─────────────────────────────────╮")
    print("│  Cestitamo! Zavrsili ste igru!  │")
    print("╰─────────────────────────────────╯")
    izlazakIzIgre()

def izlazakIzIgre():
    print("╭───────────────────────────────╮")
    print("│       Zavrsili ste igru.      │")
    print("╰───────────────────────────────╯")
    quit()
def ispisPocetnogStanjaStabla():
    pass

def uparivanje():
    pass

def ispravnostUnetihPojmova():
    pass

def dobarPut():
    pass

def pomoc():
    pass

def nemaResenja():
    pass

#endregion

#region meni
def pocetniMeni():
    global M
    global N
    global pojmovi
    global odnosi
    global matrica
    global stalni_pojmovi

    print("╭───────────────────────────────────╮")
    print("│               MENI                │")
    print("├───────────────────────────────────┤")
    print("│  0. Izadji                        │")
    print("├───────────────────────────────────┤")
    print("│  1. Igraj igru                    │")
    print("╰───────────────────────────────────╯")

    print("-> ", end='')
    redni_br = input()

    if redni_br == "0":
        izlazakIzIgre()
    elif redni_br == "1":
        ispisPocetnogStanjaStabla()
    else: print("Uneli ste pogresan redni broj opcije. Pokrenite ponovo igru.")
    ok = True
    while ok:
        print("╭───────────────────────────────────╮")
        print("│                MENI               │")
        print("├───────────────────────────────────┤")
        print("│  0. Izadji                        │")
        print("├───────────────────────────────────┤")
        print("│  1. Uparivanje                    │")
        print("├───────────────────────────────────┤")
        print("│  2. Ispravnost unetih pojmova     │")
        print("├───────────────────────────────────┤")
        print("│  3. Da li ste na dobrom putu?     │")
        print("├───────────────────────────────────┤")
        print("│  4. Pomoc                         │")
        print("├───────────────────────────────────┤")
        print("│  5. Nema resenja?                 │")
        print("╰───────────────────────────────────╯")
        print("-> ", end='')
        izborMeni = input().strip()
        if(izborMeni == '0'):
            izlazakIzIgre()
        elif(izborMeni == '1'):
            uparivanje()
        elif(izborMeni == '2'):
            ispravnostUnetihPojmova()
        elif(izborMeni == '3'):
            dobarPut()
        elif(izborMeni == '4'):
            pomoc()
        elif(izborMeni == '5'):
            nemaResenja()
        else:
            print("Uneli ste pogresan broj. Pokusajte ponovo.")
#endregion


stalni_pojmovi = []
matrica = []
M, N, pojmovi, odnosi = unos()
print("Pojmovi:")
print(pojmovi)
print("Odnosi:")
print(odnosi)
print("Matrica:", matrica)
pocetniMeni()
root_stanje = 12
max_dubina = 6
stablo = kreirajStablo(root_stanje, max_dubina)
levelOrderIspis(stablo)
