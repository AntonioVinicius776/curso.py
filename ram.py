import random

def sorteio_aluno():
    alunos = [
        "jose", "ana", "pedro", "julia", "maria","fabiana"
    ]
    escolher=random.choice(alunos)
    print(f"o sortudo foi:{escolher}")

    sorteio_aluno()