import shutil

def escreverArquivo(texto):
    arquivo = open('teste.txt', 'w') #Cria o arquivo, e o 'w' serve para escrever 'a' para atualizar
    arquivo.write(texto)
    arquivo.close()
    
def atualizarArquivo(nomeArquivo, texto):
    arquivo = open(nomeArquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
    
def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    alunoNota = arquivo.read() 
    alunoNota = alunoNota.split('\n')
    
    listaMedia = []
    
    for nota in alunoNota:
        listaNotas = nota.split(',')
        aluno = listaNotas[0]
        listaNotas.pop(0)
        print(aluno)
        print(listaNotas)
        media = lambda notas: sum([int(notaAlunos) for notaAlunos in notas]) / 4
        print(media(listaNotas))
        listaMedia.append({aluno: media(listaNotas)})
    return listaMedia
        
def copiaArquivo(nomeArquivo):
    shutil.copy(nomeArquivo, 'C:/Users/igmath/Documents/ADS')
        
def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo, 'C:/Users/igmath/Documents/ADS/Spring Framerork Experience' )
        

if __name__=='__main__':
    moveArquivo('notas.txt')
    #copiaArquivo('notas.txt')
    #listaMedia = mediaNotas ('notas.txt')
    #print(listaMedia)
    #aluno = '\nKarol 9, 8, 8, 6'
    #escreverArquivo('Primeira Linha\n')
    #atualizarArquivo('notas.txt', aluno)
    #lerArquivo('teste.txt')