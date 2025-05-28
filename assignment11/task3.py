import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')
print("The first 10: ")
print(df.head(10))
print("\n The last 10: ")
print(df.tail(10))

df['strength'] = df['strength'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)
print(df[['direction', 'strength']].head(10))

fig = px.scatter(
    df, 
    x=df['strength'],
    y= df['frequency'],
    color='direction',
    title="Interactive scatter plot of strength vs. frequency")
fig.write_html("wind.html", auto_open=True)