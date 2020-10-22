#HOLA QUE TAL AMIGO OCUPA 144 bits, huffman lo reduce
sentence = "hoooolllllaaaaccccccomo"
frecuency = {}
answer = {}
priority_queue = []

#realizamos la frecuencias
for i in range(len(sentence)):
    if sentence[i] not in frecuency:
        frecuency[sentence[i]] = 1
        answer[sentence[i]] = ""
    else:
        frecuency[sentence[i]]+=1
print("frecuencias", frecuency)
#arbolito
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

#agregamos elementos de las frecuencias al priorityQueue
for letter in frecuency:
    priority_queue.append((letter, frecuency[letter]))

priority_queue = sorted(priority_queue, key=lambda x: x[1])

#logica para armar arbol grande
while len(priority_queue) is not 1:
    left = priority_queue.pop(0)
    right = priority_queue.pop(0)
    arbolito = Tree(left[0], right[0])
    priority_queue.append((arbolito, left[1]+right[1]))
    priority_queue = sorted(priority_queue, key=lambda x: x[1])

#recorremos el arbol
def recorrido(tree, code):
    if type(tree) is str:
        answer[tree] = code
        return tree
    
    recorrido(tree.left,code + "0")
    recorrido(tree.right, code + "1")

recorrido(priority_queue[0][0], "")

print(answer)




    