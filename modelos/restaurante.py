class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        
        self.nome = nome
        self.categoria = categoria
        self._status = False #Private
        
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        
        return f'{self.nome} - {self.categoria}' 
    
    def listar_restaurantes():
        
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        
        for restaurante in Restaurante.restaurantes:
            
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.status}')
            
    @property #muda como o atributo será lido
    def status(self):
        
        return '☑' if self._status else '☒'
    

pizzaria = Restaurante('Dom Corneone', 'Massa')

sushi = Restaurante('Sushi', 'Japones')

Restaurante.listar_restaurantes()

#pizzaria.nome = 'Dom Corneone'
#pizzaria.categoria = 'Massa'

#show attributes
#print(dir(pizzaria))

#show attributes format dic
#print(vars(pizzaria))

