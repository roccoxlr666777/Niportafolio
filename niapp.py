import streamlit as st

# Configuración profesional
st.set_page_config(page_title="Portafolio Economía Internacional UDAL", layout="wide")

# Estilo para ejemplos (Color azul/celeste)
def blue_text(text):
    return f":blue[{text}]"

# Título y Navegación
st.title("🏛️ Portafolio de Economía Internacional para los Negocios")
st.sidebar.header("Menú de Control")
menu = st.sidebar.radio("Navegación:", [
    "1. Estrategias de Negociación", 
    "2. Catálogo de Cálculos (Teoría)", 
    "3. Calculadora Interactiva"
])

# --- SECCIÓN 1: ESTRATEGIAS DE NEGOCIACIÓN ---
if menu == "1. Estrategias de Negociación":
    st.header("🤝 Diccionario Táctico de Negociación")
    tecnicas = [
        ("Asimetría de Información", "Controlar datos clave.", "Ocultar costos reales de importación.", "Basándonos en informes exclusivos..."),
        ("Hecho Consumado", "Actuar antes de negociar.", "Instalar el software antes de firmar.", "El sistema ya está corriendo..."),
        ("Anclaje", "Fijar precio extremo inicial.", "Pedir 1M cuando quieres 500k.", "Nuestra tarifa inicial es de..."),
        ("Negociación Coercitiva", "Usar dependencia.", "Amenazar con romper el contrato.", "Si no firman hoy, perdemos la cuota..."),
        ("Cortesía Innecesaria", "Generar deuda moral.", "Regalos o cenas de lujo.", "Tras esta cena, espero que vean..."),
        ("Vinculación (Linkage)", "Condicionar puntos ajenos.", "Bajar arancel si nos dan el puerto.", "Acepto X si ustedes me dan Y."),
        ("MAAN (BATNA)", "Plan B sólido.", "Tener otra oferta en mano.", "Si no cerramos, firmaremos con..."),
        ("ZOPA", "Rango de acuerdo.", "Saber el límite del otro.", "Busquemos el punto medio entre..."),
        ("Retirada Estudiada", "Abandonar la mesa.", "Demostrar que no estás desesperado.", "Lamentablemente, no podemos aceptar..."),
        ("Autoridad Limitada", "Consultar a superior.", "Echar la culpa a la junta.", "Mi jefe no aprobaría esto sin..."),
        ("El Flinch", "Reacción de asombro.", "Gesto de dolor ante oferta.", "(Gesto de sorpresa) ¿Ese precio?"),
        ("Silencio Estratégico", "Incomodar al otro.", "No hablar tras una propuesta.", "(Mantener silencio prolongado)"),
        ("Policía Bueno/Malo", "Presión y empatía.", "Socio duro y socio blando.", "Él es difícil, pero yo les ayudo si..."),
        ("El Espejo", "Repetir palabras.", "Extraer info sutilmente.", "¿Demasiado caro? (en tono de duda)"),
        ("Enmarcado (Framing)", "Presentar como ganancia.", "Seguridad vs Costo.", "No es un gasto, es un blindaje."),
        ("Psicología Inversa", "Pedir lo contrario.", "Sugerir que no quieres diamantes.", "Por favor, no me paguen con oro..."),
        ("Técnica del Salami", "Concesiones mínimas.", "Acuerdos por partes pequeñas.", "Primero el flete, luego el seguro..."),
        ("Mordisqueo", "Extra al final.", "Pedir post-venta gratis.", "Ya que firmamos, ¿incluyen el envío?"),
        ("El Krunch", "Obligar a mejorar.", "Rechazo automático.", "Tienen que hacerlo mejor que eso."),
        ("El Bogey", "Fingir interés en algo.", "Pelear por el color del logo.", "El color es vital... (luego lo cedes)"),
        ("El Señuelo", "Opción mala comparada.", "Plan caro vs Plan ideal.", "El plan C es terrible, el A es mejor."),
        ("Inundación de Datos", "Confundir con info.", "Entregar 500 anexos técnicos.", "Como ven en estos 50 manuales..."),
        ("Oferta Explosiva", "Presión de tiempo.", "Válido solo por 10 minutos.", "Esta oferta expira al colgar."),
        ("Dividir Diferencia", "Punto medio.", "Cerrar rápido.", "Ustedes 10, yo 6; quedemos en 8."),
        ("Red Herring", "Distracción.", "Hablar de estética, no de deuda.", "Vean qué bonitos son los túneles.")
    ]
    
    for nombre, uso, ejemplo, guion in tecnicas:
        with st.expander(f"🔹 {nombre}"):
            st.write(f"**Uso:** {uso}")
            st.write(f"**Ejemplo:** {blue_text(ejemplo)}")
            st.code(f"Guion: '{guion}'")

# --- SECCIÓN 2: CATÁLOGO DE CÁLCULOS ---
elif menu == "2. Catálogo de Cálculos (Teoría)":
    st.header("📖 Catálogo de Variables e Indicadores")
    
    with st.expander("📝 Glosario de Variables"):
        st.markdown("""
        * $C$: Consumo de las familias.
        * $I$: Inversión de las empresas.
        * $G$: Gasto público gubernamental.
        * $X$: Exportaciones.
        * $M$: Importaciones.
        * $S$: Salarios de obreros.
        * $i$: Intereses del capital.
        * $A$: Alquileres por la tierra / Arrendamientos.
        * $G_{emp}$: Ganancias o beneficios empresariales.
        * $RNE$: Renta de Nacionales en el Extranjero.
        * $REN$: Renta de Extranjeros en la Nación.
        """)

    st.subheader("1. Producción y Renta Nacional")
    st.latex(r"PIB_{Gasto} = C + I + G + (X - M)")
    st.latex(r"PIB_{Renta} = S + i + A + G_{emp}")
    st.latex(r"PNB = PIB + RNE - REN")
    st.latex(r"PIN = PIB - Depreciación")
    st.latex(r"RNN = PNB - Depreciación - Impuestos Indirectos + Subvenciones")
    st.write(f"**Ejemplo:** {blue_text('Si el PIB es 1000 y los nacionales ganan 200 fuera, el PNB sube a 1200.')}")

    st.subheader("2. Precios e Inflación (Base 1)")
    st.latex(r"IPC = \frac{\sum P_{actual} \cdot Q_{base}}{\sum P_{base} \cdot Q_{base}}")
    st.latex(r"Deflactor = \frac{PIB_{Nominal}}{PIB_{Real}}")
    st.latex(r"Poder Adquisitivo = \frac{Precio_{Histórico}}{Precio_{Actual}} = \frac{1}{IPC}")
    st.write(f"**Ejemplo:** {blue_text('Si el IPC es 1.20, el poder adquisitivo cayó a 0.83 (1/1.20).')}")

    st.subheader("3. Finanzas Internacionales")
    st.latex(r"Tasa Intercambio (TOT) = \frac{P_{Exportación}}{P_{Importación}}")
    st.latex(r"E_{Real} = E_{Nominal} \times \frac{P_{Extranjero}}{P_{Local}}")

# --- SECCIÓN 3: CALCULADORA INTERACTIVA ---
elif menu == "3. Calculadora Interactiva":
    st.header("🧮 Calculadora de Economía Internacional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Entradas de Datos")
        c = st.number_input("Consumo (C)", value=0.0)
        i_inv = st.number_input("Inversión (I)", value=0.0)
        g = st.number_input("Gasto Público (G)", value=0.0)
        exp = st.number_input("Exportaciones (X)", value=0.0)
        imp = st.number_input("Importaciones (M)", value=0.0)
        p_nom = st.number_input("PIB Nominal (para deflactor)", value=1.0)
        p_real = st.number_input("PIB Real", value=1.0)
        dep = st.number_input("Depreciación Total", value=0.0)

    with col2:
        st.subheader("Resultados en Tiempo Real")
        pib_g = c + i_inv + g + (exp - imp)
        st.metric("PIB (Método Gasto)", f"{pib_g:,.2f}")
        
        pin = pib_g - dep
        st.metric("PIN (Producto Interno Neto)", f"{pin:,.2f}")
        
        deflactor = p_nom / p_real
        st.metric("Deflactor (Base 1)", f"{deflactor:,.4f}")
        
        if deflactor > 0:
            pa = 1 / deflactor
            st.metric("Poder Adquisitivo (Rel. Deflactor)", f"{pa:,.4f}")
            
        if imp > 0:
            tot = exp / imp
            st.metric("Tasa de Intercambio (TOT)", f"{tot:,.2f}")

    st.markdown("---")
    st.subheader("Cálculo de Depreciación")
    v_i = st.number_input("Valor Inicial del Activo", value=1000.0)
    v_r = st.number_input("Valor Residual", value=100.0)
    vida = st.number_input("Vida Útil (años)", value=5)
    
    dep_lin = (v_i - v_r) / vida
    st.write(f"**Depreciación Lineal Anual:** {dep_lin:,.2f}")
