import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

sql_update_senha_temp = 'update loja set senha_temp = %s where email = %s;'
sql_criar_loja        = 'insert into loja (nome, email, telefone, endereco, cep, senha, cta, bio, filosofia, explain, fachada, logo, s, latitude, longitude, capa, avatar, cidade, estado, schema, keywords, url_canonica, url, business) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
sql_update_loja       = 'update loja set nome = %s, email = %s, telefone = %s, endereco = %s, cep = %s, logo = %s, cta = %s, bio = %s, filosofia = %s, explaining = %s, foto_fachada = %s, latitude = %s, longitude = %s, capa = %s, avatar = %s, cidade = %s, estado = %s, schema = %s, keywords = %s, url_canonica = %s, url = %s, business = %s  where id = %s;'
sql_update_loja_senha = 'update loja set nome = %s, email = %s, telefone = %s, endereco = %s, cep = %s, senha = %s, logo = %s, cta = %s, bio = %s, filosofia = %s, explaining = %s, foto_fachada = %s, latitude = %s, longitude = %s, capa = %s, avatar = %s, cidade = %s, estado = %s, schema = %s, keywords = %s, url_canonica = %s, url = %s, business = %s  where id = %s;'
sql_login_email       = 'select * from loja where email = %s;'
sql_loja_id           = 'select * from loja where id = %s;'
sql_verifica_rec_senha= 'select email from loja where email = %s;'
sql_load_studio       = 'select * from loja where nome = %s;'
sql_criar_galeria     = 'insert into galeria (id_loja, imagem) values(%s, %s);'
sql_load_galeria      = 'select id, imagem from galeria where id_loja = %s;'
sql_remover_galeria   = 'delete from galeria where id = %s;'
sql_criar_depoimento  = 'insert into depoimentos (id_loja, imagem) values(%s, %s);'
sql_load_depoimentos  = 'select id, imagem from depoimentos where id_loja = %s;'
sql_remover_depoimento= 'delete from depoimentos where id = %s;'
sql_load_schema       = 'select schema from caixacerto.schemas;'


sql_listar_profissionais = 'select id, nome, foto, apelido from profissionais where id_loja = %s;'

def executar_sql(__sql__, params=None):

    __host__:str = os.getenv('DB_HOST',    '')
    __user__:str = os.getenv('DB_USER',    '')
    __pass__:str = os.getenv('DB_PASSWORD','')
    __name__:str = os.getenv('DB_NAME',    '')
    __char__:str = os.getenv('DB_CHARSET', '')
    
    __port__:int = int(os.getenv('DB_PORT',''))

    connection = pymysql.connect(
        host    = __host__,
        port    = __port__,
        user    = __user__,
        password= __pass__,
        database= __name__,
        charset = __char__,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:
            if params:
                cursor.execute(__sql__, params)

            else:    
                cursor.execute(__sql__)

            if not __sql__.startswith('select'):
                connection.commit()

            else:
                return cursor.fetchall()  
    finally: 
        connection.close()