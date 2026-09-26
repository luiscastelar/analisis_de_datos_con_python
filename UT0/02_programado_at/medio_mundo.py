import sys

def main():
    version = sys.version.split()[0]
    print(f"Esto es una prueba de fallo")
    sys.exit(1)

if __name__ == "__main__":
    main()
