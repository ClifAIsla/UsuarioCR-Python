from mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id = data['id'],
        self.nombre = data['first_name']
        self.apellido = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('usuarioscr').query_db(query)
        usuarios =[]
        for usuario in results:
            usuarios.append( usuario ) 
        return usuarios
    
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, updated_at, created_at) VALUES ( %(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('usuarioscr').query_db(query, data)