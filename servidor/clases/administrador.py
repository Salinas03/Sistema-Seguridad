class Administrador:
    def __init__(self, id_admin, nombre_admin, apellido_admin, telefono_admin, correo_admin, contrasena_admin, rol_propietario, numero_serie):
        self.id_admin = id_admin
        self.nombre_admin = nombre_admin
        self.apellido_admin = apellido_admin
        self.telefono_admin = telefono_admin
        self.correo_admin = correo_admin
        self.contrasena_admin = contrasena_admin
        self.rol_propietario = rol_propietario
        self.numero_serie = numero_serie

    def get_id_admin(self):
        return self.id_admin
    
    def get_nombre_admin(self):
        return self.nombre_admin
    
    def get_apellido_admin(self):
        return self.apellido_admin
    
    def get_telefono_admin(self):
        return self.telefono_admin
    
    def get_correo_admin(self):
        return self.correo_admin
    
    def get_contrasena_admin(self):
        return self.contrasena_admin
    
    def get_id_propietario(self):
        return self.rol_propietario
    
    def get_numero_serie(self):
        return self.numero_serie