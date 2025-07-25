def limpiar_y_validar_hex(hex_str):
    hex_str = hex_str.lower().replace("0x", "").strip()
    if len(hex_str) != 8:
        raise ValueError(f"'{hex_str}' is not an hexadecimal 4 byte value.")
    return hex_str

def invertir_endianess(hex_str):
    # hex_str debe tener 8 caracteres → 4 bytes
    return ''.join([hex_str[i:i+2] for i in range(0, 8, 2)][::-1])

def bitwise_not_bytes(hex_str):
    # Convertir en bytes
    bytes_list = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]
    # Aplicar ~b & 0xFF
    return [~b & 0xFF for b in bytes_list]

def bytes_a_ascii(byte_list):
    return ''.join(chr(b) if 32 <= b <= 126 else '.' for b in byte_list)

def procesar(valores_hex, cambiar_endianess):
    resultado_bytes = []

    for valor in valores_hex:
        try:
            limpio = limpiar_y_validar_hex(valor)
            if cambiar_endianess:
                limpio = invertir_endianess(limpio)
            bytes_not = bitwise_not_bytes(limpio)
            resultado_bytes.extend(bytes_not)
        except ValueError as e:
            print(f"Error with the value '{valor}': {e}")
            continue

    ascii_resultado = bytes_a_ascii(resultado_bytes)
    print("\nASCII result:")
    print(f"\033[1m{ascii_resultado}\033[0m")

if __name__ == "__main__":
    entrada = input("Introduce your 4 byte hexadecimal values, separated by spaces (they may have 0x):\n> ")
    valores = entrada.replace(",", " ").split()

    print("\n¿Do you want to change the endianess?")
    print("1. Yes (invert the position of every byte)")
    print("2. No")
    opcion = input("Select 1 or 2: ").strip()

    if opcion not in ("1", "2"):
        print("Invalid option.")
    else:
        cambiar = opcion == "1"
        procesar(valores, cambiar)


# Prueba: 0xae98c9b3 0x959c899b 0x86c7b1cd 0xadca9ea5 0xbd978b94 0xa8b2aacf 0x8f8590b9 0xac8ca7cb





