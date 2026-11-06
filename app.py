import random
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Pandora TRPG - Simulador de Captura",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Simulador de Captura de Pandora")
st.write(
    "Configura los parámetros de tu lanzamiento para intentar atrapar al"
    " Pokémon salvaje."
)

# Entradas de datos en la interfaz web
pokemon_nombre = st.text_input(
    "Nombre del Pokémon:", value="Pokémon Salvaje"
)

# Selección del tipo de Poké Ball con sus respectivos ratios clásicos
tipo_pokeball = st.selectbox(
    "Selecciona la Poké Ball:",
    ["Poké Ball (Ratio 1.0)", "Super Ball (Ratio 1.5)", "Ultra Ball (Ratio 2.0)"],
)

# Asignar el valor numérico según la Poké Ball elegida
if "Super Ball" in tipo_pokeball:
  pokeball_ratio = 1.5
elif "Ultra Ball" in tipo_pokeball:
  pokeball_ratio = 2.0
else:
  pokeball_ratio = 1.0

pokemon_ratio = st.number_input(
    "Ratio de captura base del Pokémon (ej. 45 para difíciles, 255 para"
    " fáciles):",
    min_value=1,
    max_value=255,
    value=45,
)

estado_pokemon = st.selectbox(
    "Estado alterado del Pokémon:",
    ["Normal", "Dormido", "Congelado", "Envenenado", "Paralizado", "Quemado"],
)

# Diccionario de modificadores por estado
estado_modificador = {
    "Normal": 1.0,
    "Dormido": 2.0,
    "Congelado": 2.0,
    "Envenenado": 1.5,
    "Paralizado": 1.5,
    "Quemado": 1.5,
}.get(estado_pokemon, 1.0)

st.write("")
if st.button("🎲 ¡Intentar Captura!"):
  # Simular número de giros (0 a 3)
  giros = random.randint(0, 3)

  # Cálculo de probabilidad de captura
  probabilidad_captura = min(
      1.0,
      (pokeball_ratio * float(pokemon_ratio) * estado_modificador) / 255,
  )
  captura_exitosa = random.random() < probabilidad_captura

  if captura_exitosa:
    st.balloons()
    st.success(
        f"★ Salieron Estrellas luego de que la Poké Ball diera {giros} giro(s).\n\n"
        f"🎉 ¡Felicidades, Capturaste a {pokemon_nombre}!"
    )
  else:
    # Reacciones aleatorias al fallar
    reacciones = [
        (
            "Mucho Cuidado: Luego de escapar de la Ball, el Pokémon se lanza"
            " al ataque."
        ),
        (
            "Estás en Mala Racha: Luego de salir de la Ball, el Pokémon huye de"
            " la zona."
        ),
        (
            "Alégrate, no Todo es Malo: Luego de salir de la Ball, el Pokémon se"
            " defiende en posición de combate."
        ),
    ]
    reaccion = random.choice(reacciones)

    st.error(
        f"✖ La Poké Ball dio {giros} giro(s), pero {pokemon_nombre} escapó.\n\n"
        f"☹️ Mejor suerte la próxima vez.\n\n_{reaccion}_"
    )
