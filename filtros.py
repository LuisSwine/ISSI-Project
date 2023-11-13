


def filtrar_movimientos_factura_por_cobrar(factura, movimientos):
    
    movimientos_filtados = []
    
    for movimiento in movimientos:
        if movimiento.fecha >= factura.fecha_emision and movimiento.monto > 0.01:
            movimientos_filtados.append(movimiento)
            
    return movimientos_filtados
    