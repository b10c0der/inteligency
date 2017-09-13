# author cadu
import random
cpu = random.randint(0,9)
player = int(input("Coloca um número entre 0 e 9 e tenta ganhar de mim: "))

if player > 9:
   print("\033[1;33mVocê sabe que não pode botar números maiores que 9 né animal !\033[m")
else:
    if player == cpu:
        print("\033[32mVocê ganhou cara\033[m")
    else:
        print("\033[31mNão foi dessa vez cara, eu pensei no número {} e não no {}\033[m".format(cpu,player))
