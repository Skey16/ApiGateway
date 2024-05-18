def validar_producto(producto):
    if not producto.nombre:
        raise ValueError("El nombre del producto no puede estar vacío")
    if type(producto.nombre) is not str:
        raise ValueError("El nombre del producto debe ser una cadena")
    if producto.precio <= 0:
        raise ValueError("El precio del producto debe ser positivo")
    if type(producto.precio) not in [int, float]:
        raise ValueError("El precio del producto debe ser un número")
    if producto.stock < 0:
        raise ValueError("El stock del producto no puede ser negativo")
    if type(producto.stock) is not int:
        raise ValueError("El stock del producto debe ser un número entero")
