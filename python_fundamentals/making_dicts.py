def make_dict(lista,listb):
    if len(listb) > len(lista):
        temp = lista
        lista = listb
        listb = temp
    new_dict={}
    new_dict=dict(zip(lista,listb))
    return new_dict    








name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

faveanimalsdict = make_dict(name,favorite_animal)
print faveanimalsdict