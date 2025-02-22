def main():
    from PIL import Image
    # Función para cambiar el formato de la imagen
    def cambiar_tipo_imagen(input_path, output_path, output_format):
        # Abrir la imagen
        imagen = Image.open(input_path)

        # Guardar la imagen en el nuevo formato
        imagen.save(output_path, format=output_format)

        print(f"Imagen guardada en {output_path} con el formato {output_format}")

    # Ejemplo de uso
    input_path = 'ruta/a/tu/imagen.jpg'
    output_path = 'ruta/a/tu/imagen_convertida.png'
    output_format = 'PNG'

    cambiar_tipo_imagen(input_path, output_path, output_format)

if __name__ == "__main__":
    main()