class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        
        self.nome = nome
        self.categoria = categoria
        self.status = False
        
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        
        return f'{self.nome} - {self.categoria}' 
    
    def listar_restaurantes():
        
        for restaurante in Restaurante.restaurantes:
            
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.status}')
    

pizzaria = Restaurante('Dom Corneone', 'Massa')

sushi = Restaurante('Sushi', 'Japones')

Restaurante.listar_restaurantes()

#pizzaria.nome = 'Dom Corneone'
#pizzaria.categoria = 'Massa'

#show attributes
#print(dir(pizzaria))

#show attributes format dic
#print(vars(pizzaria))

print(pizzaria)