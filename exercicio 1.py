def contrario(novoAlgo):
    print(" Palavra invertida",novoAlgo)

algo= str(input('Uma palavra: '))
print(' palavra: {}'.format(algo))
novoAlgo = algo[::-1]
print('palavra ao contrário: {}'.format(novoAlgo))