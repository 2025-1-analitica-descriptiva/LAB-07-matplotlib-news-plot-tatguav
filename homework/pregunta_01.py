"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Leer los datos del archivo CSV
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Definir colores para cada categoría
    colors = {
        "Television": "#FF69B4",
        "Newspaper": "#C8A2C8",
        "Internet": "#87CEFA",
        "Radio": "#D3D3D3",
    }

    # Z-order define el orden de apilamiento (quién va encima)
    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,  # Queremos que Internet esté encima
        "Radio": 1,
    }

    # Grosor de las líneas
    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    # Crear el gráfico
    plt.figure(figsize=(8, 6))

    # Dibujar las líneas
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    # Configurar el título
    plt.title("How people get their news", fontsize=16, fontweight='bold')

    # Remover los bordes no necesarios y el eje Y
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    # Agregar etiquetas al inicio y fin de cada línea
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        # Punto y texto al inicio
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )
        plt.text(
            first_year - 0.3,
            df[col][first_year],
            f"{col} {df[col][first_year]}%",
            ha='right',
            va='center',
            color=colors[col],
            fontsize=9
        )

        # Punto y texto al final
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )
        plt.text(
            last_year + 0.3,
            df[col][last_year],
            f"{df[col][last_year]}%",
            ha='left',
            va='center',
            color=colors[col],
            fontsize=9
        )

    # Ajustar etiquetas del eje X
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )

    # Ajustar espaciado y guardar el gráfico
    plt.tight_layout()
    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")

pregunta_01()