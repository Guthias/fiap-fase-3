# Sistema Inteligente de Gerenciamento de Recursos da Colônia

## 1. (Sobre o projeto)


O **Sistema Inteligente de Gerenciamento de Recursos da Colônia** é um projeto acadêmico desenvolvido como parte das atividades da Fase 3 da FIAP.

A proposta consiste no desenvolvimento de um sistema integrado capaz de representar o funcionamento inteligente de uma colônia, utilizando conceitos fundamentais de programação para organizar informações, monitorar recursos, analisar o consumo energético, realizar previsões e tomar decisões automatizadas.

Desenvolvido em Python, o sistema reúne diferentes funcionalidades relacionadas ao gerenciamento de recursos essenciais, considerando informações sobre geração de energia solar e eólica, reservas energéticas, combustível, condições climáticas e funcionamento dos sistemas operacionais.

A aplicação busca demonstrar como a integração entre estruturas de dados, lógica de programação e modelos matemáticos simples pode contribuir para a administração eficiente dos recursos de uma colônia.


## 2. (Objetivos do projeto)


### 2.1 Objetivo geral

Desenvolver um sistema computacional integrado que represente o gerenciamento inteligente de uma colônia, utilizando estruturas de dados, funções, estruturas condicionais e modelos matemáticos para organizar informações, interpretar situações e auxiliar na tomada de decisões.

### 2.2 Objetivos específicos

- Organizar informações utilizando listas e dicionários.
- Representar os subsistemas por meio de estruturas hierárquicas.
- Implementar regras lógicas para a tomada de decisões automatizadas.
- Monitorar a geração e o consumo de energia.
- Identificar situações de risco e possíveis excedentes energéticos.
- Aplicar regressão linear simples para estimar a geração de energia eólica.
- Analisar informações históricas para realizar previsões.
- Simular eventos climáticos e suas possíveis consequências.
- Desenvolver mecanismos de gerenciamento e economia de recursos.

## 4. (Estrutura e organização do projeto)

O código-fonte está organizado em três diretórios principais, responsáveis por separar as funcionalidades relacionadas à organização dos dados, às previsões e ao gerenciamento do sistema:

```text
├─  (1) - <Dados/>
│   1.1 -├─ dados.py;
│   1.2 -├─ historico.py;
│   1.3 -├─ consumo.py;
│   1.4 -└─ navegacao.py;

├─  (2) - <Previsao/>
│   2.1 -├─ regressao.py;
│   2.2 -├─ gastos.py;
│   2.3 -└─ eventos.py;

├─  (3) - <Sistema/>
│   3.1 -├─ decisao.py;
│   3.2 -├─ energia.py;
│   3.3 -├─ modo_economico.py;
│   3.4 -└─ utilidades.py;

├── (4) - <main.py/>
└── (5) - <README.md/>
```

### 4.1`dados:`

Responsável pela organização, armazenamento e disponibilização das informações utilizadas pela aplicação.

- **dados.py:** contém a estrutura principal da colônia, incluindo informações sobre energia, combustível, clima e sistemas operacionais.
- **historico.py:** armazena registros históricos relacionados à geração energética, velocidade do vento, temperatura e consumo.
- **consumo.py:** realiza cálculos relacionados ao consumo dos sistemas ativos e à geração energética.
- **navegacao.py:** permite visualizar a organização hierárquica das informações e consultar valores por meio de caminhos específicos.

### 4.2 `previsao:`
Reúne funcionalidades responsáveis pelas estimativas e análises dos recursos da colônia.

- **regressao.py:** implementa o cálculo de regressão linear simples para estimar a geração de energia eólica a partir da velocidade do vento.
- **gastos.py:** realiza análises relacionadas à geração, ao consumo e ao saldo energético, identificando também o maior consumidor.
- **eventos.py:** permite simular acontecimentos climáticos e apresentar recomendações conforme as condições da colônia.

### 4.3 `sistema:`

Contém as regras e funcionalidades responsáveis pelo gerenciamento e funcionamento da aplicação.

- **decisao.py:** estabelece regras condicionais para gerar alertas, recomendações e decisões automatizadas.
- **energia.py:** compara a geração energética com o consumo e identifica situações de déficit, excedente ou equilíbrio.
- **modo_economico.py:** gerencia a ativação e desativação do modo econômico, considerando a disponibilidade dos recursos.
- **utilidades.py:** disponibiliza funções auxiliares para receber e validar entradas numéricas.

### 4.4 `main.py:`
Representa o ponto de entrada da aplicação. É responsável por integrar os módulos, apresentar o menu principal e permitir que o usuário acesse as funcionalidades disponíveis por meio de uma interface interativa no terminal.

## 5. (Funcionalidades do sistema)

### 5.1 Organização e navegação dos dados

As informações da colônia são organizadas utilizando dicionários e listas, permitindo representar diferentes subsistemas de maneira hierárquica.

Entre as informações armazenadas estão:

- Energia solar e eólica.
- Reserva energética.
- Combustível.
- Condições climáticas.
- Temperaturas internas e externas.
- Estados operacionais dos sistemas essenciais.

A estrutura hierárquica permite consultar informações específicas sem a necessidade de percorrer manualmente todos os dados armazenados.

### 5.2 Monitoramento das condições da colônia
O sistema realiza verificações relacionadas aos recursos disponíveis, às condições climáticas e ao funcionamento dos sistemas operacionais. Com base nas informações armazenadas, são identificadas situações que podem exigir atenção, permitindo apresentar mensagens informativas, alertas e recomendações.

### 5.3 Sistema de tomada de decisões

A aplicação utiliza estruturas condicionais para analisar diferentes situações e determinar ações conforme as regras estabelecidas.

Entre as possibilidades estão:

- Reduzir o consumo quando a disponibilidade energética estiver baixa.
- Ativar estratégias de economia diante de condições críticas.
- Emitir alertas quando o consumo superar a geração.
- Recomendar o armazenamento de energia excedente.
- Preservar o funcionamento dos sistemas essenciais.

As decisões são determinadas pela análise das condições estabelecidas na lógica do programa.

### 5.4 Gerenciamento do modo econômico

O modo econômico permite reduzir o funcionamento de sistemas não essenciais, priorizando a preservação dos recursos disponíveis.
Durante sua ativação, o sistema:

- Mantém o suporte à vida em funcionamento.
- Desativa o laboratório.
- Desativa a iluminação.
- Aplica uma redução de 10% aos valores registrados de energia solar, eólica e combustível.

Ao desativar o modo econômico, os estados e valores anteriores são restaurados.

### 5.5 Previsão de geração de energia eólica

O projeto utiliza regressão linear simples para analisar a relação entre a velocidade do vento e a quantidade de energia eólica gerada. O cálculo utiliza informações históricas organizadas em listas e determina uma relação matemática entre as variáveis.

A partir dessa relação, o sistema consegue estimar valores de geração energética para novas velocidades de vento informadas pelo usuário.

**Exemplo de utilização:**

Entrada:
```text
Velocidade do vento: 11 m/s
```

Saída aproximada:
```text
Energia eólica prevista: 27.5
```

O sistema também apresenta um aviso quando a velocidade informada está fora da faixa de valores observados no histórico, indicando que a estimativa pode apresentar menor confiabilidade.

### 5.6 Análise de geração e consumo energético

O sistema compara a energia produzida pelas fontes solar e eólica com o consumo dos sistemas ativos.
A partir dessa comparação, identifica três situações principais:

Condição identificada / Interpretação

| (Consumo superior à geração / Possível déficit energético)
| (Geração superior ao consumo / Possibilidade de armazenar energia excedente)
| (Geração igual ao consumo / Equilíbrio entre geração e consumo)

A aplicação também identifica o sistema que apresenta o maior consumo entre os sistemas ativos, contribuindo para a interpretação dos gastos energéticos.

### 5.7 Simulação de eventos climáticos

A aplicação permite simular diferentes acontecimentos que podem afetar o funcionamento da colônia.
Os eventos disponíveis são:

- Tempestade de areia;
- Vento forte;
- Queda de temperatura;

Cada simulação apresenta possíveis consequências e recomendações relacionadas ao gerenciamento dos recursos e às condições operacionais.

### 5.8 Registro de novos dados históricos

O sistema permite adicionar informações referentes a novos dias de operação da colônia.

Entre os dados registrados estão:

- Geração de energia solar.
- Geração de energia eólica.
- Velocidade do vento.
- Consumo energético.
- Temperatura externa.

Esses registros atualizam as listas históricas utilizadas nas análises e nas previsões realizadas durante a execução do programa.

## 6. Como executar o projeto

### 6.1 Pré-requisitos

Para executar a aplicação, é necessário possuir:

- Python 3.10 ou superior.
- Git instalado.
- Terminal ou ambiente de desenvolvimento compatível com Python.

### 6.2 Clonando o repositório

Primeiramente, utilize o comando abaixo para obter uma cópia do projeto:

```bash
git clone https://github.com/Guthias/fiap-fase-3.git
```

### 6.3 Acessando o diretório

Após clonar o repositório, acesse a pasta do projeto:

```bash
cd fiap-fase-3
```

### 6.4 Executando a aplicação

Para iniciar o sistema, execute:

```bash
python main.py
```

Em alguns ambientes, pode ser necessário utilizar:

```bash
python3 main.py
```

Não é necessário instalar dependências externas para executar o projeto.

## 7. (Exemplos de utilização)

### 7.1 Análise de geração e consumo

Considerando os valores iniciais da aplicação:

- Geração solar: 60.
- Geração eólica: 40.
- Consumo do suporte à vida: 35.
- Consumo do laboratório: 30.
- Consumo da iluminação: 20.

Resultado ilustrativo:

```text
Geração total: 100
Consumo total: 85
Saldo energético: 15
```

Interpretação:

```text
SUGESTÃO: armazenar energia excedente
```

### 7.2 Sistema de decisão
Considerando uma situação em que a disponibilidade energética é inferior ao consumo:

Entrada:
```text
Energia: 40
Consumo: 70
Geração: 40
```

Resultado esperado:
```text
ALERTA: reduzir consumo
```

### 7.3 Previsão de energia eólica

Entrada:
```text
Velocidade do vento: 11
```

Resultado aproximado:
```text
Energia eólica prevista: 27.5
```

Os valores apresentados são exemplos de utilização baseados nos dados e nas regras do projeto.

## 8. Contribuição do sistema para o gerenciamento da colônia

A integração das funcionalidades permite que a aplicação organize informações, interprete condições operacionais e apresente recomendações para o gerenciamento dos recursos. A análise da geração e do consumo energético auxilia na identificação de possíveis déficits e excedentes, enquanto as regras condicionais permitem estabelecer respostas para diferentes situações.

A utilização de regressão linear simples amplia essa capacidade ao possibilitar estimativas baseadas em informações históricas, contribuindo para uma ação que não se limita à análise de condições atuais. Dessa maneira, o sistema demonstra a aplicação prática de conceitos computacionais na construção de uma solução integrada focada ao gerenciamento inteligente de recursos.
