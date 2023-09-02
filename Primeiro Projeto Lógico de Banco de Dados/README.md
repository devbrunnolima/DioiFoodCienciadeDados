# Projeto Lógico do Banco de Dados - E-commerce

Este documento descreve o projeto lógico do banco de dados para um sistema de e-commerce. O banco de dados foi criado com o objetivo de gerenciar informações relacionadas a clientes, produtos, pedidos, fornecedores e vendedores em um ambiente de comércio eletrônico. Com base no esquema:  

![PrimeiroProjetoLogicodeBancodeDados](https://github.com/devbrunnolima/DioiFoodCienciadeDados/blob/main/Primeiro%20Projeto%20L%C3%B3gico%20de%20Banco%20de%20Dados/PrimeiroProjetoLogicodeBancodeDados.JPG)

## Descrição das Tabelas

### Tabela `clients`
- Armazena informações sobre os clientes.
- Campos:
  - `idClient` (Chave Primária): Identificador único do cliente.
  - `Fname`: Primeiro nome do cliente.
  - `Minit`: Inicial do nome do meio do cliente.
  - `Lname`: Sobrenome do cliente.
  - `CPF`: Número de CPF do cliente (chave única).
  - `Address`: Endereço do cliente.

### Tabela `product`
- Armazena informações sobre os produtos disponíveis para compra.
- Campos:
  - `idProduct` (Chave Primária): Identificador único do produto.
  - `Pname`: Nome do produto.
  - `classification_kids`: Indica se o produto é destinado a crianças (booleano).
  - `category`: Categoria do produto (Eletrônico, Vestimenta, Brinquedos, Alimentos, Móveis).
  - `avaliação`: Avaliação do produto (pode ser nulo).
  - `size`: Tamanho do produto (pode ser nulo).

### Tabela `orders`
- Armazena informações sobre os pedidos feitos pelos clientes.
- Campos:
  - `idOrder` (Chave Primária): Identificador único do pedido.
  - `idOrderClient`: Identificador do cliente que fez o pedido (chave estrangeira).
  - `orderStatus`: Status do pedido (Cancelado, Confirmado, Em processamento).
  - `orderDescription`: Descrição do pedido.
  - `sendValue`: Valor do envio.
  - `paymentCash`: Indica se o pagamento foi em dinheiro (booleano).

### Tabela `productStorage`
- Armazena informações sobre o estoque de produtos.
- Campos:
  - `idProdStorage` (Chave Primária): Identificador único do registro de estoque.
  - `storageLocation`: Localização do estoque.
  - `quantity`: Quantidade disponível do produto.

### Tabela `supplier`
- Armazena informações sobre os fornecedores de produtos.
- Campos:
  - `idSupplier` (Chave Primária): Identificador único do fornecedor.
  - `SocialName`: Nome social do fornecedor.
  - `CNPJ`: Número de CNPJ do fornecedor (chave única).
  - `contact`: Informações de contato do fornecedor.

### Tabela `seller`
- Armazena informações sobre os vendedores que atuam no e-commerce.
- Campos:
  - `idSeller` (Chave Primária): Identificador único do vendedor.
  - `SocialName`: Nome social do vendedor.
  - `AbstName`: Nome abreviado do vendedor.
  - `CNPJ`: Número de CNPJ do vendedor (pode ser nulo).
  - `CPF`: Número de CPF do vendedor (pode ser nulo).
  - `location`: Localização do vendedor.
  - `contact`: Informações de contato do vendedor.

### Tabela `productSeller`
- Estabelece a relação entre vendedores e produtos que eles vendem.
- Campos:
  - `idPseller`: Identificador do vendedor (chave estrangeira).
  - `idProduct`: Identificador do produto (chave estrangeira).
  - `prodQuantity`: Quantidade do produto disponível com o vendedor.

### Tabela `productOrder`
- Estabelece a relação entre pedidos e produtos associados a esses pedidos.
- Campos:
  - `idPOproduct`: Identificador do produto (chave estrangeira).
  - `idPOorder`: Identificador do pedido (chave estrangeira).
  - `poQuantity`: Quantidade do produto no pedido.
  - `poStatus`: Status do produto no pedido (Disponível, Sem estoque).

### Tabela `storageLocation`
- Estabelece a relação entre produtos e suas localizações no estoque.
- Campos:
  - `idLproduct`: Identificador do produto (chave estrangeira).
  - `idLstorage`: Identificador do registro de estoque (chave estrangeira).
  - `location`: Localização do produto no estoque.

### Tabela `productSupplier`
- Estabelece a relação entre fornecedores e os produtos que eles fornecem.
- Campos:
  - `idPsSupplier`: Identificador do fornecedor (chave estrangeira).
  - `idPsProduct`: Identificador do produto (chave estrangeira).
  - `quantity`: Quantidade do produto fornecida pelo fornecedor.

### Tabela `payments`
- Armazena informações sobre os pagamentos realizados pelos clientes.
- Campos:
  - `idPayment`: Identificador do pagamento.
  - `idClient`: Identificador do cliente que efetuou o pagamento (chave estrangeira).
  - `typePayment`: Tipo de pagamento (Boleto, Cartão, Dois Cartões).
  - `limitAvailable`: Limite disponível para pagamento.

## Consultas de Exemplo

O banco de dados permite a realização de diversas consultas para gerenciamento e análise de dados. Alguns exemplos de consultas incluem:

- Recuperação de todos os clientes cadastrados.
- Recuperação de todos os produtos disponíveis.
- Recuperação de todos os vendedores cadastrados.
- Recuperação de todos os pedidos realizados pelos clientes.
- Recuperação de pedidos com produtos associados.
- Recuperação do número de pedidos realizados por cliente.

## Observações

- O banco de dados possui chaves primárias e chaves estrangeiras para garantir a integridade referencial dos dados.
- As tabelas `payments` e `productSeller` são relacionadas aos clientes e vendedores, mas podem ser desenvolvidas e utilizadas para registrar informações de pagamento e relação entre vendedores e produtos, respectivamente.
