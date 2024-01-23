# WGS2GNG-Transform
WGS2GNG-Converter is a Python-based geospatial tool designed to streamline the transformation of coordinates between the widely used World Geodetic System (WGS84) and the specific coordinate system of Ghana, known as Ghana National Grid (GNG). 

## Overview

WGS2GNG-Converter is a user-friendly Python tool designed to simplify the conversion of geographic coordinates from the widely used World Geodetic System (WGS84) to the specific Ghana National Grid (GNG). This tool is based on the ESPG standard and leverages the PyProj library to provide a hassle-free experience for transforming coordinates. Whether you are working on cadastral mapping or other projects in Ghana, WGS2GNG-Converter streamlines the process without the need for complex tasks.

## Why Use WGS2GNG-Converter?

### Cadastral Mapping Made Easy

For cadastral purposes in Ghana, using GNG coordinates is common. WGS2GNG-Converter makes it straightforward to transform coordinates obtained from GPS devices in WGS84 to the Ghana National Grid. Save time and effort with a simple CSV preparation and a single command.

### ESPG Standard for Accuracy

The tool is built on the widely accepted ESPG standard, ensuring accurate and reliable coordinate transformations. No need for manual calculations or dealing with intricate coordinate systems – let WGS2GNG-Converter handle it for you.

### Example Usage

1. **Prepare Your Data:**
   - Organize your WGS84 coordinates in a CSV file. Name it `input_coordinates.csv`.

   Example CSV Format (`input_coordinates.csv`):

   ```plaintext
   Longitude,Latitude
   -3.2169,7.1309
   -0.7605,10.9257
   # ... additional coordinates
   ```

2. **Run the coordinate_conversion.py script**
   - The tool will generate output_transformed_coordinates.csv containing the transformed GNG coordinates.
