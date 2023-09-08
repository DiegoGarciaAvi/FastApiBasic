import os 
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

##SQLalchemy es nuestro kit de herrmanientas de SQL



sqllite_file_name="../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
## Se crea la url para la conexion a la base de datos
database_url = f"sqlite:///{os.path.join(base_dir,sqllite_file_name)}"

#Se crea un motor SQLalchemy
engine = create_engine(database_url, echo=True)

#Se inicia sesion a la base de datos
Session = sessionmaker(bind = engine)
#Sirve para declarar las clases de modelo de tablas
Base= declarative_base()