class Produto:
    def __init__(self, nome, descricao, codigo, valor, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.codigo = codigo
        self.valor = valor
        self.quantidade = quantidade


    def __str__(self):
        return f'''Produto: {self.nome}
Descrição: {self.descricao}
Código: {self.codigo}
Valor: {self.valor}
Quantidade: {self.quantidade}'''
    
produto1 = Produto("Arroz", "Integral", 11, 25.00, "5Kg" )
    
print(produto1)