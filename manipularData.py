from datetime import date, time, datetime, timedelta

    # srtftime convete para String, e acima está no tipo date
    # O Y maiusculo traz os 4 dígitos do ano, minusculo 2
    # A maiusculo recebe dia da semana, B maiusculo o mês por escrito
    
def trabalhandoComDatetime():
    dateAtual = datetime.now()
    print(dateAtual)
    print(dateAtual.strftime('%d/%m%Y %H:%M:%S')) #especifica o que quer, e tira o milisegundos
    print(dateAtual.strftime('%c')) #traz mais completo
    print(dateAtual.weekday())
    
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo' )
    print(tupla[dateAtual.weekday()]) #Forma de importar em portugês
    
    dataCriada = datetime(2020, 6, 20, 15, 30 , 15)
    print(dataCriada)
    print(dataCriada.strftime('%c'))
    
    #strptime converte para dataetime
    dataString = '01/01/2019 20:15:56'
    dataConvertida = datetime.strptime(dataString, '%d/%m/%Y %H:%M:%S')
    print(dataString)
    print(type(dataString))
    print(dataConvertida)
    print(type(dataConvertida))
    
    #timedelta é para fazer operação data( em formato de dias ), e horas normalmente
    novaData = dataConvertida - timedelta(days=365, hours=7, minutes=11, seconds=1)
    print(novaData)
    
        
def trabalhandoComDate():
    dataAtual = date.today()
    dataAtualStr = dataAtual.strftime('%d/%m/%Y') 
    print(dataAtual.strftime('%A %B %Y'))
    print(type(dataAtual))
    print(type(dataAtualStr))

def trabalhandoComTime():
    # Hora é sempre Maiúsculo
    horario = time(hour=15, minute=10, second=30)
    horarioStr = horario.strftime('%H:%M:%S')
    print(type(horario))
    print(horario)
    print(type(horarioStr))
    print(horarioStr)
    
    
if __name__=='__main__':
    #trabalhandoComDate()
    #trabalhandoComTime()
    trabalhandoComDatetime()