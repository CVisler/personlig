import pandas as pd
import random
import plotly.express as px

df = px.data.iris()
headers = list(df.columns.values)
dataset = list({})
for header in headers:
    tmp = {}
    tmp["name"] = header
    tmp["value"] = random.randint(1, 100)
    dataset.append(tmp)

# for item in dataset:
#     print(item)


pandas_df = {
"trial": {
        "title": {"text": "ECharts Getting Started Example"},
        "tooltip": {},
        # "legend": {"data": ["sales"]},
        "series": [
            {
                "name": "sales",
                "type": "pie",
                "radius": [0, "50%"],
                "data": dataset,
                "universalTransition": True,
            }
        ],
    },
}

pie_chart = {
"pie": {
        "title": {"text": "ECharts Getting Started Example"},
        "tooltip": {},
        # "legend": {"data": ["sales"]},
        "series": [
            {
                "name": "sales",
                "type": "pie",
                "radius": [0, "50%"],
                "data": [
                    {"name": "TME", "value": 5},
                    {"name": "VSE", "value": 15},
                    {"name": "DIM", "value": 9},
                    {"name": "MOB", "value": 2},
                ],
                "universalTransition": True,
            }
        ],
    },
}

line = {
    'kekkers':  {
        'xAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'data': [820, 932, 901, 934, 1290, 1330, 1320],
                'type': 'line',
                'smooth': True
            }
        ]
    }
}
