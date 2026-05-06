from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definicion del modelo
class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False, unique=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    
    def __repr__(self):
        return f"<producto(name='{self.name}', price='{self.price}', stock='{self.stock}')"

# inicializar la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactiriamente")

# Operaciones CRUD
def insert_productos():
    with app.app_context():
        # CRUD - INSERT
        # Instanciacion de Objetos de tipo User
        # Un objeto
        producto1 = Producto(name="Cafe ECCO", price=34.50, stock=70)
        # Otro objeto
        producto2 = Producto(name="Leche PIL", price=8.50, stock=120)
        producto3 = Producto(name="Galleta CREAM CRACKER", price=6.00, stock=24)
        
        # Adicion de objetos - registros en la tabla
        db.session.add(producto1)
        db.session.add(producto2)
        db.session.add(producto3)

        # Consolida los cambios en la base de datos
        db.session.commit()
        
        print("Productos insertados")

# Consultas a la Base de Datos
def query_productos():
    with app.app_context():
        # CRUD - LECTURA
        # Consultar todos los registros de una tabla
        print("Listado de Productos")
        productos = Producto.query.all()
        for item in productos:
            print(item)
        
        # CRUD - Consultas que cumplan cierta condicion
        print("Listado de registros filtrados")
        filtrados = Producto.query.filter(Producto.id>=2).all()
        for item in filtrados:
            print(item)

        # CRUD - Consulta de un solo producto
        print("Obtener un solo registro")
        user = Producto.query.filter_by(id=1).first()
        if user:
            print(user)
        else:
            print("Producto NO encontrado")

# CRUD - Actualizar
def update_producto():
    with app.app_context():
        print("\nActualizacion de un registro")
        producto = Producto.query.filter_by(id=1).first()
        if producto:
            producto.name = "Coca Cola"
            producto.price = 11.50
            producto.stock = 300
            db.session.commit()
            print("Producto actualizado: ", producto)
        else:
            print("Producto no encontrado")

# CRUD - Eliminar
def delete_producto():
    with app.app_context():
        print("\nEliminacion del Registro")
        producto = Producto.query.filter_by(id=3).first()
        if producto:
            db.session.delete(producto)
            db.session.commit()
            print("Producto Eliminado satisfactoriamente")
        else:
            print("Producto NO encontrado")
            

if __name__ == "__main__":
    init_db()
    insert_productos()
    query_productos() 
    update_producto()
    delete_producto()
    
    
    
    