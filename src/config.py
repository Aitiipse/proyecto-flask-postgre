from psycopg2 import connect


HOST= 'ec2-3-225-110-188.compute-1.amazonaws.com'
PORT= 5432
BD='d4hohg1ih0n0h9'
USUARIO='xvwvitidjigidx'
PASSWORD='9816a8fe39743364b6efc343a0268ea1f41e9d445c6f726861a1765b4815399b'

def EstablecerConexion():
    try:
        conexion=connect(host=HOST, port=PORT, database=BD, user=USUARIO, password=PASSWORD)
        return conexion
    except Exception as e:
        print(e)
        return None
    
   