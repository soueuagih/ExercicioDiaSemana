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
