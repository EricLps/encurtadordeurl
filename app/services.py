import string
import random

def gerar_codigo_curto(tamanho=6):
    
    caracteres = string.ascii_letters + string.digits

    return ''.join(random.choice(caracteres) for _ in range(tamanho))