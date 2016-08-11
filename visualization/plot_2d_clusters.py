import plotly
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('../data/clustered_results/TX-houses.csv')
df.head()

data = []
clusters = []
colors = ['rgb(228,26,28)','rgb(55,126,184)','rgb(77,175,74)', 'rgb(255, 51, 153)', 'rgb(102, 204, 255)', 'rgb(0, 153, 51)', 'rgb(153, 51, 0)']

for i in range(len(df['cluster'].unique())):
    name = df['cluster'].unique()[i]

    color = colors[i]
    x = df[ df['cluster'] == name ]['sqft']
    y = df[ df['cluster'] == name ]['zestimate']

    trace = dict(
        name = 'Cluster {}'.format(name),
        x = x, y = y,
        type = "scatter2d",
        mode = 'markers',
        marker = dict( size=3, color=color, line=dict(width=0) ) )
    data.append( trace )

    # cluster = dict(
    #     color = color,
    #     opacity = 0.3,
    #     type = "mesh2d",
    #     x = x, y = y )
    # data.append( cluster )

layout = dict(
    width=800,
    height=550,
    autosize=False,
    title='Zestimate vs. sqft',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        aspectratio = dict( x=1, y=1 ),
        aspectmode = 'manual'
    ),
)

fig = dict(data=data, layout=layout)

# IPython notebook
# py.iplot(fig, filename='pandas-3d-scatter-iris', validate=False)

url = plotly.offline.plot(fig, filename='plot_2d_clusters.html', validate=False)
