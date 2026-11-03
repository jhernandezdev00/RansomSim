from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from Config import ARCHIVO_PRIV_LLAVE, ARCHIVO_SALIDA_KEY, ARCHIVO_KEY_RESCATE

def obtener_solucion():
    with open(ARCHIVO_PRIV_LLAVE, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(ARCHIVO_SALIDA_KEY, "rb") as f:
        contenido_bin = f.read()

    clave_original = private_key.decrypt(
        contenido_bin,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None
        )
    )

    print(f"\nLLAVE RECUPERADA: {clave_original.decode()}")

    with open(ARCHIVO_KEY_RESCATE, "w") as f:
        f.write(clave_original.decode())

if __name__ == "__main__":
    obtener_solucion()