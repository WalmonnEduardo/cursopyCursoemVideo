class Texto():
   
    @staticmethod
    def  alinhar_topicos(itens):
        maior = Texto.contagem(itens)
        for item in itens:
            while len(item) < maior:
                item += " "
            item += ":"
            print(item)

    @staticmethod
    def contagem(itens):
        maior = 0
        for item in itens:
            n = len(item)
            if n > maior:
                maior = n
        maior += 1
        return maior

    @staticmethod
    def tabela(itens):
        maior = Texto.contagem(itens)+13
        numr = len(itens)*2+1
        a = 0
        for i in range(numr):
            if i%2 == 1:
                p = a+1
                p = str(p)
                linha = "[ "+p+" -> "
                linha += itens[a]
                while len(linha) < maior:
                    linha += " "
                linha += "]"
                print(linha)
                a += 1
            else:
                linha = "="
                while len(linha) < maior:
                    linha += "="
                linha += "="
                print(linha)