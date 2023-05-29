import gmaps,gmaps.datasets
from matplotlib import pyplot as plt
gmaps.configure(api_key=your_api_key)

earthquake=gmaps.datasets.load_dataset_as_df('earthquakes')
locations=earthquake[['latitude','longitude']]
weights=earthquake['magnitude']

fig=gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations,weights))
fig