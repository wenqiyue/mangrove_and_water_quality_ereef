# Welcome to our project!

Project title: Mangrove and_Water Quality, eReef
Project overview: Investigate effect of mangroves on water quality using data from the eReefs project

This project is taken as part of University of Sydney's ENVI 5809 Environmental Sinulation Modelling course, taught by Prof. Tristan Salles

Group member: Ruiqi Luo, Cong Wang, Kexin Yang, Wenqi Yue

We explored datasets provided by eReef's simulation output to investigate changes in water quality indicators
that could potentially linked to mangrove damage and recovery at HinchinbrooK Island, Queensland, Australia following Cyclone Yasi at 2011-02-03

## Scientific Question:
1. Examine which water quality indicator are affected by mangrove destruction around Hinchinbrook Island after Cyclone Yasi
2. Investigate the change in water quality data over time as mangroves gradually recover after the cyclone
3. Explore spatial variations of data at different monitoring points around Hinchinbrook Island. Also compare to average values across eReef's study region (area of Great Barrier Reef,  around lon 142E to 157E, lat 7S- 29S)

## Data source
We performed analysis on Water quality data extracted from the eReef project simulation output [https://www.ereefs.org.au/]. We used data from the Hydyodynamic model v4 and Biogeochemocal model, both at 4km resolution.

## File description:

**Jupyter Notebooks:**
* explore_2d_data.ipynb: explore data set, draw 2d (lat-lon) colormesh representing data of variables
* gen_gif_monthly.ipynb: generate histogram of 2d lat-lon data plot over a time range
* analyze_time_series.ipynb (main content): extract and plot time series over
* calculate_correlation.ipynb
