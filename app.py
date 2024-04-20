from modelos.restaurante import Restaurante

pizzaria = Restaurante('pizza 74', 'Italiana')

sushi = Restaurante('papaya sushi', 'Japonesa')

sushi.receber_avaliacao('Marcelo', 10)
sushi.receber_avaliacao('Rosa', 10)

pizzaria.receber_avaliacao('Bruno', 5)
pizzaria.receber_avaliacao('Vanessa', 8)


def main():

    Restaurante.listar_restaurantes()

#evita que o arquivo app seja importado por outro script
if __name__ == '__main__':
    main()