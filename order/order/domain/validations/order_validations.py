def validar_orden(orden):
    if orden.total <= 0:
        raise ValueError("El total del pedido debe ser positivo.")
    if orden.estado not in ['Pagado', 'Creado', 'Enviado']:
        raise ValueError("Estatus de pedido no válido")
    if not orden.productos_orden:
        raise ValueError("El pedido debe tener al menos un producto.")
