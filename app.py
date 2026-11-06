import random
import streamlit as st

# Configuración general de la página y diseño
st.set_page_config(
    page_title="Pandora - Sistema de Gestión TRPG",
    page_icon="⛺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Estilos CSS personalizados para mejorar el diseño
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #ff2121;
        color: white;
    }
    .card-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1e2530;
        border: 1px solid #2f3742;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Encabezado principal con estilo de tarjeta
st.markdown(
    """
    <div class="card-box" style="text-align: center;">
        <h1>⛺ PANDORA TRPG</h1>
        <p style="color: #a3afbb;">Sistema Automatizado de Expediciones, Encuentros y Capturas</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Menú lateral estilizado
menu = st.sidebar.selectbox(
    "🧭 Menú de Navegación",
    ["🗺️ Exploración y Encuentros", "🎯 Simulador de Captura"],
)

# ==========================================
# MÓDULO 1: EXPLORACIÓN Y ENCUENTROS
# ==========================================
if menu == "🗺️ Exploración y Encuentros":
  st.markdown("### 🌲 Zona de Expedición")
  st.write(
      "Selecciona tu base de partida en las regiones de Pandora para buscar"
      " fauna salvaje y anomalías."
  )

  base_seleccionada = st.selectbox(
      "Elige tu Base de operaciones:",
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

  st.write("")
  if st.button("🔍 Iniciar Exploración"):
    pokemon_encontrado = random.choice(fauna_por_zona[base_seleccionada])
    nivel = random.randint(3, 8)

    iv_ps = random.randint(0, 31)
    iv_ataque = random.randint(0, 31)
    iv_defensa = random.randint(0, 31)
    iv_atq_esp = random.randint(0, 31)
    iv_def_esp = random.randint(0, 31)
    iv_velocidad = random.randint(0, 31)

    st.markdown(
        f"""
        <div class="card-box">
            <h3 style="color: #4CAF50; margin-top: 0;">¡Encuentro Salvaje!</h3>
            <p>Has encontrado un <strong>{pokemon_encontrado}</strong>.</p>
            <hr style="border-color: #2f3742;">
            <h4>📊 Estadísticas Base:</h4>
            <ul>
                <li><strong>Nivel:</strong> {nivel}</li>
                <li><strong>IVs (PS / Atq / Def):</strong> {iv_ps} / {iv_ataque} / {iv_defensa}</li>
                <li><strong>IVs (Atq.Esp / Def.Esp / Vel):</strong> {iv_atq_esp} / {iv_def_esp} / {iv_velocidad}</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info(
        "💡 *Copia los datos de arriba para reportar tu hallazgo en el grupo de"
        " WhatsApp.*"
    )

# ==========================================
# MÓDULO 2: CALCULADORA DE CAPTURA
# ==========================================
elif menu == "🎯 Simulador de Captura":
  st.markdown("### 🛑 Intentar Captura de Pokémon")
  st.write(
      "Ajusta los parámetros de tu lanzamiento para calcular el resultado de la"
      " captura."
  )

  pokeball = st.selectbox(
      "Selecciona la Pokéball a utilizar:",
      ["Pokéball estándar", "Superball", "Ultraball"],
  )
  salud_pokemon = st.slider(
      "Salud restante estimada del Pokémon (%)", 1, 100, 50
  )

  st.write("")
  if st.button("🎲 ¡Lanzar Pokéball!"):
    bonificador = (
        0
        if pokeball == "Pokéball estándar"
        else (20 if pokeball == "Superball" else 40)
    )
    probabilidad_exito = (100 - salud_pokemon) + bonificador
    tirada = random.randint(1, 100)
    minimo_exito = max(probabilidad_exito, 20)

    if tirada <= minimo_exito:
      st.balloons()
      st.success(
          "🎉 ¡Éxito absoluto! La criatura ha sido atrapada y registrada en"
          " tu equipo."
      )
    else:
      # Si falla la captura, elegimos de forma aleatoria su reacción de escape
      reaccion_escape = random.choice(
          [
              (
                  "⚔️ ¡El Pokémon se ha liberado y furioso **se lanza al"
                  " ataque** contra ti!"
              ),
              (
                  "👀 ¡El Pokémon se libera de la Pokéball, pero se queda"
                  " estático, **observándote fijamente** desde la distancia..."
              ),
              (
                  "💨 ¡El Pokémon logra zafarse con éxito y **huye a toda"
                  " velocidad** perdiéndose entre la maleza!"
              ),
          ]
      )

      st.error(
          "💥 ¡El Pokémon se ha liberado en el último segundo!\n\n"
          f"{reaccion_escape}"
      )
