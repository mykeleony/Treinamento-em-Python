def calcular_tempo(segundos):
    # Dado o tempo em segundos de certa tarefa, imprime o tempo formatado em termos de segundos, minutos e horas.

    if segundos < 0:
        print('Entrada inválida. Por favor, insira um valor válido e tente novamente')
        return

    minutos = int(segundos/60)
    segundos = segundos-(minutos*60)
    horas = int(minutos/60)
    minutos = minutos-(horas*60)

    print(str(horas)+':'+str(minutos)+':'+str(segundos))

if __name__ == '__main__':
    calcular_tempo(3652
