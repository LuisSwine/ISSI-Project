class Movimiento:
    id_transaccion = None
    fecha = None
    concepto = None
    monto = None
    moneda = None
    referencia = None
    clave_rastreo = None
    tipo_movimiento = None
    banco_emisor = None
    cuenta_emisor = None
    nombre_emisor = None
    rfc_emisor = None
    banco_receptor = None
    cuenta_receptor = None
    nombre_receptor = None
    rfc_receptor = None
    comprobante = None
    
    #Declaramos el constructor de la clase
    def __init__(self, id_transaccion, fecha, concepto, monto, moneda, referencia, clave_rastreo, tipo_movimiento, banco_emisor, cuenta_emisor, nombre_emisor, rfc_emisor, banco_receptor, cuenta_receptor, nombre_receptor, rfc_receptor, comprobante):
        self.id_transaccion = id_transaccion
        self.fecha = fecha
        self.concepto = concepto
        self.monto = monto
        self.moneda = moneda
        self.referencia = referencia
        self.clave_rastreo = clave_rastreo
        self.tipo_movimiento = tipo_movimiento
        self.banco_emisor = banco_emisor
        self.cuenta_emisor = cuenta_emisor
        self.nombre_emisor = nombre_emisor
        self.rfc_emisor = rfc_emisor
        self.banco_receptor = banco_receptor
        self.cuenta_receptor = cuenta_receptor
        self.nombre_receptor = nombre_receptor
        self.rfc_receptor = rfc_receptor
        self.comprobante = comprobante
        pass
    
    
    