import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portafolio Economía - UDAL", layout="wide")

# Función para dar formato a los ejemplos
def ejemplo(texto):
    return f":blue[**🔷 Ejemplo:** *{texto}*]"

# Encabezado principal
st.title("🏛️ Portafolio de Economía Internacional para los Negocios")
st.markdown("Catálogo oficial de consulta académica con fórmulas, variables y criterios de valoración comercial.")
st.divider()

# Menú lateral
menu = st.sidebar.radio("Navegación del Portafolio:", [
    "1. Las 25 Tácticas de Negociación", 
    "2. Producción, Renta y Empleo", 
    "3. Precios, Finanzas Públicas e Intereses", 
    "4. Comercio Exterior, Inversión y Negociación Cuantitativa",
    "5. Rentabilidad Empresarial y Evaluación de Proyectos"
])

# ==========================================
# SECCIÓN 1: TÁCTICAS DE NEGOCIACIÓN
# ==========================================
if menu == "1. Las 25 Tácticas de Negociación":
    st.header("🤝 Diccionario Táctico de Negociación Internacional")
    st.info("Estrategias observadas en negociaciones corporativas y diplomacia comercial (Inspirado en casos como 'The Phoenician Scheme').")
    
    tacticas = [
        ("Asimetría de Información", "Controlar datos clave que el otro ignora.", "Ocultar los costos reales de importación del acero.", "Basándonos en informes exclusivos sobre el mercado..."),
        ("Hecho Consumado (Fait Accompli)", "Ejecutar una acción irreversible antes de negociar.", "Instalar el software en sus servidores antes de firmar.", "El sistema ya está corriendo, apagarlo será más costoso..."),
        ("Anclaje (Anchoring)", "Fijar una primera oferta extrema.", "Pedir 1 millón cuando tu meta son 500 mil.", "Nuestra tarifa inicial para este proyecto es de..."),
        ("Negociación Coercitiva", "Usar la falta de alternativas del otro.", "Imponer condiciones bajo amenaza de irse con la competencia.", "Si no firman hoy, la concesión pasa al estado vecino mañana."),
        ("Cortesía Innecesaria", "Generar deuda moral mediante lujos.", "Pagar cenas de gala o viajes a los burócratas.", "Tras esta cena en su honor, espero revisen el contrato..."),
        ("Vinculación (Linkage)", "Condicionar un punto a cambio de otro ajeno.", "Aceptar el precio si te dan exclusividad de distribución.", "Acepto este arancel si ustedes me ceden el control del puerto."),
        ("MAAN / BATNA", "Tener el mejor Plan B posible.", "Saber exactamente con qué otro proveedor irse.", "Si no cerramos bajo estos términos, firmaremos con la competencia."),
        ("ZOPA", "Identificar el rango de acuerdo posible.", "Saber el límite máximo del comprador y mínimo del vendedor.", "Busquemos el punto medio entre sus capacidades y nuestras metas."),
        ("La Retirada Estudiada", "Estar dispuesto a abandonar la mesa.", "Levantarse y recoger los papeles sin enojo.", "Lamentablemente, estos términos destruyen valor para nosotros. Adiós."),
        ("Autoridad Limitada", "Fingir no tener la última palabra.", "Echarle la culpa a la junta directiva o al gobierno.", "Me encanta su propuesta, pero el corporativo nunca la aprobará..."),
        ("El Flinch", "Mueca física de asombro ante una oferta.", "Gesto de dolor para hacer dudar al oponente.", "(Gesto de asombro) ¿Ese es su precio final?"),
        ("Silencio Estratégico", "Callar tras una oferta para incomodar.", "No responder para que el otro ofrezca más.", "(Mantener contacto visual en silencio absoluto por 10 segundos)."),
        ("Policía Bueno / Policía Malo", "Alternar presión y empatía.", "Un socio grita y el otro ofrece consuelo.", "Mi socio es inflexible, pero si ceden en esto, yo los ayudo."),
        ("El Espejo (Mirroring)", "Repetir últimas palabras como pregunta.", "Obligar al otro a explicarse sin presionar.", "¿El presupuesto es muy ajustado? (tono de duda)."),
        ("El Enmarcado (Framing)", "Presentar gasto como inversión/seguridad.", "Vender el precio alto como garantía anti-riesgos.", "No es un sobreprecio, es la prima que asegura cero multas legales."),
        ("Psicología Inversa", "Pedir lo contrario a lo que deseas.", "Hacer creer que prefieres otra moneda.", "Por favor, no me paguen en especie, prefiero su devaluada moneda..."),
        ("Técnica del Salami", "Conseguir concesiones pedazo a pedazo.", "No negociar todo el contrato de golpe.", "Primero acordemos el flete, mañana revisamos el seguro..."),
        ("El Mordisqueo (Nibbling)", "Pedir un extra con el trato casi cerrado.", "Exigir mantenimiento gratis al final.", "Ya que estamos de acuerdo, asumo que el envío viene incluido, ¿no?"),
        ("El Krunch", "Rechazar sin hacer contraoferta.", "Obligar al otro a bajar su propio precio.", "He revisado sus números, pero tienen que hacerlo mejor que eso."),
        ("El Bogey (Espantapájaros)", "Fingir interés vital en algo irrelevante.", "Pelear por el color para luego cederlo por dinero.", "El diseño original es innegociable... (luego lo cedes por un descuento)."),
        ("El Señuelo (Decoy)", "Presentar una opción mala para resaltar la buena.", "Ofrecer un contrato draconiano al lado del que quieres.", "Pueden elegir la opción C (carísima) o la A (la que tú quieres que elijan)."),
        ("Inundación de Datos", "Abrumar con tecnicismos legales.", "Entregar 500 anexos para esconder una cláusula.", "Como podrán constatar en los 40 manuales de ingeniería adjuntos..."),
        ("Oferta Explosiva", "Presión de tiempo irrazonable.", "Dar 10 minutos para firmar un trato millonario.", "Esta oferta expira en cuanto me levante de esta mesa."),
        ("Dividir la Diferencia", "Sugerir el punto medio a tu favor.", "Acercar posiciones cuando el anclaje te beneficia.", "Ustedes piden 10, yo ofrezco 6. Quedemos en 8 y terminemos esto."),
        ("Red Herring", "Distracción con un tema falso.", "Discutir la inauguración en vez de la tasa de interés.", "Pero hablemos de lo hermosa que quedará la obra terminada...")
    ]
    
    for nombre, uso, ej, guion in tacticas:
        with st.expander(f"🔹 {nombre}"):
            st.write(f"**Uso Profesional:** {uso}")
            st.write(ejemplo(ej))
            st.code(f"Guion sugerido: '{guion}'")

# ==========================================
# SECCIÓN 2: PRODUCCIÓN, RENTA Y EMPLEO
# ==========================================
elif menu == "2. Producción, Renta y Empleo":
    st.header("📊 1. Indicadores de Producción y Distribución de Renta")

    st.subheader("A. PIB por Método del Gasto")
    st.latex(r"PIB = C + I + G + (X - M)")
    st.markdown("**Variables:** $C$ (Consumo familias), $I$ (Inversión empresas), $G$ (Gasto público), $X$ (Exportaciones), $M$ (Importaciones).")
    st.write(ejemplo("Consumo 500, Inversión 200, Gobierno 150, Exportaciones 100, Importaciones 50. PIB = 900."))

    st.subheader("B. PIB por Método de Renta")
    st.latex(r"PIB = S + i + A + G_{emp}")
    st.markdown("**Variables:** $S$ (Salarios), $i$ (Intereses), $A$ (Alquileres), $G_{emp}$ (Ganancias empresariales).")

    st.subheader("C. PIB por Valor Agregado")
    st.latex(r"PIB = \sum (V_{Final} - V_{Intermedio})")
    st.write(ejemplo("Si el agricultor agrega $10, el molinero $5 y el panadero $10, el PIB es 25 (evita doble contabilidad)."))

    st.subheader("D. PIB Per Cápita (Nominal y Real)")
    st.latex(r"PIB_{per\_capita} = \frac{PIB}{Población}")

    st.subheader("E. PNB y PIN (Ajustes de Producción)")
    st.latex(r"PNB = PIB + RNE - REN")
    st.markdown("**Variables:** $RNE$ (Renta Nacionales Extranjero), $REN$ (Renta Extranjeros Nación).")
    st.latex(r"PIN = PIB - Depreciación")

    st.subheader("F. Renta Nacional (RN), Personal (RP) y Disponible (RPD)")
    st.latex(r"RN = PNB - Depreciación - Impuestos\_Indirectos + Subvenciones")
    st.latex(r"RP = RN - BND - IS - CS + TR")
    st.latex(r"RPD = RP - Impuestos\_Directos")
    st.markdown("**Variables:** $BND$ (Beneficios No Distribuidos), $IS$ (Impuesto Sociedades), $CS$ (Cotizaciones Sociales), $TR$ (Transferencias).")
    st.write(ejemplo("Si ganas 820 y pagas 100 de ISR, tu RPD (para gastar o ahorrar) es 720."))

    st.divider()
    st.header("👥 2. Indicadores Sociolaborales")
    st.subheader("Tasa de Desempleo y Tipos")
    st.latex(r"Tasa\_Desempleo = \frac{Desempleados}{PEA} \times 100")
    st.markdown("""
    **Tipos de Desempleo:**
    * **Friccional:** Transición voluntaria entre empleos.
    * **Estructural:** Desajuste entre habilidades de la gente y demandas del mercado (ej. IA reemplazando labores).
    * **Cíclico:** Causado por caídas en el PIB (recesiones).
    """)

# ==========================================
# SECCIÓN 3: PRECIOS, FINANZAS E INTERESES
# ==========================================
elif menu == "3. Precios, Finanzas Públicas e Intereses":
    st.header("📉 3. Precios y Poder Adquisitivo")

    st.subheader("A. IPC, Deflactor e Inflación (Base 1)")
    st.latex(r"IPC = \frac{Precio\_Actual\_Canasta}{Precio\_Base\_Canasta}")
    st.latex(r"Deflactor = \frac{PIB_{Nominal}}{PIB_{Real}}")
    st.latex(r"Inflación\_IPC (\%) = \frac{IPC_{Actual} - IPC_{Anterior}}{IPC_{Anterior}} \times 100")

    st.subheader("B. Poder Adquisitivo y Variación")
    st.latex(r"Poder\_Adquisitivo = \frac{Precio\_Histórico}{Precio\_Actual} = \frac{1}{IPC}")
    st.latex(r"\Delta \%_{PA} = \frac{PA_{Actual} - PA_{Anterior}}{PA_{Anterior}} \times 100")
    st.write(ejemplo("Con un IPC de 1.20, el Poder Adquisitivo es 1 / 1.20 = 0.833. El dinero vale un 16.7% menos."))

    st.divider()
    st.header("🏛️ 4. Finanzas Públicas y Estado")
    
    st.subheader("A. Presupuesto y Deuda")
    st.latex(r"Balance = Ingresos\_Tributarios - Gasto\_Público")
    st.latex(r"Presión\_Fiscal = \frac{Recaudación\_Tributaria}{PIB} \times 100")
    st.latex(r"Ratio\_Deuda = \frac{Deuda\_Pública\_Total}{PIB} \times 100")
    st.markdown("**Criterio de Valoración (Ratio Deuda):** < 60% (Sano), 60%-90% (Precaución), > 90% (Riesgo Crítico).")

    st.divider()
    st.header("💰 5. Tipos de Interés")
    
    st.subheader("A. Simple, Compuesto y Relación de Fisher")
    st.latex(r"Interés\_Simple = Principal \times i \times t")
    st.latex(r"Monto\_Compuesto = Principal \times (1 + i)^t")
    st.latex(r"Tasa\_Real (r) \approx i_{Nominal} - Inflación")
    st.write(ejemplo("Si el banco cobra 15% pero la inflación es 10%, la tasa de interés real que impacta tu deuda es solo del 5%."))

# ==========================================
# SECCIÓN 4: COMERCIO Y NEGOCIACIÓN CUANTITATIVA
# ==========================================
elif menu == "4. Comercio Exterior, Inversión y Negociación Cuantitativa":
    st.header("🚢 6. Comercio Internacional")

    st.subheader("A. Elasticidad de Importaciones/Exportaciones")
    st.latex(r"\epsilon = \frac{\% \Delta Q}{\% \Delta P}")
    st.markdown("**Criterio:** $|\epsilon| > 1$ (Elástica, muy sensible al precio). $|\epsilon| < 1$ (Inelástica, poder monopólico, soporta aranceles).")
    
    st.subheader("B. Tipos de Cambio")
    st.markdown("* **Directo:** Moneda local por 1 extranjera (Ej. 20 MXN = 1 USD).")
    st.markdown("* **Indirecto:** Moneda extranjera por 1 local (Ej. 1 MXN = 0.05 USD).")
    st.latex(r"E_{Cruzado} (A/C) = E(A/B) \times E(B/C)")
    st.latex(r"E_{Real} = E_{Nominal} \times \frac{P_{Extranjero}}{P_{Local}}")

    st.subheader("C. Ventaja Comparativa, Aranceles y Cuotas")
    st.latex(r"Costo\_Oportunidad = \frac{\text{Producción Bien Sacrificado}}{\text{Producción Bien Obtenido}}")
    st.markdown("* **Aranceles:** Ad Valorem (% del valor), Específico (cobro fijo por unidad), Mixto.")
    st.markdown("* **Cuotas:** Límite máximo en volumen físico permitido en frontera (No recauda impuestos).")

    st.divider()
    st.header("⚖️ 7. Negociación Cuantitativa")

    st.subheader("A. ZOPA (Zona de Posible Acuerdo)")
    st.latex(r"ZOPA = PR_{Comprador} - PR_{Vendedor}")
    st.markdown("**Criterio:** Si ZOPA > 0, el trato es viable. Si ZOPA < 0, invoca tu MAAN y abandona la mesa.")
    
    st.subheader("B. Valor Esperado (VE)")
    st.latex(r"VE = (Prob\_Éxito \times Beneficio) - (Prob\_Fracaso \times Pérdida)")
    st.markdown("**Criterio:** Aceptar si el VE es estrictamente mayor al valor financiero de tu MAAN.")

    st.subheader("C. Valoración del MAAN / BATNA")
    st.latex(r"Valor\_MAAN = Beneficio\_Alternativa - Costo\_Transición")
    
    st.subheader("D. Ratio de Apalancamiento de Poder")
    st.latex(r"Ratio\_Poder = \frac{Costo\_MAAN\_Oponente}{Costo\_MAAN\_Propio}")
    st.markdown("**Criterio:** Ratio > 1 implica que tú tienes el poder (al otro le cuesta más romper el trato).")
    
    st.subheader("E. Costo Total de Concesión (CTC) y VPN de Ofertas Diferidas")
    st.latex(r"CTC = (Valor\_Original - Valor\_Concedido) \times Volumen \times Tiempo")
    st.latex(r"VPN\_Negociación = \frac{Pago\_Futuro}{(1 + i)^n}")
    st.write(ejemplo("Si te ofrecen 115M en 2 años en lugar de 100M hoy, y tu tasa (i) es 10%, el VPN es 95M. Estás perdiendo valor real."))

# ==========================================
# SECCIÓN 5: RENTABILIDAD Y PROYECTOS
# ==========================================
elif menu == "5. Rentabilidad Empresarial y Evaluación de Proyectos":
    st.header("🏢 8. Rentabilidad Corporativa e Inversión")

    st.subheader("A. Margen Neto, ROA y ROE")
    st.latex(r"Margen\_Neto = \frac{Beneficio\_Neto}{Ventas\_Totales} \times 100")
    st.latex(r"ROA = \frac{Beneficio\_Neto}{Activos\_Totales} \times 100")
    st.latex(r"ROE = \frac{Beneficio\_Neto}{Patrimonio\_Neto} \times 100")
    st.markdown("""
    **Criterios de Valoración:**
    * **ROA > 5%:** Sano para industrias pesadas (Mide eficiencia gerencial global).
    * **ROE > ROA:** Indica uso inteligente de deuda (apalancamiento) para maximizar la ganancia de los dueños.
    """)

    st.subheader("B. EBITDA y ROI")
    st.latex(r"EBITDA = Ingresos - Costos\_Operativos\_Directos")
    st.latex(r"ROI = \frac{Ganancia - Inversión}{Inversión} \times 100")
    st.markdown("**Criterio ROI:** Debe ser mayor que la Tasa Libre de Riesgo (Cetes/Bonos) + Prima de Riesgo.")

    st.subheader("C. Depreciación")
    st.latex(r"Depreciación\_Lineal = \frac{V_{Inicial} - V_{Residual}}{Vida\_Útil}")
    st.markdown("**Acelerada / Doble Saldo:** Se deprecia un porcentaje fijo superior sobre el saldo en libros, cargando el costo en los primeros años.")

    st.divider()
    st.header("⏳ 9. Evaluación de Proyectos y Plazos")

    st.subheader("A. Ciclo de Conversión de Efectivo (CCE)")
    st.latex(r"CCE = Días\_Inventario + Días\_Cobro - Días\_Pago")
    st.markdown("**Criterio:** Mientras menor (o más negativo), mejor. Significa que los proveedores financian tu operación sin intereses.")

    st.subheader("B. Payback (Periodo de Recuperación)")
    st.latex(r"Payback = \frac{Inversión\_Inicial}{Flujo\_Caja\_Anual}")
    st.write(ejemplo("Inversión de 500M que deja 125M anuales libres, se recupera en 4 años."))

    st.subheader("C. Tasa Interna de Retorno (TIR)")
    st.markdown("""
    Es la tasa porcentual anualizada de rentabilidad del proyecto (aquella que hace que el Valor Presente Neto sea 0).
    **Criterios de Decisión (Regla de Oro):**
    * **TIR > WACC (Costo de Capital):** Aceptar el proyecto. Genera riqueza.
    * **TIR < WACC (Costo de Capital):** Rechazar. El banco te cobra más de lo que el proyecto te paga.
    """)
    
