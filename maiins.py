#Crie um sistema de pedidos com as classes
#-Pedido (atr: valorTotal; metodos: adicionarItem e obterTotal)
#-ItemPedido (atr:quantidade; Metodos: itemPedido(construtor) recendo produto e quantidade)
#-Produto(atr: codigo,valor,descrição; metodos: produto(construtor)recebendo codigo valor e descrição)
class Pedido:
    def __init__(self) -> None:
        self.total = 0
        self.items = []
    def adicionarItem(self,produto, quantidade):
        self.items.append(ItemPedido(produto,quantidade))
    def calcularTotal(self):
        for i in self.items:
            self.total += i.quantidade * i.produto.valor
        return self.total
class ItemPedido:
    def __init__(self, produto, quantidade) -> None:
        self.produto = produto
        self.quantidade = quantidade
class Produto:
    def __init__(self,codigo,valor,descricao) -> None:
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
almondega = Produto("001",15,"Almondega congelada")
aguaDeBanho = Produto("666",15000,"Agua gostosas")
controle = Produto("002",20,"Controle Remoto")
pedido = Pedido()
pedido.adicionarItem(almondega,10)
pedido.adicionarItem(aguaDeBanho,2)
pedido.adicionarItem(controle,1)

print(pedido.items[0].quantidade)
print(pedido.calcularTotal())