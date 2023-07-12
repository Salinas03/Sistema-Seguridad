class EquipoConectado:

    #Sobrecarga de constructores
    def __init__(self, conexion, direccion, nombre_host, identificador):
        self.conexion = conexion
        self.direccion = direccion
        self.nombre_host = nombre_host
        self.identificador = identificador
        self.seleccionado = False

    #Getters
    def get_conexion(self):
        return self.conexion
    
    def get_direccion(self):
        return self.direccion
    
    def get_nombre_host(self):
        return self.nombre_host
    
    def get_identificador(self):
        return self.identificador
    
    def get_seleccionado(self):
        return self.seleccionado

    #Setters
    def set_conexion(self, conexion):
        self.conexion = conexion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_nombre_host(self, nombre_host):
        self.nombre_host = nombre_host

    def set_identificador(self, identificador):
        self.identificador = identificador

    def set_seleccionado(self, seleccionado):
        self.seleccionado = seleccionado
