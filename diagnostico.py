import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd
import streamlit as st # Importa a biblioteca streamlit e a renomeia como st
from streamlit_echarts import st_echarts, st_pyecharts
import requests
import json


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
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import streamlit as st

list2 = [
    {"value": 12, "percent": 12 / (12 + 3)},
    {"value": 23, "percent": 23 / (23 + 21)},
    {"value": 33, "percent": 33 / (33 + 5)},
    {"value": 3, "percent": 3 / (3 + 52)},
    {"value": 33, "percent": 33 / (33 + 43)},
]

list3 = [
    {"value": 3, "percent": 3 / (12 + 3)},
    {"value": 21, "percent": 21 / (23 + 21)},
    {"value": 5, "percent": 5 / (33 + 5)},
    {"value": 52, "percent": 52 / (3 + 52)},
    {"value": 43, "percent": 43 / (33 + 43)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([1, 2, 3, 4, 5])
    .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
    .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
)

st_pyecharts(c)





