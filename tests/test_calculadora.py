def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser cero. Proporciona distinto de 0.")
    return a / b


def test_funcion_nueva():
    # Este test falla a propósito para simular detección por CI
    from calculadora import funcion_nueva_con_bug
    # Si CI hace bien su trabajo, esto nunca llega a producción
    resultado = funcion_nueva_con_bug()
    assert resultado is not None
