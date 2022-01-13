import pandas as pd
import plotly_express as px

df = pd.read_csv("line_chart.csv")

fig = px.line(df,x="Year",y="Per capita income",title="Line chart of Per Capita Income",color="Country")

fig.show()

