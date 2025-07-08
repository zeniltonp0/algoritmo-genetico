# 🧬 Otimização de Carteira com Algoritmo Genético (PyGAD)

Este projeto utiliza a biblioteca [PyGAD](https://pygad.readthedocs.io/) para otimizar a alocação de ativos financeiros, buscando maximizar o retorno esperado e controlar o risco.

O projeto foi feito para a disciplina de Inteligência Artificial II.

## 📥 Entrada

- **Retornos esperados** dos ativos (vetor `expected_returns`)
- **Riscos** individuais dos ativos (vetor `risks`)

Estes dados são definidos no código como arrays NumPy e representam, respectivamente, o retorno médio e o risco (desvio padrão) de cada ativo.

## 📤 Saída:

### Ao final da execução, o programa imprime:
  
- A melhor alocação de pesos (normalizada para somar 1) — em decimal e em porcentagem

- O retorno esperado do portfólio

- O risco total calculado com base nos pesos

- O valor do fitness da solução

## ▶️ Como executar:

### Clone o repositório:

git clone https://github.com/SEU_USUARIO/algoritmo-genetico-otimizacao.git

### Crie um ambiente virtual:

```python3 -m venv venv```

```source venv/bin/activate  # Linux/macOS``` 

```venv\Scripts\activate     # Windows``` 

### Execute o script

```python main.py``` 


## ⚙️ Funcionamento

O algoritmo genético realiza o seguinte:

  Inicializa populações com diferentes pesos (alocações) para os ativos.

  Avalia cada solução por meio de uma função fitness, que calcula:
  
  Retorno total do portfólio

  Penalizações por risco excessivo

  Seleciona as melhores soluções (pais)

  Recombina (crossover) e muta para gerar novas soluções

  Repete por várias gerações para melhorar os resultados

O objetivo é encontrar a melhor combinação de alocações que maximize o retorno e mantenha o risco abaixo de um limite definido.

## Os participantes do projeto são:
Zenilton Pereira
Bruna Raquel
João Victor Paiva
Vandré Cortês
Eduardo de Carvalho
