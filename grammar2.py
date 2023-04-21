


wrd=[]
new=[]
dictgram = {}
gr = open("grammar.txt",'r')
cu = open("cuvinte.txt",'r')

gram = gr.readline().strip().split()

for i in gram:
    blist = []
    aux = gr.readline().strip().split()
    for el in aux:
        list = []
        list[:0] = el
        blist.append(list)
    dictgram[i]=blist

print(dictgram)

ok = [0]


def prog(wrd,lit):
        if lit in gram:
            nr = len(dictgram[lit])
            j = 0
            while(j < nr):
                new = wrd[:-1]
                for nrl in dictgram[lit][j]:
                    new.append(nrl)
                j=j+1
                if new != wrdtocheck and len(new) <= len(wrdtocheck):
                    prog(new,new[-1])
                else:
                    if (new == wrdtocheck):
                        print("cuvantul ",*new, " este acceptat ")
                        ok[0]=1

        else:
            return None


cuv = []
for cuvant in cu:
    cuv.append(cuvant.strip())

for c in cuv:
    ok[0] = 0
    if len(c) == 0:
        print("cuv vid")
    newc =[]
    newc[:0] = c
    wrdtocheck = newc
    litstart = newc[0]
    for listt in dictgram['S']:
        if litstart in listt:
            wrd = listt
            break
    prog(wrd, wrd[-1])
    if ok[0] == 0:
        print("cuvantul ",*wrdtocheck, " NU este acceptat")




