from abc import ABC, abstractmethod
from datetime import datetime


class DayStrategy(ABC):
    @abstractmethod
    def execute(self, user, info):
        pass


class MondayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: segunda-feira")
        print("Prioridade: ALTA")
        print(f'Mensagem: {user}, organize suas prioridades e foque na tarefa "{info}".')


class TuesdayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: terça-feira")
        print("Prioridade: ALTA")
        print(f'Mensagem: {user}, avance nas tarefas pendentes, especialmente em "{info}".')


class WednesdayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: quarta-feira")
        print("Prioridade: MÉDIA")
        print(f'Mensagem: Dia de revisão: verifique o andamento da atividade "{info}".')


class ThursdayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: quinta-feira")
        print("Prioridade: MÉDIA")
        print(f'Mensagem: {user}, colabore com alguém da equipe para evoluir em "{info}".')


class FridayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: sexta-feira")
        print("Prioridade: MÉDIA")
        print(f'Mensagem: {user}, registre o que foi concluído na tarefa "{info}".')


class SaturdayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: sábado")
        print("Prioridade: BAIXA")
        print(f'Mensagem: {user}, realize estudo livre ou descanse após trabalhar em "{info}".')


class SundayStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: domingo")
        print("Prioridade: BAIXA")
        print(f'Mensagem: {user}, planeje a próxima semana considerando "{info}".')


class NullStrategy(DayStrategy):
    def execute(self, user, info):
        print("Dia consultado: inválido ou sem estratégia associada")
        print("Prioridade: BAIXA")
        print("Mensagem: Nenhuma estratégia disponível para o dia informado.")
