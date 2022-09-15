#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

from main import Aluno, Nota


aluno = Aluno('Henrique', 17, 2, "noturno")
nota= Nota(2.5, 8, 8.5)

aluno.mostrarAluno()
aluno.trocarIdade(16)
aluno.trocarNome("João Carlos")
aluno.mostrarAluno()
nota.mostrarNotas()
nota.resultado()
