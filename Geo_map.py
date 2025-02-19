import plotly.express as px
import pandas

data = pandas.read_csv("Hotel Bookings.csv")
# Count the number of bookings per country
country_counts = data['country'].value_counts().reset_index()
country_counts.columns = ['country', 'bookings']

# Create a choropleth map
fig = px.choropleth(
    country_counts,
    locations="country",
    locationmode="ISO-3",  # Use ISO 3166-1 alpha-3 codes for countries
    color="bookings",
    title="Number of Bookings per Country",
    color_continuous_scale=px.colors.sequential.Plasma,
)

# Update layout for better visualization
fig.update_layout(
    title_x=0.5,
    geo=dict(showframe=False, showcoastlines=True, projection_type="equirectangular")
)

# Show the map
fig.show()
