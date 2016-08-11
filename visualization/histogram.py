import plotly
import plotly.graph_objs as go
import cufflinks as cf
import pandas as pd
import numpy as np # for generating random data

cf.set_config_file(offline=True, world_readable=True, theme='pearl')

# df = pd.read_csv('../data/clustered_results/All-houses.csv')

df = pd.DataFrame({'a': np.random.randn(1000) + 1,
                   'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1})
df.head(2)

data = []

for col in df.columns:
    data.append(  go.Histogram( y=df[col], name=col, showlegend=False ) )

plotly.offline.plot(data, filename='multiple-histograms')
