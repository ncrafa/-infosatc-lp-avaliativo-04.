
senha=[]
usuario=0
apto=[]
cpf=[]
nome=[]


def pessoa ( apto, senha , nome , x , y , cpf ):
    
    print( "O nome do usuario",x,"é",nome [ y ])
    print( "O cpf do usuario",x,"é",cpf [ y ])
    print( "A senha do usuario",x,"é",senha [ y ])
    print( "O usuario",x,"esta apto?",apto [ y ])
    print( "" )
def casdastro ():
    nome.anexar( input ( " nome :" ))
    senha.anexar( input ( "senha :" ))
    cpf.anexar( input ( " cpf:" ))
    apto.anexar( input ( " apto:" ))
    
for x in range(5):
    descricao=""
    escolha=""
    conta=0
    print("")
    idade=(int(input("Insira a sua idade: ")))
    peso=(float(input("Insira o seu peso: ")))
    tempo=(float(input("Dormiu quantas horas na última noite : ")))
    if idade>16 and idade<69:
        conta+=1
    else:
        descricao="idade"+descricao
    if peso>50:
        conta+=1
    else:
        descricao="peso"+descricao
    if tempo>6:
        conta+=1
    else:
        descricao="sono"+descricao
    if conta==3:
        print("Pode doar sangue")
        escolha=(input("Deseja se cadastrar?(s/n): "))
        if(escolha=="s"):
           pessoa()
        else:
            pass
    else:
        print("Não está apto a doar sangue,falta de:",descricao)

for x in range(usuario):
  casdastro()