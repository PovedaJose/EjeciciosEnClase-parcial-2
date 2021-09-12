from datetime import date

class Empresa:
    def __init__(self, nom,ruc, tel,dir):
        self.nombre= nom
        self.ruc= ruc
        self.telefono= tel
        self.direccion= dir
    
    def mostrarEmpresa(self):
        print("Empresa: {:17} Ruc: {}".format(self.nombre, self.ruc))

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, ced, nom, dir, tel):
        self.cedula= ced
        self.nombre= nom
        self.direccion= dir
        self.telefono= tel
    
    @abstractmethod
    def getCedula(self):
        return self.cedula

    def mostrarCliente(self):
        print("Cliente: {:17} Cedula: {:17} Telefono: {}".format(self.nombre, self.cedula, self.telefono))
    
class ClienteCorporativo(Cliente):
    def __init__(self,ced, nom, dir, tel,contrato):
        super().__init__(ced, nom, dir, tel)
        self.__contrato= contrato
        
    @property 
    def contrato(self):   #getter: obtener el valor del atributo privado
        return self.__contrato
    
    @contrato.setter
    def contrato(self,value):    #setter: asigna un valor al atributo privado
        if value:
            self.__contrato= value
        else:
            self.__contrato= "Sin contrato"

    def mostrarCliente(self):
        print("Cliente: {:17} Contrato: {}".format(self.nombre, self.__contrato))

class ClientePersonal(Cliente):
    def __init__(self,ced, nom, dir, tel,promocion= True):
        super().__init__(ced, nom, dir, tel)
        self.__promocion= promocion
        
    @property 
    def promocion(self):   
        return self.__promocion
    
    def getCedula(self):
        return super().getCedula()

    def mostrarCliente(self):
        print("Cliente: {:17} Cedula:{} Promoción: {}".format(self.nombre, self.cedula, self.promocion))

class Articulo:
    secuencia=0
    iva=0.12
    def __init__(self, des,pre,sto):
        Articulo.secuencia+=1
        self.codigo= Articulo.secuencia
        self.descripcion= des
        self.precio= pre
        self.stock= sto
    
    def mostrarArticulo(self):
        print(self.codigo, self.descripcion, self.precio, self.stock)

class detVenta:
    linea=0

    def __init__(self, articulo, cantidad):
        detVenta.linea+=1
        self.lineaDetalle=detVenta.linea
        self.articulo= articulo
        self.precio= articulo.precio
        self.cantidad= cantidad
    
class cabVenta:
    def __init__(self, fac, fecha,cliente, tot=0):
        self.factura= fac
        self.fecha= fecha
        self.cliente= cliente
        self.total= tot
        self.detVen= []
    
    def agregarDetalle(self,articulo, cantidad):
        detalle= detVenta(articulo,cantidad)
        self.total+=detalle.precio*detalle.cantidad
        self.detVen.append(detalle)
    
    def mostrarVenta(self, empNombre, empRuc):
        print("Empresa: {:17} Ruc: {}" .format(empNombre, empRuc))
        print("Factura: {:17} Fecha: {}" .format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo        Precio  Cantidad  Subtotal ")
        for det in self.detVen:
            print("{:5} {:15} {} {:6} {:7}" .format(det.linea, det.articulo.descripcion, det.precio, det.cantidad, det.precio*det.cantidad))
        print("Total Venta: {:26}" .format(self.total))

# emp= Empresa("El mas Barato", "099999999", "042971234", "Juan Montalvo y Pedro Carbo")
# emp.mostrarEmpresa()
# cli1= ClienteCorporativo("09471510245","Carlos Garcia", "Cdla. Las Piñas","0988318480","#0001")
# cli1.mostrarCliente()
# cli2= ClientePersonal("09471510245","Carlos Garcia", "Cdla. Las Piñas","0988318480",True)
# print(cli2.getCedula())
# cli2.mostrarCliente()
# art1= Articulo("manzana",1,200)
# art2= Articulo("manzana",1,200)
# art1.mostrarArticulo()
# art2.mostrarArticulo()
# print(Articulo.iva)
# today= date.today()
# fecha= date(2021,8,15)
# Venta= cabVenta("F001", date.today(), cli1)
# Venta.agregarDetalle(art1,3)
# Venta.agregarDetalle(art2,5)
# Venta.mostrarVenta(emp.nombre, emp.ruc)

class InterfaceSistemaPago(ABC):
    @abstractmethod
    # este proceso hace el pago de calculo
    def pago(self):
        pass

    @abstractmethod
    def saldo(self):
        pass

class PagoTarjetaImplements(InterfaceSistemaPago):
    # este proceso hace el pago del calculo de interes de la tarjeta
    def pago(self):
        return "Pago tarjeta"
    
    def saldo(self):
        return "Saldo Tarjeta rebajado"

class ImplementsPagoContrato(InterfaceSistemaPago):
    def pago(self):
        return "Pago Contrato2"
    
    def saldo(self):
        return "Saldo Contrato rebajado"

class Vendedor:
    def __init__(self, nom):
        self.nombre= nom
    
    def moduloPago(self,contratoV):
        return contratoV.pago()

# pagoTarjeta= PagoTarjetaImplements()
# print(pagoTarjeta.pago())
# pagoContrato= ImplementsPagoContrato()
# print(pagoContrato.pago())
# ven= Vendedor("Daniel")
# print(ven.moduloPago(pagoContrato))