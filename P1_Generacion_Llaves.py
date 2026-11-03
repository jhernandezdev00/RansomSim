import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

ruta_actual = os.path.dirname(os.path.abspath(__file__))

carpeta_destino = os.path.join(ruta_actual, "Llaves_Criptograficas")

os.makedirs(carpeta_destino, exist_ok=True)

llave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
llave_publica = llave_privada.public_key()

ruta_privada = os.path.join(carpeta_destino, "llave_privada.pem")
ruta_publica = os.path.join(carpeta_destino, "llave_publica.pem")

with open(ruta_privada, "wb") as f:
    f.write(llave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open(ruta_publica, "wb") as f:
    f.write(llave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print(f"Llaves generadas con éxito. Ruta completa: {carpeta_destino}")