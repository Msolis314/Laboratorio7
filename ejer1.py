import argparse
import os

def arguments():
    """Funcion para resibir argumentos de la terminal
    ...
    :return: objeto con los argumentos de la terminal
    :rtype: objeto
    """
    parser= argparse.ArgumentParser(description="Informacion de un proceso")
    parser.add_argument("--id",required=True,help="Id del proceso")
    return parser.parse_args()

def main():
    """Funcion donde se toma el id y se busca la informacion usando los comandos de la terminal
    """
    args = arguments()
    id_p = args.id
    print("Nombre:") 
    os.system(f"ps -p {id_p} -o comm=")
    print( "Parent process id:")
    os.system(f" ps -p {id_p} -o pid=")
    print("Usuario propetario:") 
    os.system(f" ps -p {id_p} -o user=")
    print("Porcentaje de uso de CPU:") 
    os.system(f" ps -p {id_p} -o %cpu=")
    print("Consumo de memoria:")
    os.system(f" ps -p {id_p} -o %mem=")
    print("Estado:") 
    os.system(f" ps -p {id_p} -o stat=")
    print("Path del ejecutable:")
    os.system(f" ps -p {id_p} -o command=")

if __name__ == '__main__':
    main()
