            #sueldo base/ dias calculos/horas de trabajos normales*pago por horas*horas extras.
            valorHorasextras = sueldo/ 14/8*3*valorHorasextras



class PagoSobretiempo():   
    def __init__(self, horasexT, pagoH):
        self.horasextrasTrabajadas = horasexT
        self.pagoHoraextras = pagoH
        
    def calculoPago(self):
        cal = self.horasextrasTrabajadas * self.pagoHoraextras
        return cal