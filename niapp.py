import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Portafolio de Economía Internacional", layout="wide")

# Título Principal
st.title("🏛️ Portafolio de Economía Internacional para los Negocios")
st.markdown("---")

# Navegación Lateral
menu = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Estrategias de Negociación (25 Técnicas)", "Indicadores y Cálculos Macroeconómicos"]
)

if menu == "Estrategias de Negociación (25 Técnicas)":
    st.header("🤝 Diccionario Táctico de Negociación")
    st.info("Inspirado en el análisis de 'The Phoenician Scheme' y fundamentos de diplomacia comercial.")

    tecnicas = [
        {"Nombre": "Asimetría de Información", "Uso": "Controlar el flujo de datos para que la contraparte dependa de tu versión.", "Guion": "Según nuestros informes exclusivos de infraestructura, el costo del acero subirá un 20%; basándonos en esto..."},
        {"Nombre": "Hecho Consumado (Fait Accompli)", "Uso": "Actuar antes de negociar para dejar a la otra parte sin opciones.", "Guion": "Los cimientos del puerto ya están colados; ahora discutamos cómo financiar el resto."},
        {"Nombre": "Anclaje (Anchoring)", "Uso": "Fijar un precio inicial extremo.", "Guion": "Nuestra tarifa base por el proyecto Excalibur es de 500 millones (sabiendo que el valor real es 300)."},
        {"Nombre": "Negociación Coercitiva", "Uso": "Usar la dependencia del otro.", "Guion": "Si no aceptan estas condiciones laborales, la concesión del túnel pasará a Sacramento mañana mismo."},
        {"Nombre": "Cortesía Innecesaria", "Uso": "Generar deuda moral mediante hospitalidad.", "Guion": "Después de esta excelente cena en honor a su delegación, estoy seguro de que revisarán el anexo B con ojos más amigables."},
        {"Nombre": "Vinculación (Linkage)", "Uso": "Condicionar un punto a cambio de otro ajeno.", "Guion": "Aceptamos bajar el arancel al vino si nos otorgan el contrato de las turbinas eléctricas."},
        {"Nombre": "MAAN (BATNA)", "Uso": "Tener un plan B sólido.", "Guion": "Si no llegamos a un acuerdo, ya tenemos una oferta similar de la competencia lista para firmar."},
        {"Nombre": "ZOPA", "Uso": "Identificar el rango donde ambos ganan.", "Guion": "Sabemos que su máximo es X y nuestro mínimo es Y; movámonos en ese rango."},
        {"Nombre": "La Retirada Estudiada", "Uso": "Demostrar disposición a abandonar la mesa.", "Guion": "Lamentablemente, estos términos no son viables para nosotros. Gracias por su tiempo. (Se levanta)."},
        {"Nombre": "Autoridad Limitada", "Uso": "Ganar tiempo o evitar ceder.", "Guion": "Me gustaría aceptar, pero mi junta directiva en Fenicia debe aprobar cualquier cambio mayor a este contrato."},
        {"Nombre": "El Flinch", "Uso": "Reacción física de asombro ante una oferta.", "Guion": "(Gesto de sorpresa) ¿Ese es el precio? Me temo que estamos muy lejos de lo que esperábamos."},
        {"Nombre": "Silencio Estratégico", "Uso": "Forzar al otro a hablar por incomodidad.", "Guion": "(Después de la oferta del otro, mantener contacto visual en silencio por 10 segundos)."},
        {"Nombre": "Policía Bueno / Policía Malo", "Uso": "Alternar presión y empatía.", "Guion": "Mi socio es inflexible, pero si me ayudan con el plazo, yo puedo convencerlo de bajar el precio."},
        {"Nombre": "El Espejo (Mirroring)", "Uso": "Repetir palabras finales para extraer información.", "Guion": "—¿El costo de los remaches es demasiado alto? —¿Demasiado alto?"},
        {"Nombre": "El Enmarcado (Framing)", "Uso": "Presentar datos como ganancia, no pérdida.", "Guion": "No estamos subiendo el precio, estamos asegurando la calidad que evitará multas futuras."},
        {"Nombre": "Psicología Inversa", "Uso": "Pedir lo contrario a lo deseado.", "Guion": "Por favor, no me obliguen a aceptar el pago en diamantes, prefiero la moneda local (sabiendo que quieres diamantes)."},
        {"Nombre": "Técnica del Salami", "Uso": "Concesiones pequeñas una a una.", "Guion": "Primero acordemos el horario, luego el transporte, luego el seguro..."},
        {"Nombre": "El Mordisqueo (Nibbling)", "Uso": "Extra de último minuto.", "Guion": "Todo firmado. Por cierto, ¿podrían incluir el transporte al puerto sin costo extra?"},
        {"Nombre": "El Krunch", "Uso": "Obligar a mejorar la oferta sin contraofertar.", "Guion": "He visto su propuesta, pero honestamente... tienen que hacerlo mejor que eso."},
        {"Nombre": "El Bogey", "Uso": "Fingir que algo irrelevante es vital.", "Guion": "No puedo ceder en el color de los planos; es política interna. (Luego lo cedes por un descuento real)."},
        {"Nombre": "El Señuelo (Decoy)", "Uso": "Opción mala para resaltar la buena.", "Guion": "El plan C es carísimo y lento. El plan A es eficiente. ¿Cuál prefieren?"},
        {"Nombre": "Inundación de Datos", "Uso": "Confundir con tecnicismos.", "Guion": "Como verán en los 40 anexos de la auditoría técnica y los 15 manuales de ingeniería..."},
        {"Nombre": "Oferta Explosiva", "Uso": "Presión temporal extrema.", "Guion": "Este precio solo es válido hasta que termine esta llamada. Mañana será otro."},
        {"Nombre": "Dividir la Diferencia", "Uso": "Ir al punto medio (favorable a ti).", "Guion": "Ustedes dicen 100, yo digo 80. Quedemos en 90 y cerremos esto hoy."},
        {"Nombre": "Red Herring", "Uso": "Distraer con un tema falso.", "Guion": "Hablemos de la estética de los túneles (mientras ocultas el problema de la deuda)."}
    ]

    for t in tecnicas:
        with st.expander(f"🔹 {t['Nombre']}"):
            st.write(f"**Uso Profesional:** {t['Uso']}")
            st.code(f"Guion sugerido: '{t['Guion']}'", language="markdown")

elif menu == "Indicadores y Cálculos Macroeconómicos":
    st.header("📊 Calculadora de Indicadores Macroeconómicos")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Producción (PIB)", "Precios e Inflación", "Finanzas y Cambio", "Comercio e Inversión"])

    with tab1:
        st.subheader("Fórmulas del Producto Interno Bruto (PIB)")
        st.latex(r"PIB_{Gasto} = C + I + G + (X - M)")
        st.latex(r"PIB_{Renta} = Salarios + Intereses + Alquileres + Ganancias")
        st.latex(r"PIB_{Valor Agregado} = \sum (V_{Final} - V_{Intermedio})")
        st.markdown("---")
        st.latex(r"PIB_{PerCapita} = \frac{PIB}{Población}")
        st.latex(r"Deflactor_{PIB} = \frac{PIB_{Nominal}}{PIB_{Real}} \times 100")

    with tab2:
        st.subheader("Inflación y Poder Adquisitivo")
        st.latex(r"IPC = \frac{\text{Costo Canasta Año Actual}}{\text{Costo Canasta Año Base}} \times 100")
        st.latex(r"Inflación = \frac{IPC_{t} - IPC_{t-1}}{IPC_{t-1}} \times 100")
        st.latex(r"Poder Adquisitivo = \frac{Salario}{IPC}")

    with tab3:
        st.subheader("Tipos de Cambio e Intereses")
        st.write("**Tipos de Cambio:**")
        st.latex(r"E_{Real} = E_{Nominal} \times \frac{P_{ext}}{P_{int}}")
        st.latex(r"E_{Cruzado} (A/C) = E(A/B) \times E(B/C)")
        st.write("**Intereses:**")
        st.latex(r"I_{Simple} = P \times i \times n")
        st.latex(r"A = P(1 + i)^n \text{ (Compuesto)}")
        st.latex(r"i_{Real} \approx i_{Nominal} - \text{Inflación}")

    with tab4:
        st.subheader("Comercio Exterior e Inversión")
        st.write("**Elasticidades:**")
        st.latex(r"\epsilon_{X, M} = \frac{\% \Delta Cantidad}{\% \Delta Precio}")
        st.write("**Inversión:**")
        st.latex(r"ROI = \frac{\text{Ganancia} - \text{Inversión}}{\text{Inversión}} \times 100")
        st.write("**Depreciación Lineal:**")
        st.latex(r"D = \frac{V_{Inicial} - V_{Residual}}{Vida Útil}")

st.sidebar.markdown("---")
st.sidebar.caption("Desarrollado para la cátedra de Economía Internacional - UDAL")
