''' exemplo def test_polimorfismo_preco():
    data = datetime.now()
    voos = [
        Voo("1", "A", "B", data),
        VooExecutivo("2", "A", "B", data)
    ]

    precos = [voo.calcular_preco() for voo in voos]

    assert precos == [300, 600]
'''