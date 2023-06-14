import argparse
import pandas as pd


# Función para desglosar cualquier columna en varias filas
def desglosar_lista(row,column):
    transformada = row[column].strip("[]").split(", ")
    titulo = row["titulo"]
    votos = row["votos"]
    votacion = row["votacion"]
    nota_media = row["nota"]
    desglosado = []
    for i in transformada:
        desglosado.append([i.strip("''"), titulo, votos, nota_media, votacion])
    return desglosado


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='decompose puntuacionesFA in subsets')
    parser.add_argument("-c",
                        "--column",
                         type = str,
                         help="base column to decompose")
    args = parser.parse_args()
    column = args.column

    # Cargamos el dataframe original
    df = pd.read_csv('../datasets/puntuacionesFA.csv')

    # Aplicar la función a cada fila del DataFrame para desglosar la columna especificada
    filas_desglosadas = df.apply(lambda row: desglosar_lista(row, column), axis=1).explode()

    # Crear un nuevo DataFrame con las filas desglosadas
    new_df = pd.DataFrame(filas_desglosadas.tolist(), columns=[column, "titulo", "votos", "votacion", "nota"])
    new_df.to_csv("./" + column + "_subset.csv", index=False)
