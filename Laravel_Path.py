import os
import subprocess

def aplicar_permisos(directorio):
    if not os.path.exists(directorio):
        crear = input(f"El directorio '{directorio}' no existe. ¿Deseas crearlo? (s/n): ").lower()
        if crear == 's':
            try:
                os.makedirs(directorio)
                print(f"Directorio '{directorio}' creado exitosamente.")
            except Exception as e:
                print(f"Error al crear el directorio: {e}")
                return
        else:
            print("No se ha creado el directorio. Operación cancelada.")
            return

    chmod_valor = input("Introduce el valor de chmod (por ejemplo, 755): ")
    chown_valor = input("Introduce el usuario:grupo para chown (por ejemplo, ismael:users): ")

    try:
        subprocess.run(['chmod', chmod_valor, directorio], check=True)
        print(f"Permisos chmod {chmod_valor} aplicados a '{directorio}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al aplicar chmod: {e}")

    try:
        subprocess.run(['chown', chown_valor, directorio], check=True)
        print(f"Propietario cambiado a {chown_valor} en '{directorio}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al aplicar chown: {e}")

def main():
    while True:
        directorio = input("\nIntroduce el directorio sobre el que quieres actuar: ")
        aplicar_permisos(directorio)

        repetir = input("¿Deseas actuar sobre otro directorio? (s/n): ").lower()
        if repetir != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
