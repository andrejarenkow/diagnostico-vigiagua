import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd
import streamlit as st # Importa a biblioteca streamlit e a renomeia como st
from streamlit_echarts import st_echarts


st.title('area de testes')

import streamlit as st
from streamlit_echarts import st_echarts

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
            "type": "Total de amostras",
            "name": "水量",
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

