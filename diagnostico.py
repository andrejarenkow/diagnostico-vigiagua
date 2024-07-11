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

# URL do SVG
svg_url = "https://echarts.apache.org/examples/data/asset/geo/Veins_Medical_Diagram_clip_art.svg"

# Carregar o SVG
svg_content = requests.get(svg_url).text

# Configurar as opções do gráfico
option = {
    "tooltip": {},
    "geo": {
        "left": 10,
        "right": '50%',
        "map": 'organ_diagram',
        "selectedMode": 'multiple',
        "emphasis": {
            "focus": 'self',
            "itemStyle": {
                "color": None
            },
            "label": {
                "position": 'bottom',
                "distance": 0,
                "textBorderColor": '#fff',
                "textBorderWidth": 2
            }
        },
        "blur": {},
        "select": {
            "itemStyle": {
                "color": '#b50205'
            },
            "label": {
                "show": False,
                "textBorderColor": '#fff',
                "textBorderWidth": 2
            }
        }
    },
    "grid": {
        "left": '60%',
        "top": '20%',
        "bottom": '20%'
    },
    "xAxis": {},
    "yAxis": {
        "data": [
            'heart',
            'large-intestine',
            'small-intestine',
            'spleen',
            'kidney',
            'lung',
            'liver'
        ]
    },
    "series": [
        {
            "type": 'bar',
            "emphasis": {
                "focus": 'self'
            },
            "data": [121, 321, 141, 52, 198, 289, 139]
        }
    ]
}

# Renderizar o gráfico
st_echarts(
    options=option,
    height="600px",
    width="100%",
    renderer="svg",
    key="organ_diagram_chart",
    map={
        "organ_diagram": svg_content
    }
)


