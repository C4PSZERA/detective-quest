import time

def mostrar_texto(texto, atraso=1.5):
    print(texto)
    time.sleep(atraso)

def introducao():
    print("\n🕵️‍♂️ BEM-VINDO AO DETECTIVE QUEST: O CASO DO PROJETO ZERO 🕵️‍♀️")
    print("="*60)
    mostrar_texto("Você é um detetive de elite contratado pela TechCorp.")
    mostrar_texto("O protótipo 'Projeto Zero' foi roubado ontem à noite.")
    mostrar_texto("A sua missão: Encontrar o culpado e recuperar o projeto.")
    print("="*60)

def fase_1():
    print("\n--- FASE 1: O CÓDIGO DA PORTA ---")
    mostrar_texto("Encontra um bilhete codificado no chão: '4 - 1 - 4 - 15'.")
    mostrar_texto("Dica: A=1, B=2, C=3...")
    
    tentativas = 3
    while tentativas > 0:
        resposta = input("Descodifique os números e digite a palavra: ").upper().strip()
        if resposta == "DADO":
            print("✅ Correto! A palavra é DADO. A porta abre-se.")
            return True
        else:
            tentativas -= 1
            print(f"❌ Incorreto. Tentativas restantes: {tentativas}")
    
    print("💀 Falhou em abrir a porta. O ladrão escapou.")
    return False

def fase_2():
    print("\n--- FASE 2: A DEDUÇÃO ---")
    mostrar_texto("Factos recolhidos:")
    print("1. Quem estava na Sala de Servidores roubou o projeto.")
    print("2. O Marcus estava a comer na Copa.")
    print("3. O Sr. Victor NÃO estava no Laboratório Principal.")
    print("4. A Dra. Elena estava numa das 3 salas (Copa, Lab, Servidores).")
    
    mostrar_texto("Analisando os factos...", 2)
    
    resposta = input("Quem é o culpado (quem estava na Sala de Servidores)? [Elena/Marcus/Victor]: ").upper().strip()
    
    if "VICTOR" in resposta:
        print("✅ Brilhante! Por eliminação, o Victor estava na sala do crime.")
        return True
    else:
        print("❌ Dedução errada. Acusou a pessoa errada e foi despedido.")
        return False

def fase_3():
    print("\n--- FASE 3: O ESCONDERIJO ---")
    mostrar_texto("Email recuperado do Victor: 'O pacote está onde o tempo para.'")
    print("Opções no saguão:")
    print("A) Estátua de bronze")
    print("B) Quadro abstrato")
    print("C) Relógio antigo quebrado")
    
    resposta = input("Onde está o projeto? [A/B/C]: ").upper().strip()
    
    if resposta == "C":
        return True
    else:
        print("❌ Procurou no sítio errado e o cúmplice do Victor fugiu com o projeto.")
        return False

def jogar():
    introducao()
    if fase_1():
        if fase_2():
            if fase_3():
                print("\n🎉 PARABÉNS DETETIVE! 🎉")
                print("Encontrou o Projeto Zero dentro do relógio e prendeu o Sr. Victor.")
                print("Caso Encerrado com Sucesso.")
            else:
                print("\nFIM DE JOGO - Quase conseguiu!")
        else:
            print("\nFIM DE JOGO - O mistério permanece.")
    else:
        print("\nFIM DE JOGO - Preso na entrada.")

if __name__ == "__main__":
    jogar()
