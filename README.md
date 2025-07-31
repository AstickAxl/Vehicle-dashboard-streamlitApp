# 🚗 Dashboard Interactivo de Anuncios de Vehículos

[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.10-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Built%20with-Streamlit-fc4c02)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Completo-brightgreen)](#)

---

Este proyecto es una aplicación web interactiva construida con **Streamlit**, que permite explorar datos de anuncios de vehículos usados. Proporciona visualizaciones dinámicas como histogramas y gráficos de dispersión, y permite visualizar el dataset completo con un solo clic.

---

## 📌 Funcionalidades principales

- ✅ Visualización del dataset de vehículos usados
- ✅ Histograma interactivo de precios
- ✅ Gráfico de dispersión entre el año del vehículo y su precio
- ✅ Interfaz amigable y ligera, construida con `Streamlit` y `Plotly`

---

## 🛠️ Herramientas utilizadas

- Python 3.10+
- Streamlit
- Plotly Express
- Pandas

---

## ▶️ Instrucciones para ejecución local

``bash``

   1. Clona el repositorio:

git clone ([https://github.com/AstickAxl/PROJECT-S7.git](https://github.com/AstickAxl/Vehicle-dashboard-streamlitApp.git))

   2. Instala las dependencias:
   
pip install -r requirements.txt

   3. Ejecuta la app:
   
streamlit run app.py
   
---

## 📁 Estructura del proyecto

vehicle_dashboard_streamlitApp/

├── app.py #Aplicación Streamlit

├── vehicles_us.csv #Dataset utilizado

├── requirements.txt #Librerías necesarias

└── README.md #Documentación del proyecto

---


## 🧠 Conclusiones

Esta aplicación demuestra cómo una interfaz construida con **Streamlit** puede facilitar el análisis exploratorio de datos de forma ágil, visual e intuitiva. El dashboard permite identificar tendencias clave en el mercado de vehículos usados:

- 📉 Existe una relación inversa entre el **año del vehículo** y su **precio**, como era de esperarse, aunque con ciertas excepciones interesantes por modelo o marca.
- 💸 El **histograma de precios** revela una alta concentración en vehículos de gama baja, lo que sugiere un mercado activo en ese segmento.
- 🧩 La interfaz permite a usuarios no técnicos visualizar la información sin necesidad de herramientas adicionales, promoviendo el acceso abierto a la toma de decisiones basada en datos.

En resumen, esta app puede escalarse como una herramienta para portales de clasificados, concesionarias o analistas que busquen detectar patrones de comportamiento en el mercado automotriz con rapidez y claridad.


---

## 👨‍💻 Autor

   Axel López

   🔗 [LinkedIn](https://www.linkedin.com/in/axel-l%C3%B3pez-linares/)

   🎯 Proyecto de portafolio - Bootcamp de Ciencia de Datos

