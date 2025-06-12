import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# T[itulo de la app
st.header("Dashboard de Anuncios de Vehículos")


# #Boton para histograma
# hist_button = st.button('Mostrar histograma del precio')  # crear un botón
# if hist_button:  #al hacer clic en el botón
#    # escribir un mensaje
#    st.write('Histograma del precio de los vehículos')
#    # crear un histograma
#    fig = px.histogram(car_data, x="price", nbins=50,
#                       title="Histograma de Precios de Vehículos")
#    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(fig, use_container_width=True)
#
# #Boton para gráfico de dispersión
# disp_button = st.button('Mostrar gráfico de dispersión')
# if disp_button:  # al hacer clic en el botón
#    # escribir un mensaje
#    st.write('Gráfico de dispersión del Precio vs Año')
#    # crear un gráfico de dispersión
#    fig2 = px.scatter(car_data, x="model_year", y="price",
#                      title="Precio vs Año de Vehículos")
#    # mostrar un gráfico Plotly interactivo
#    st.plotly_chart(fig2, use_container_width=True)

# Checkbox para mostrar el dataframe
buil_dataframe = st.checkbox('Mostrar DataFrame')
if buil_dataframe:  # al marcar el checkbox
    # escribir un mensaje
    st.write('DataFrame de los vehículos')
    # mostrar el dataframe
    st.dataframe(car_data)

# Checkbox para mostrar el histograma
buil_histogram = st.checkbox('Mostrar histograma del precio')
if buil_histogram:  # al marcar el checkbox
    # escribir un mensaje
    st.write('Histograma del precio de los vehículos')
    # crear un histograma
    fig = px.histogram(car_data, x="price", nbins=50,
                       title="Histograma de Precios de Vehículos")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
buil_scatter = st.checkbox('Mostrar gráfico de dispersión')
if buil_scatter:  # al marcar el checkbox
    # escribir un mensaje
    st.write('Gráfico de dispersión del Precio vs Año')
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="model_year", y="price",
                      title="Precio vs Año de Vehículos")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
