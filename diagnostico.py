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
    date = time.mktime(time.strptime(year + '-01-01', '%Y-%m-%d'))
    end = time.mktime(time.strptime(str(int(year) + 1) + '-01-01', '%Y-%m-%d'))
    day_time = 3600 * 24 * 1000
    data = []
    while date < end:
        data.append([
            time.strftime('%Y-%m-%d', time.localtime(date)),
            int(random.random() * 1000)
        ])
        date += day_time
    return data

# Dados do gráfico
option = {
    "tooltip": {
        "position": "top",
        "formatter": "{b}: {c}"
    },
    "visualMap": {
        "min": 0,
        "max": 1000,
        "calculable": True,
        "orient": "vertical",
        "left": "670",
        "top": "center"
    },
    "calendar": [
        {"orient": "vertical", "range": "2015"},
        {"left": 300, "orient": "vertical", "range": "2016"},
        {
            "left": 520,
            "cellSize": [20, 'auto'],
            "bottom": 10,
            "orient": "vertical",
            "range": "2017",
            "dayLabel": {"margin": 5}
        }
    ],
    "series": [
        {"type": "heatmap", "coordinateSystem": "calendar", "calendarIndex": 0, "data": get_virtual_data('2015')},
        {"type": "heatmap", "coordinateSystem": "calendar", "calendarIndex": 1, "data": get_virtual_data('2016')},
        {"type": "heatmap", "coordinateSystem": "calendar", "calendarIndex": 2, "data": get_virtual_data('2017')}
    ]
}

st_echarts(options=option, height="600px")



