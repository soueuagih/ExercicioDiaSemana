# ExercicioDiaSemana

## Descrição

Este projeto implementa o padrão de projeto **Strategy**, no qual cada dia da semana possui uma estratégia responsável por executar um comportamento específico.

O programa identifica o dia atual do sistema ou permite que o usuário informe manualmente um dia da semana. Com base nessa informação, uma estratégia é selecionada para apresentar uma recomendação de prioridade e uma mensagem personalizada relacionada à tarefa informada.

Para tratar dias inválidos ou sem estratégia cadastrada, foi utilizada uma estratégia padrão (`NullStrategy`), aplicando o padrão **Null Object**.
