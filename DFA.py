class NFA:
    def __init__(self, delta, q0, final,words):
        self.delta = delta #tranzitii
        self.q0 = q0 #stare initiala
        self.final = final
        self.words = words


    def cuvinte(self,state,word,n,length,last):
        if length < n:
            for i in range(len(self.delta[state])):
                if last != delta[state]:
                    last = (self.delta[state][i][0], state)
                    if self.delta[state][i][0] == "`":
                        # cuv = word + self.delta[state][i][0]
                        self.cuvinte(delta[state][i][1],word,n,length + 1,last)
                    else:
                        cuv = word + self.delta[state][i][0]
                        if delta[state][i][1] in self.final:
                            self.words.append(cuv)
                        self.cuvinte(delta[state][i][1],cuv,n,length + 1,last)
                else:
                    continue
        else:
            return False

    def w(self):
        return self.words




f = open("automata.in", 'r')

q0 = f.readline().strip()
final = [x.strip() for x in f.readline().split()]
delta = {}

for linie in f:
    linie = linie.split()
    if linie[0] in delta:
        delta[linie[0]].append((linie[1],linie[2]))
    else:
        delta[linie[0]] = [(linie[1],linie[2])]


auto = NFA(delta,q0,final,[])


auto.cuvinte(q0,"",6,0,("",""))
print(set(auto.w()))

