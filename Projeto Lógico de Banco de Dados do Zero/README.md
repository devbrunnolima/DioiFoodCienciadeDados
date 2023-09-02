# Projeto Lógico - Oficina Mecânica

Este é um projeto lógico de banco de dados para uma oficina mecânica. Ele descreve as tabelas, relacionamentos e dados essenciais para o funcionamento de uma oficina mecânica fictícia.  Com base no esquema:  

![ProjetoLogicodeBancodeDadosdoZero]()

## Entidades Essenciais

### Tipo de Logradouro
- **id_tipo_logradouro** (Chave Primária, Inteiro, Auto-incremento)
- **tipo_logradouro** (Texto, Não Nulo)

Esta tabela armazena os tipos de logradouro, como Rua, Avenida, Alameda, etc.

### Estado
- **id_estado** (Chave Primária, Inteiro, Auto-incremento)
- **estado** (Texto, Não Nulo)
- **sigla_estado** (Texto, Não Nulo)

Esta tabela armazena os estados brasileiros e suas siglas.

### Equipe Especialidade
- **id_especialidade** (Chave Primária, Inteiro, Auto-incremento)
- **especialidade** (Texto, Não Nulo)

Esta tabela armazena as especialidades da equipe da oficina, como Mecatrônica, Funilaria, etc.

### Peça
- **id_peça** (Chave Primária, Inteiro, Auto-incremento)
- **nome_peça** (Texto)
- **valor_peça** (Ponto Flutuante)

Esta tabela armazena informações sobre peças que podem ser usadas nas ordens de serviço.

### Serviço
- **id_serviço** (Chave Primária, Inteiro, Auto-incremento)
- **serviço** (Texto, Não Nulo)
- **valor_serviço** (Ponto Flutuante, Não Nulo)

Esta tabela armazena os serviços oferecidos pela oficina e seus valores.

### Ordem de Serviço Status
- **id_ordem_serviço_status** (Chave Primária, Inteiro, Auto-incremento)
- **ordem_serviço_status** (Texto, Não Nulo)

Esta tabela armazena os status possíveis das ordens de serviço, como "Em Análise" e "Veículo Entregue".

## Demais Entidades

### Cliente
- **id_cliente** (Chave Primária, Inteiro, Auto-incremento)
- **nome_cliente** (Texto, Não Nulo)
- **sobrenome_cliente** (Texto, Não Nulo)
- **cpf** (Texto, Não Nulo)
- **email** (Texto, Não Nulo)
- **telefone_residencial** (Texto)
- **telefone_celular** (Texto, Não Nulo)
- **telefone_comercial** (Texto)

Esta tabela armazena informações sobre os clientes da oficina, incluindo nome, CPF, e-mail e números de telefone.

### Veículo
- **id_veículo** (Chave Primária, Inteiro, Auto-incremento)
- **id_cliente** (Chave Estrangeira, Inteiro)
- **tipo_veículo** (Texto, Não Nulo)
- **modelo_veículo** (Texto, Não Nulo)
- **marca_veículo** (Texto, Não Nulo)
- **ano_veículo** (Data, Não Nulo)

Esta tabela armazena informações sobre os veículos dos clientes, incluindo tipo, modelo, marca e ano.

### Veículo Serviço
- **id_veículo_serviço** (Chave Primária, Inteiro, Auto-incremento)
- **id_veículo** (Chave Estrangeira, Inteiro)
- **id_serviço** (Chave Estrangeira, Inteiro)

Esta tabela associa serviços a veículos específicos, permitindo que a oficina registre quais serviços foram realizados em quais veículos.

### Tabela de Referência
- **id_tabela_referência** (Chave Primária, Inteiro, Auto-incremento)
- **id_serviço** (Chave Estrangeira, Inteiro)
- **valor_serviço** (Ponto Flutuante, Não Nulo)
- **tempo_conclusão** (Texto, Não Nulo)

Esta tabela fornece informações de referência para serviços, incluindo valores e tempo estimado de conclusão.

### Equipe
- **id_equipe** (Chave Primária, Inteiro, Auto-incremento)
- **nome_equipe** (Texto, Não Nulo)

Esta tabela armazena informações sobre as equipes de mecânicos da oficina.

### Endereço
- **id_endereço** (Chave Primária, Inteiro, Auto-incremento)
- **id_tipo_logradouro** (Chave Estrangeira, Inteiro)
- **logradouro** (Texto, Não Nulo)
- **numero** (Texto, Não Nulo)
- **complemento** (Texto)
- **bairro** (Texto, Não Nulo)
- **cep** (Texto, Não Nulo)
- **cidade** (Texto, Não Nulo)
- **id_estado** (Chave Estrangeira, Inteiro)

Esta tabela armazena informações de endereço, incluindo logradouro, número, bairro, CEP, cidade e estado.

### Mecânico
- **id_mecânico** (Chave Primária, Inteiro, Auto-incremento)
- **id_especialidade** (Chave Estrangeira, Inteiro)
- **id_equipe** (Chave Estrangeira, Inteiro)
- **id_endereço** (Chave Estrangeira, Inteiro)
- **nome_mecânico** (Texto, Não Nulo)
- **sobrenome_mecânico** (Texto, Não Nulo)

Esta tabela armazena informações sobre os mecânicos da oficina, incluindo especialidade, equipe e endereço.

### Ordem de Serviço
- **id_ordem_serviço** (Chave Primária, Inteiro, Auto-incremento)
- **numero_ordem_serviço** (Inteiro, Não Nulo)
- **id_ordem_serviço_status** (Chave Estrangeira, Inteiro)
- **id_tabela_referência** (Chave Estrangeira, Inteiro)
- **id_cliente** (Chave Estrangeira, Inteiro)
- **id_equipe** (Chave Estrangeira, Inteiro)
- **data_emissão** (Data)
- **valor** (
