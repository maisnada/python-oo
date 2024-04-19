from modelos.avaliacao import Avaliacao

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):
        
        self._nome = nome.title()
        self._categoria = categoria
        self._status = False #Private
        self._avaliacao = []
        
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        
        return f'{self._nome} - {self._categoria}' 
    
    @classmethod #metódo da class, como pro exemplo static e parâmetro cls é uma convenção
    def listar_restaurantes(cls):
        
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        
        for restaurante in cls.restaurantes:
            
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante._status}')
            
    
    @property #muda como o atributo será lido
    def status(self):
        
        return '☑' if self._status else '☒'
    
    def alternar_status(self):
        
        self._status = not self._status
    

