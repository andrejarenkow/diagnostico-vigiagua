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

with open("https://raw.githubusercontent.com/andfanilo/streamlit-echarts-demo/master/data/life-expectancy-table.json") as f:
    raw_data = json.load(f)
countries = [
    "Finland",
    "France",
    "Germany",
    "Iceland",
    "Norway",
    "Poland",
    "Russia",
    "United Kingdom",
]

datasetWithFilters = [
    {
        "id": f"dataset_{country}",
        "fromDatasetId": "dataset_raw",
        "transform": {
            "type": "filter",
            "config": {
                "and": [
                    {"dimension": "Year", "gte": 1950},
                    {"dimension": "Country", "=": country},
                ]
            },
        },
    }
    for country in countries
]

seriesList = [
    {
        "type": "line",
        "datasetId": f"dataset_{country}",
        "showSymbol": False,
        "name": country,
        "endLabel": {
            "show": True,
            "formatter": JsCode(
                "function (params) { return params.value[3] + ': ' + params.value[0];}"
            ).js_code,
        },
        "labelLayout": {"moveOverlap": "shiftY"},
        "emphasis": {"focus": "series"},
        "encode": {
            "x": "Year",
            "y": "Income",
            "label": ["Country", "Income"],
            "itemName": "Year",
            "tooltip": ["Income"],
        },
    }
    for country in countries
]

option = {
    "animationDuration": 10000,
    "dataset": [{"id": "dataset_raw", "source": raw_data}] + datasetWithFilters,
    "title": {"text": "Income in Europe since 1950"},
    "tooltip": {"order": "valueDesc", "trigger": "axis"},
    "xAxis": {"type": "category", "nameLocation": "middle"},
    "yAxis": {"name": "Income"},
    "grid": {"right": 140},
    "series": seriesList,
}
st_echarts(options=option, height="600px")



