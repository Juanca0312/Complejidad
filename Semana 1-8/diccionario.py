txt = "El correo de Juan Pérez es juanpe@upc.edu.pe, y la clave: 1#221"
dic = {}

for letter in txt:
    if letter not in dic:
        dic[letter] = 1
    else:
        dic[letter] = dic[letter]+1

print(dic)


#not in, in
#is not, is