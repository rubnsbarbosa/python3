def header(f):
    def wrapper(*args, **kwargs):
        print("### Bem Vindo ###")
        return f(*args, *kwargs)
    return wrapper


@header
def produto(nome):
    print(f"Produto {nome} - R$ 2k")

produto("Cadeira Gamer")
produto("Teclado Mecanico")