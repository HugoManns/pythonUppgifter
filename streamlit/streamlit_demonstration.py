import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# =============================================================================
# Loading Data and Modelling it.
# =============================================================================

# Put your own path for reading the Excel file.
modelling_data = pd.read_excel(r'/Users/hugomanns/Documents/repos/pythonUppgifter/streamlit/modelling_data.xlsx')

x = np.array(modelling_data["x"])
y = np.array(modelling_data["y"])

# Plotting the data.
fig_data, ax_data = plt.subplots(figsize=(8, 4))
ax_data.set_title('Data')
ax_data.scatter(modelling_data["x"], modelling_data["y"])
ax_data.set_xlabel('x')
ax_data.set_ylabel('y')

# Initializing and fitting our Linear Regression model.
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Creating new data that we will predict with our fitted model.
x_new = np.linspace(0, 2, 20).reshape(-1, 1)
y_pred_lr = lin_reg.predict(x_new)

# Plotting the data and our model predictions.
fig_model, ax_model = plt.subplots()
ax_model.set_title("Linear Regression Model")
ax_model.scatter(x, y, label="Data")
ax_model.plot(x_new, y_pred_lr, 'r', label='Predictions')
ax_model.set_xlabel("x")
ax_model.set_ylabel("y")
ax_model.legend()

# =============================================================================
# Creating the streamlit application. #
# =============================================================================

# Creating a navigation menu with four different sections the user can choose. 
nav = st.sidebar.radio("Navigation Menu", ["Purpose", "Data & Modelling", "Other Diagrams", "Next Step"])

if nav == "Purpose":
    st.title("Streamlit - Example Demonstration")
    st.header("Purpose")
    st.write("""The purpose of this example demonstration is to give you a fast 
             overview of Streamlit where details are omitted.""")

if nav == "Data & Modelling":
    st.title("Data & Machine Learning Modelling")
    st.write('In this section we will look at the data and also model it using Linear Regression.')

    st.header("Data")
    st.subheader("Scatterplot of the Data")
    st.pyplot(fig_data)

    st.header("Machine Learning Model - Linear Regression")
    st.subheader("Visualizing the Model")
    st.pyplot(fig_model)

if nav == "Other Diagrams":
    st.title("Additional Diagrams")

    # Pie Chart
    st.subheader("Pie Chart")
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(y.flatten(), labels=x.flatten(), autopct="%.2f%%")
    st.pyplot(fig_pie)

    # Bar Plot
    st.subheader("Bar Plot")
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(x.flatten(), y.flatten())
    ax_bar.set_xlabel("x")
    ax_bar.set_ylabel("y")
    st.pyplot(fig_bar)

if nav == "Next Step":
    st.title("Read the Documentation")
    st.write("""Read the section "Get Started" from the documentation
    available at: [https://docs.streamlit.io/library/get-started](https://docs.streamlit.io/library/get-started) .""")
