# Sistema Inteligente de Gerenciamento de Recursos da Colônia

Projeto acadêmico desenvolvido em Python para representar, de forma integrada, o monitoramento e a gestão de recursos de uma colônia. A aplicação organiza dados em estruturas hierárquicas, aplica regras de decisão e usa regressão linear simples para estimar a geração de energia eólica.

## Objetivo

Transformar informações sobre energia, consumo, clima e sistemas da colônia em análises e recomendações simples. O projeto demonstra a organização de dados, a navegação entre subsistemas, a aplicação de lógica condicional e o uso de dados históricos para fazer uma estimativa.

## O que o sistema faz

- Organiza os dados da colônia em dicionários hierárquicos.
- Exibe a hierarquia e permite consultar um valor por um caminho, como `colonia/energia/solar`.
- Verifica níveis de energia solar e eólica, combustível, temperaturas e estado dos sistemas.
- Compara geração e consumo e informa déficit, excedente ou equilíbrio; também identifica o sistema ativo de maior consumo.
- Aplica regras de decisão para recomendar redução de consumo, modo econômico ou armazenamento de excedentes.
- Ajusta uma reta por mínimos quadrados com os dados históricos de vento e geração eólica, e estima a geração para uma velocidade informada.
- Simula recomendações para eventos climáticos predefinidos.
- Permite registrar novas leituras diárias no histórico durante a execução.
- Ativa e desativa um modo econômico que preserva o suporte à vida, desliga laboratório e iluminação e altera os valores de energia e combustível.

## Como os dados e as regras estão organizados

Os dados correntes ficam em `dados/dados.py`, em um dicionário com as chaves `energia`, `combustivel`, `clima` e `sistema`. Os dados históricos ficam em `dados/historico.py`, separados em listas de geração solar, geração eólica, velocidade do vento, temperatura externa e consumo.

A lógica de decisão está em `sistema/decisao.py`. Por exemplo, com energia abaixo de 50 e consumo de pelo menos 80, o sistema recomenda ativar o modo econômico; com energia abaixo de 50, mas consumo menor, recomenda reduzir o consumo. A análise de balanço em `sistema/energia.py` compara geração e consumo: consumo maior indica alerta, geração maior sugere armazenar excedente e valores iguais indicam equilíbrio.

A previsão eólica usa a velocidade do vento como variável de entrada e a geração eólica como variável estimada. A regressão é calculada a partir do histórico existente e o programa avisa quando a velocidade informada está fora do intervalo observado. É uma estimativa simples, não uma garantia de geração futura.

## Exemplo de entrada e saída

Na opção **6 — Previsão de energia eólica**, ao informar uma velocidade do vento de `11 m/s`, o histórico atual produz uma estimativa próxima de `27.5`:

```text
Velocidade do vento prevista (m/s): 11
Energia eólica prevista: 27.5
```

Na opção **7 — Análise geração x consumo**, considerando geração de 40 e consumo de 70, o sistema informa:

```text
ALERTA: consumo maior que geração
```

Se a geração for 80 e o consumo 30, a recomendação é armazenar a energia excedente.

## Executar o projeto

### Pré-requisitos

- Python 3.10 ou superior (o menu usa `match/case`, disponível a partir do Python 3.10).
- Git, caso queira clonar o repositório.

Não são necessárias bibliotecas externas.

### Clonar e iniciar

```bash
git clone https://github.com/Guthias/fiap-fase-3.git
cd fiap-fase-3
python main.py
```

Em alguns ambientes, use `python3 main.py`.

## Menu da aplicação

Ao iniciar `main.py`, o programa apresenta as seguintes opções:

1. Ver a hierarquia da colônia.
2. Consultar um valor por caminho.
3. Verificar os dados da colônia.
4. Executar o sistema de decisão com dados atuais ou valores simulados.
5. Ativar ou desativar o modo econômico.
6. Prever energia eólica por regressão linear.
7. Analisar geração, consumo, saldo e maior consumidor.
8. Simular um evento climático.
9. Registrar um novo dia no histórico.
0. Sair.

## Estrutura do projeto

```text
├── (1) - <dados/>
│   1.1 -├── consumo.py       # Cálculos de consumo dos sistemas ativos e geração atual;
│   1.2 -├── dados.py         # Estado inicial da colônia;
│   1.3 -├── historico.py     # Séries históricas e registro de novas leituras;
│   1.4 -├── limite.py        # Estrutura de limites de referência;
└── 1.5 -└── navegacao.py     # Exibição e consulta da hierarquia;

├── (2) - <Previsao/>
│   2.1 -├── eventos.py       # Eventos climáticos e recomendações;
│   2.2 -├── gastos.py        # Balanço energético e maior consumidor;
└── 2.3 -└── regressao.py     # Ajuste da reta e previsão eólica;

├── (3) - <sistema/>
│   3.1 -├── decisao.py       # Regras de decisão automatizadas;
│   3.2 -├── energia.py       # Comparação entre geração e consumo;
│   3.3 -├── modo_economico.py# Verificação de dados e modo econômico;
└── 3.4 -└── utilidades.py    # Leitura de valores numéricos;

├── (4) - <visuais/>
│   4.1 - exibir_card.py   # Funções auxiliares de exibição;
│   4.2 - main.py              # Ponto de entrada e menu executado;
│   4.3 - menu_principal.py    # Menu visual auxiliar;
└── 4.4 - README.md;
```

O fluxo principal atualmente é iniciado por `main.py`, que apresenta o menu no terminal. O registro de novos dias é mantido em memória e não persiste depois que a aplicação é encerrada.

## Escopo e observações

- O modo econômico subtrai 10 unidades dos valores registrados de energia solar, energia eólica e gasolina (limitando-os a zero); não calcula uma redução percentual. Ao desativá-lo, restaura os valores salvos antes da ativação.
- A reserva energética é usada em algumas regras e simulações, mas a análise de geração e consumo compara a geração solar e eólica com o consumo dos sistemas ligados.
- Os eventos climáticos retornam recomendações simuladas; eles não alteram automaticamente os dados da colônia.
- `dados/limite.py`, `menu_principal.py` e `visuais/exibir_card.py` estão no repositório, mas não são usados pelo fluxo principal de `main.py`.
- O sistema é uma simulação acadêmica, não um controlador de recursos de uma instalação real.

## Contexto acadêmico

O projeto atende à proposta de integrar organização de dados, lógica de decisão, análise do uso de energia e previsão simples com regressão, priorizando clareza, funções e conceitos introdutórios de programação. Neste projeto, não utilizamos banco de dados nem recursos de desenvolvimento mais avançados. Os dados ficam em estruturas mantidas na memória enquanto o programa está aberto; por isso, os registros feitos durante a execução não são preservados depois que ele é encerrado.
