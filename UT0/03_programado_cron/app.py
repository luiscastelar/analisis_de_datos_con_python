import sys

def main():
    version = sys.version.split()[0]
    print(f"¡Hola Mundo desde Docker con Python {version}!")

if __name__ == "__main__":
    main()
