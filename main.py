import folium
import pandas as pd

# Load your dataset here
ufo_data_path = 'ufo_sightings (1).csv'
ufo_data = pd.read_csv(ufo_data_path, sep=',', nrows=100000)

# Function to create a map for a specific year and month
def create_ufo_sightings_map(year, data):
    # Create a base map centered around the United States
    for month in range(1,13):
        ufo_map = folium.Map(location=[47.033281, -130.732018], zoom_start=4)
    
        # Filter the dataset for the specified year and month
        filtered_data = data[(data['Dates.Sighted.Year'] == year) & (data['Dates.Sighted.Month'] == month)]
    
        # Iterate over the filtered dataset and add markers to the map
        for index, sighting in filtered_data.iterrows():
            folium.Marker(
                location=[sighting['Location.Coordinates.Latitude '], sighting['Location.Coordinates.Longitude ']],
                tooltip=f"State: {sighting['Location.State']} Coords: {sighting['Location.Coordinates.Latitude ']}, {sighting['Location.Coordinates.Longitude ']}",
                icon=folium.Icon(icon_size=(40, 40), color = "red"),
            ).add_to(ufo_map)
    
        # Save the map to an HTML file
        ufo_map.save(f'ufo_sightings_map_{year}_{month}.html')

# Example usage: Create and save a map for January 2013
create_ufo_sightings_map(2013, ufo_data)

