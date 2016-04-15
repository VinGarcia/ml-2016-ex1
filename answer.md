
# Lista prática de exercícios

```
Autor: Vinícius Veloso de Mello Garcia
Matrícula: 2015662027
Disciplina: Aprendizado de Máquina 2016/1
Instituição: Universidade Federal de Minas Gerais - UFMG
```

# Introdução

Segue abaixo a resolução da lista de exercícios 1 disponibilizada no
[site da disciplina][1] pelo monitor Felipe Moraes e prof. Adriano Veloso.

Os exercícios abaixo foram realizados após realizar o download dos seguintes
arquivos de dados necessários:

1. `spam_test.txt`
2. `spam_train.txt`

## Exercício 1 (Train and validation sets):

Divida o arquivo `spam_train.txt` que contém 5000 linhas em dois arquivos:

1. `spam_train.txt` com as primeiras 4000 linhas do arquivo original.
2. `spam_validation.txt` com 1000 últimas linhas do arquivo original.

E então explique com suas palavras porque seria difícil avaliar a qualidade
dos classificadores que irei produzir neste exercício sem realizar essa
divisão previa dos dados de treino.

### Resposta:

A divisão dos dois arquivos foi realizada rapidamente utilizando a ferramenta `vim`.

O motivo pelo qual a avaliação se tornaria difícil é porque não haveriam dados disponíveis
para testar a generalização do meu algoritmo. Logo eu não poderia avaliar a presença ou
ausência do fenomeno de _overfitting_ em meus classificadores.

## Exercício 2 (Feature vectors):

Transforme todos os e-mails em `feature vectores`:

1. Encontre todas as palavras presentes nos e-mails de treino.
2. Forme o vocabulário com todas as palavras que aparecem e mmais de 30 e-mails.
3. Crie um _feature vector_ para cada e-mail, ou seja  
   Um vetor indexado segundo as palavras do vocabulário onde cada posição indica
   se a respectiva palavra está ou não presente no e-mail.

### Resposta:

Foi criado um script `ex2.py` para executar estas tarefas. Os arquivos produzidos
foram salvos no formato `JSON` nos seguintes arquivos:

- `ex2-vocabulary.json`
- `ex2-fvecs.json`

## Exercício 3 (Perceptron):

### Questão 3.1

Implemente as funções:

a. `perceptron_train(data)`

Essa função deve receber a tabela com os dados de
**treino** e suas respectivas classes.

Em sua execução ela deve repetir as atualizações dos pesos do
perceptron até que se obtenha 100% de acerto no treino.

Ela deve retornar:

- A contagem de atualizações individuais dos pesos.
- O número de iterações por toda a tabela (o número de eras)
- Os pesos finais calculados.

b. `perceptron_test(w_vec, data)`

Essa função deve receber:

- Os pesos calculados pela função `perceptron_train()`
- A tabela com os dados de **validação** e suas respectivas classes.

Ela deverá retornar a porcentagem de acertos no teste.

#### Resposta:

Foi implementado uma classe de nome `Perceptron`. Essa classe contém:

- Um vetor de pesos `w_vec`
- A função `train(data)` que representa a função `perceptron_train(data)`
- A função `test(data)` que representa a função `perceptron_test(data)`

### Questão 3.2



















