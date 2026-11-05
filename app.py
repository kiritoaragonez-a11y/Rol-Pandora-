import random
import streamlit as st

st.set_page_config(page_title="Pandora TRPG", page_icon="⛺", layout="centered")

st.title("⛺ Pandora TRPG - Motor de Automatización")
st.write("Bienvenido al sistema oficial de gestión de expediciones.")

menu = st.sidebar.selectbox(
    "Menú Principal", ["Exploración y Encuentros", "Calculadora de Captura"]
)

if menu == "Exploración y Encuentros":
  st.header("🗺️ Expedición en el Territorio")

  base_seleccionada = st.selectbox(
      "Selecciona tu Base de partida / Zona:",
      [
          "Base del Bosque (Bosque Místico)",
          "Base de la Ladera (Cavernas)",
          "Base de las Montañas (Cumbre)",
          "Base de la Playa (Costa)",
          "Base del Pantano (Tierras Sombrías)",
          "Base de la Tundra (Vórtice Blanco)",
          "Base de la Isla Volcánica (Umbral de Fuego)",
      ],
  )

  fauna_por_zona = {
      "Base del Bosque (Bosque Místico)": [
          "Sobble",
          "Shinx",
          "Bounsweet",
          "Nincada",
          "Typhlosion (Forma Hisui / Alfa)",
      ],
      "Base de la Ladera (Cavernas)": ["Geodude", "Rhyhorn", "Sandshrew"],
      "Base de las Montañas (Cumbre)": [
          "Geodude (Anómalo)",
          "Chansey",
          "Rookidee",
      ],
      "Base de la Playa (Costa)": ["Machamp (Alfa)", "Zubat", "Rockruff"],
      "Base del Pantano (Tierras Sombrías)": [
          "Graveler",
          "Hippopotas",
          "Croagunk",
      ],
      "Base de la Tundra (Vórtice Blanco)": ["Swinub", "Snorunt", "Bergmite"],
      "Base de la Isla Volcánica (Umbral de Fuego)": [
          "Charmander",
          "Magby",
          "Houndour",
      ],
  }

  if st.button("🔍 ¡Explorar y Buscar Pokémon!"):
    pokemon_encontrado = random.choice(fauna_por_zona[base_seleccionada])
    nivel = 5
    iv_ps = random.randint(0, 31)
    iv_ataque = random.randint(0, 31)
    iv_defensa = random.randint(0, 31)
    iv_atq_esp = random.randint(0, 31)
    iv_def_esp = random.randint(0, 31)
    iv_velocidad = random.randint(0, 31)

    st.success(f"¡Un **{pokemon_encontrado}** salvaje ha aparecido!")
    st.markdown("### 📊 Datos del Pokémon:")
    st.write(f"- **Nivel:** {nivel}")
    st.write(
        "- **IVs:** PS: "
        f" {iv_ps} | Atq: {iv_ataque} | Def: {iv_defensa} | Atq.Esp:"
        f" {iv_atq_esp} | Def.Esp: {iv_def_esp} | Vel: {iv_velocidad}"
    )

elif menu == "Calculadora de Captura":
  st.header("🎯 Simulador de Captura")

  pokeball = st.selectbox(
      "Elige tu Pokéball:", ["Pokéball estándar", "Superball", "Ultraball"]
  )
  salud_pokemon = st.slider(
      "Porcentaje de salud restante del Pokémon (%)", 1, 100, 50
  )

  if st.button("🎲 ¡Lanzar Pokéball!"):
    probabilidad_exito = (100 - salud_pokemon) + (
        20
        if pokeball == "Superball"
        else (40 if pokeball == "Ultraball" else 0)
    )
    tirada = random.randint(1, 100)
    minimo_exito = max(probabilidad_exito, 25)

    if tirada <= minimo_exito:
      st.balloons()
      st.success("🎉 ¡Felicidades! ¡Has atrapado al Pokémon!")
    else:
      st.error("💥 ¡El Pokémon se ha liberado y ha escapado!")
