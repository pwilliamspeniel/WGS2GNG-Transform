import pandas as pd
from pyproj import CRS, Transformer

# Define CRS
WGS_84 = CRS.from_epsg(4326)  # EPSG code for WGS_84
GNG = CRS.from_epsg(2136)  # EPSG code for Ghana National Grid

# Create Transformer
transformer = Transformer.from_crs(WGS_84, GNG, always_xy=True)

# Read CSV file containing coordinates
input_file = 'input_coordinates.csv'
df = pd.read_csv(input_file)

# Apply transformation to each row of coordinates
df[['x', 'y']] = df.apply(lambda row: transformer.transform(row['Longitude'], row['Latitude']), axis=1, result_type='expand')

# Format coordinates to 4 decimal places
df['x'] = df['x'].round(4)
df['y'] = df['y'].round(4)

# Save the transformed coordinates to a new CSV file
output_file = 'output_transformed_coordinates.csv'
df.to_csv(output_file, index=False)

print(f"Transformation completed. Results saved to {output_file}")
