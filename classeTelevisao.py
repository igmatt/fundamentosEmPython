# Funções Tudo que retorna valor /  Métodos  Não retorna valor

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
            
    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1
        
    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1
            
if __name__=='__main__':
            
    televisao = Televisao()
    print('A Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power() # Liga a TV
    print('A Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power() # Desliga a TV
    print('A Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power() #Liga a TV

    print('Canal: {}'.format(televisao.canal)) #canal atual

    televisao.aumentaCanal() #aumenta canal
    televisao.aumentaCanal() #aumenta canal

    print('Canal: {}'.format(televisao.canal))

    televisao.diminuiCanal()
    print('Canal: {}'.format(televisao.canal))