import random
import string


quantidadeDeCaractere = input("Quantidade de caracteres (recomendado minimo 16): ")



chars = string.ascii_letters + string.digits + '!@#$%&*()-=+[],.;:<>|\""''}{'

rnd = random.SystemRandom()

senha = ''.join(rnd.choice(chars) for i in range(int(quantidadeDeCaractere)))

print('Senha: }' + senha)



