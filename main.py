import os, hashlib
algoritmos = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "sha3_256", "sha3_512", "blake2b", "blake2s"]

def hash(valor, algoritmos):
    archivo_salida = "ALGORITMS"
    for algoritmo in algoritmos:
        hash_algoritmo = hashlib.new(algoritmo)
        hash_algoritmo.update(valor.encode("utf-8"))
        archivo_salida += "\n\n{}\n{}".format(algoritmo.upper(), hash_algoritmo.hexdigest())
    return archivo_salida

def calcular_hash_archivo(filepath, algoritmos):
    archivo_salida = "ALGORITMS"
    with open(filepath, "rb") as f:
        for algoritmo in algoritmos:
            hash_algoritmo = hashlib.new(algoritmo)
            f.seek(0)
            for chunk in iter(lambda: f.read(4096), b""):
                hash_algoritmo.update(chunk)
            archivo_salida += "\n\n{}\n{}".format(algoritmo.upper(), hash_algoritmo.hexdigest())
    return archivo_salida

if int(input("Value (1) or File (2): ")) == 1:
    archivo_salida = hash(input("Value: "), algoritmos)
else:
    ruta_archivo = input("Relative Path: ")
    if os.path.isfile(ruta_archivo):
        archivo_salida = calcular_hash_archivo(ruta_archivo, algoritmos)
    else:
        print("File not found"); exit()

file = open("Hash.txt", "w")
file.write(archivo_salida); file.close()
print(os.path.abspath("Hash.txt"))

# MD5       hashlib.md5
# SHA-1     hashlib.sha1
# SHA-3     hashlib.sha3
# SHA-224   hashlib.sha224
# SHA-256   hashlib.sha256
# SHA-384   hashlib.sha384
# SHA-512   hashlib.sha512
# BLAKE2    hashlib.blake2b  //  hashlib.blake2s