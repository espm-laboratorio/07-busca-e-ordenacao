import util
from random import randint

lista = [randint(1, 500) for _ in range(1000000)]
print(util.bolha(lista))
