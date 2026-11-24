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
    mostrar_texto("Você encontra um bilhete codificado no chão: '4 - 1 - 4 - 15'.")
    mostrar_texto("Dica: A=1, B=2, C=3...")
    
    tentativas = 3
    while tentativas > 0:
        resposta = input("Decodifique os números e digite a palavra: ").upper().strip()
        if resposta == "DADO":
            print("✅ Correto! A palavra é DADO. A porta se abre.")
            return True
        else:
            tentativas -= 1
            print(f"❌ Incorreto. Tentativas restantes: {tentativas}")
    
    print("💀 Você não conseguiu abrir a porta. O ladrão escapou.")
    return False

def fase_2():
    print("\n--- FASE 2: A DEDUÇÃO ---")
    mostrar_texto("Fatos coletados:")
    print("1. Quem estava na Sala de Servidores roubou o projeto.")
    print("2. O Marcus estava comendo na Copa.")
    print("3. O Sr. Victor NÃO estava no Laboratório Principal.")
    print("4. A Dra. Elena estava numa das 3 salas (Copa, Lab, Servidores).")
    
    mostrar_texto("Analisando os fatos...", 2)
    
    resposta = input("Quem é o culpado (quem estava na Sala de Servidores)? [Elena/Marcus/Victor]: ").upper().strip()
    
    if "VICTOR" in resposta:
        print("✅ Brilhante! Por eliminação, o Victor estava na sala do crime.")
        return True
    else:
        print("❌ Dedução errada. Você acusou a pessoa errada e foi demitido.")
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
        print("✅ Isso! O relógio parado esconde o pacote.")
        return True
    else:
        print("❌ Você procurou no lugar errado e o cúmplice do Victor fugiu com o projeto.")
        return False

def jogar():
    introducao()
    if fase_1():
        if fase_2():
            if fase_3():
                print("\n🎉 PARABÉNS DETETIVE! 🎉")
                print("Você encontrou o Projeto Zero dentro do relógio e prendeu o Sr. Victor.")
                print("Caso encerrado com sucesso.")
            else:
                print("\nFIM DE JOGO - Quase lá!")
        else:
            print("\nFIM DE JOGO - O mistério permanece.")
    else:
        print("\nFIM DE JOGO - Preso na entrada.")

if __name__ == "__main__":
    jogar()
