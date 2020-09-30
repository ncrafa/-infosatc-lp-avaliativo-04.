
algo= str(input('Digite uma palavra: '))
outroAlgo= str(input('Digite outra palavra : '))
print(' A palavra: {}'.format(algo))
print(' E a palavra: {}'.format(outroAlgo))
string = algo[::-1]
outraString = outroAlgo
if (algo == outroAlgo):
     print("As palavras são inversas")
elif(string != outraString):
    print("as palavras não são inversas")
       
