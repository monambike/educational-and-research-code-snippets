print("Informe à seguir, produtos com quantidade e valor unitário para que seja computado o valor de compra por produto e valor total")

buy_value_total = 0
buy_value_product = 0
buy_quantity_product = 0

input_amount = input("Informe quantos produtos você gostaria de inserir: ")
amount = int(input_amount)

index_product = 1
products = ""

while index_product < amount:
    prefix = f"({index_product}º Produto)"

    value_unit = input(f"{prefix} Informe o valor unitário: ")
    value_unit = float(value_unit)

    quantity = input(f"{prefix} Informe a quantidade: ")
    quantity = int(quantity)

    buy_value_product = value_unit * quantity
    buy_value_total += buy_value_product

    products += f"""
--- TELA FINAL ---
{products}

VALOR TOTAL {buy_value_total}
"""
