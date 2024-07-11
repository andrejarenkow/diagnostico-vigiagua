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

option = {
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {
            "type": "cross",
            "crossStyle": {
                "color": "#999"
            }
        }
    },
    "toolbox": {
        "feature": {
            "dataView": {"show": True, "readOnly": False},
            "magicType": {"show": True, "type": ["line", "bar"]},
            "restore": {"show": True},
            "saveAsImage": {"show": True}
        }
    },
    "legend": {
        "data": ['Evaporation', 'Precipitation', 'Temperature']
    },
    "xAxis": [
        {
            "type": "category",
            "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            "axisPointer": {
                "type": "shadow"
            }
        }
    ],
    "yAxis": [
        {
            "type": "value",
            "name": "Precipitation",
            "min": 0,
            "max": 250,
            "interval": 50,
            "axisLabel": {
                "formatter": "{value} ml"
            }
        },
        {
            "type": "value",
            "name": "Temperature",
            "min": 0,
            "max": 25,
            "interval": 5,
            "axisLabel": {
                "formatter": "{value} °C"
            }
        }
    ],
    "series": [
        {
            "name": "Evaporation",
            "type": "bar",
            "tooltip": {
                "formatter": "{b}: {c} ml"
            },
            "data": [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6]
        },
        {
            "name": "Precipitation",
            "type": "bar",
            "tooltip": {
                "formatter": "{b}: {c} ml"
            },
            "data": [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6]
        },
        {
            "name": "Temperature",
            "type": "line",
            "yAxisIndex": 1,
            "tooltip": {
                "formatter": "{b}: {c} °C"
            },
            "data": [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3]
        }
    ]
}

st_echarts(options=option, height="600px")



