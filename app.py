from modelos.restaurante import Restaurante

pizzaria = Restaurante('pizza 69', 'Italiana')

sushi = Restaurante('papaya sushi', 'Japones')


def main():

    Restaurante.listar_restaurantes()

#evita que o arquivo app seja importado por outro script
if __name__ == '__main__':
    main()