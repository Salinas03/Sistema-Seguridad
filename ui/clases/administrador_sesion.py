class AdministradorSesion:
    def __init__(self, data_admin):
        self.id_admin = data_admin[0]
        self.nombre_admin = data_admin[1]
        self.apellido_admin = data_admin[2]
        self.tel_admin = data_admin[3]
        self.correo_admin = data_admin[4]

    def get_id_admin(self):
        return self.id_admin

    def get_nombre_admin(self):
        return self.nombre_admin
    
    def get_apellido_admin(self):
        return self.apellido_admin
    
    def get_tel_admin(self):
        return self.tel_admin
    
    def get_correo_admin(self):
        return self.correo_admin

    def actualizar_informacion_admin(self, id_admin, nombre_admin, apellido_admin, tel_admin, correo_admin):
        self.id_admin = id_admin
        self.nombre_admin = nombre_admin
        self.apellido_admin = apellido_admin
        self.tel_admin = tel_admin
        self.correo_admin = correo_admin