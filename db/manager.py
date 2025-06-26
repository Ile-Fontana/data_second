import pandas as pd
import re 
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config


class DatabaseManager:
    def __init__(self):
        user = config('DB_USERNAME')
        password = config('DB_PASS')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')

        url =f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine (url)
        

    def save_dataframe(self,df,nombre_tabla):
       
        if not isinstance(df,pd.DataFrame):
            print(f"Tipo inválido:se esperaba un Dataframe; se recibió un {type(df)}.")
            return
        
        nombre_tabla =nombre_tabla.lower().replace('-','_').replace(' ','_')
        nombre_tabla = re.sub(r"\d+", "", nombre_tabla) 
        
        try:

            df.to_sql(nombre_tabla, con=self.engine,if_exists='replace',index=False)
            
            print(f"Datos guardados en tabla: {nombre_tabla}")

        except SQLAlchemyError as e:
            print(f"Error guardando datos:{e}")

        


    
    
