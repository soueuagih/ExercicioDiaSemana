# ExercicioDiaSemana

## Descrição

Este projeto implementa o padrão de projeto **Strategy**, onde cada dia da semana possui uma estratégia responsável por executar um comportamento específico.

O programa identifica o dia atual do sistema ou permite que o usuário informe um dia da semana. Com isso, uma estratégia é selecionada para apresentar uma recomendação de prioridade e uma mensagem relacionada à tarefa informada (que pode variar).

Para tratar dias inválidos ou sem estratégia cadastrada (como feriados, por exemplo), foi utilizada uma estratégia padrão (`NullStrategy`), aplicando o padrão **Null Object**.

# Estrutura do Projeto

```
main.py

├── DayStrategy (classe abstrata)
├── MondayStrategy
├── TuesdayStrategy
├── WednesdayStrategy
├── ThursdayStrategy
├── FridayStrategy
├── SaturdayStrategy
├── SundayStrategy
├── NullStrategy
└── StrategySelector
```

---

# Padrões Utilizados
## Strategy

Encapsular os comportamentos variáveis em classes independentes.
Cada dia da semana possui sua própria estratégia, o que permite criar novos comportamentos sem mudar a lógica principal do programa.

---

## Null Object

*Implementado através da classe `NullStrategy`.
Quando um dia inválido é informado, essa estratégia é utilizada para exibir uma mensagem padrão, evitando verificações de valores nulos e tornando o código mais limpo.

---

<br>

# Questões de reflexão

## 1. Como evitar verificações repetidas de valores nulos no código principal?

Usando **Null Object**, que retorna um objeto que implemente a interface da estratégia. Assim, o código principal não precisa verificar se existe uma estratégia antes de executá-la.

---

## 2. Qual padrão de projeto pode ser utilizado para representar a ausência de uma estratégia de forma segura?

O padrão **Null Object**, que representa um comportamento padrão para situações sem estratégia/inválidas.

---

## 3. Como esse padrão foi incorporado ao projeto?

Foi criada a classe `NullStrategy`, que implementa a mesma interface das demais estratégias.
Quando o `StrategySelector` não encontra uma estratégia para o dia informado, ele retorna uma instância de `NullStrategy`, fazendo com que o programa continue funcionando normalmente.

---
<br>

# Conclusão

A utilização dos padrões **Strategy** e **Null Object** permitiu desenvolver uma solução organizada, flexível, expansível e de fácil manutenção.
O uso de casos de teste pré-definidos facilita a demonstração do funcionamento do programa, permitindo validar cenários e situações válidas ou não, sem depender dos inputs do usuário. 
