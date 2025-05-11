import streamlit as st

st.set_page_config(page_title="PredictJet", layout="wide")

# Menú de navegación funcional
st.sidebar.title("Menú de Navegación")
seccion = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Producto",
    "Beneficios",
    "Casos de uso",
    "Demo",
    "Contacto"
])

# Secciones dinámicas
if seccion == "Inicio":
    st.title("🔧 PredictJet")
    st.subheader("Predictive Maintenance for Safer, Smarter Aviation")
    st.markdown("""
    PredictJet es una plataforma de IA que predice fallos mecánicos y recomienda acciones de mantenimiento preventivo antes de que ocurran. Anticipa riesgos, mejora la disponibilidad de la flota y reduce costes.
    """)

elif seccion == "Producto":
    st.header("🛠 Nuestro Producto")
    st.markdown("""
    - **Modelos predictivos** basados en machine learning y datos operativos.
    - **Alertas tempranas** sobre fallos críticos en motor, fuselaje y aviónica.
    - **Integración completa** con sistemas AMOS y plataformas de mantenimiento.
    - **Panel de salud** de la flota con KPIs técnicos en tiempo real.
    """)

elif seccion == "Beneficios":
    st.header("📈 Beneficios Clave")
    col1, col2, col3 = st.columns(3)
    col1.metric("🛑 Incidentes evitados", "-30%", "Predictivo")
    col2.metric("✈️ Disponibilidad flota", "+12%", "↑")
    col3.metric("💰 Ahorro mantenimiento", "-20%", "Anual")

elif seccion == "Casos de uso":
    st.header("✈️ Casos de Uso")
    st.markdown("""
    - Aviones de media distancia con alta rotación diaria
    - Flotas en climas extremos con estrés mecánico acelerado
    - Operadores que buscan certificación EASA para mantenimiento predictivo
    """)

elif seccion == "Demo":
    st.header("🧪 Demo en Tiempo Real")
    st.markdown("Explora la demo funcional [aquí](https://aeropredict-demo.streamlit.app/) para ver cómo funciona la predicción avanzada.")

elif seccion == "Contacto":
    st.header("📬 Contacto")
    st.markdown("""
    ¿Quieres reducir costes e incrementar la seguridad de tu flota?
    Escríbenos:

    📧 soporte@predictjet.ai  

    """)

# Footer
st.markdown("""
---
(c) 2025 PredictJet. Todos los derechos reservados.
""")
