WARRIOR_HP = 100
WARRIOR_DMG = 20
DRAGON_HP = 150
DRAGON_DMG = 15

print("Batalha com o dragão!")
print("1 - Atacar / 2 - Defender")

while DRAGON_HP > 0 or WARRIOR_HP > 0:
    print(f"Guerreiro: {WARRIOR_HP} / Dragão: {DRAGON_HP}")

    input_option = input("Informe se você deseja atacar ou defender: ")
    int_option = int(input_option)

    if int_option == 1:
        DRAGON_HP -= WARRIOR_DMG
        WARRIOR_HP -= DRAGON_DMG
    if int_option == 2:
        DRAGON_DMG /= 2

    if DRAGON_HP <= 0:
        print("VITÓRIA! O Dragão foi derrotado e o tesouro é seu!")
        break
    elif WARRIOR_HP <= 0:
        print("GAME OVER! Você foi derrotado pelo Dragão.")
        break
