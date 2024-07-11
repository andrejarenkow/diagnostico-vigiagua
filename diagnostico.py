import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd
import streamlit as st # Importa a biblioteca streamlit e a renomeia como st
from streamlit_echarts import st_echarts
import requests



st.title('area de testes')

import streamlit as st
from streamlit_echarts import st_echarts

# Exemplos: https://echarts.apache.org/examples/en/index.html

st.markdown("""[Exemplos](https://echarts.apache.org/examples/en/index.html)""")

option = {
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {
            "type": "cross"
        }
    },
    "xAxis": {
        "type": "category",
        "data": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
        "axisPointer": {
            "type": "shadow"
        }
    },
    "yAxis": [
        {
            "type": "value",
            "name": "Total de amostras",
            "min": 0,
            "max": 250,
            "interval": 50,
            "axisLabel": {
                "formatter": "{value}"
            }
        },
        {
            "type": "value",
            "name": "Percentual de detecção",
            "min": 0,
            "max": 25,
            "interval": 5,
            "axisLabel": {
                "formatter": "{value} %"
            }
        }
    ],
    "series": [
        {
            "name": "Total de amostras",
            "type": "bar",
            "data": [18, 64, 143, 82, 70, 64, 55, 85, 115, 167, 174, 201]
        },
        {
            "name": "Percentual de detecção",
            "type": "line",
            "yAxisIndex": 1,
            "data": [0,15.6, 15.4, 8.6, 10, 6.2, 7.3, 2.4, 6.1, 7.8, 10.9, 8]
        }
    ]
}

st_echarts(
    options=option, height="400px",
)
##########################################################

import streamlit as st
import json
import time
import random

# Função para gerar dados virtuais semelhante ao JavaScript
def get_virtual_data(year):
    date_list = pd.date_range(
        start=f"{year}-01-01", end=f"{year + 1}-01-01", freq="D"
    )
    return [[d.strftime("%Y-%m-%d"), 1] for d in date_list]

option = {
    "tooltip": {"position": "top"},
    "visualMap": {
        "min": 0,
        "max": 10000,
        "calculable": True,
        "orient": "horizontal",
        "left": "center",
        "top": "top",
    },
    "calendar": [
        {"range": "2020", "cellSize": ["auto", 20]},
        {"top": 260, "range": "2019", "cellSize": ["auto", 20]},
        {"top": 450, "range": "2018", "cellSize": ["auto", 20], "right": 5},
    ],
    "series": [
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 0,
            "data": get_virtual_data(2020),
        },
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 1,
            "data": get_virtual_data(2019),
        },
        {
            "type": "heatmap",
            "coordinateSystem": "calendar",
            "calendarIndex": 2,
            "data": get_virtual_data(2018),
        },
    ],
}
st_echarts(option, height="640px", key="echarts")



