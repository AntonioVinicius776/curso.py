import time 
def lembrete_atividade(intervalo_minutos=1):
    contador =1 
    while True:
        print(f"/n tempo encerrado(lembrete{contador})")
        contador+=1
        time.sleep(intervalo_minutos*60)
        lembrete_atividade()