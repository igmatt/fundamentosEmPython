#Digitar pip install requests no terminal para instalar o pacote request
import requests

def retornaDadosCep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code) # 200 quer dizer com sucesso, 400 quer dizer Not Found
    print(type(response.text))
    print(response.json()) #Converte para dicionário
    print(response.text) #Mostra todo texto da URL

    dadosCep = response.json()
    print(dadosCep['logradouro'])
    print(dadosCep['complemento'])
    return dadosCep
    
    
def retoraDadosPokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dadosPokemon = response.json()
    return dadosPokemon
    
def retornaResponse(url):
    response = requests.get(url)
    return response.text
    
    
if __name__=='__main__':
    response = retornaResponse('https://globalacademy.com/')
    print(response) #Retorna todo HTML do site
    
    #retornaDadosCep('01001000')
    
    #dadosPokemon = retoraDadosPokemon('pikachu')
    #print(dadosPokemon['sprites']['front_shiny']) #retorna o link no terminal da imagem do pokemon