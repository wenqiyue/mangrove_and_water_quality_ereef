# Plot extent of area under study in cartopy

# Import libraries
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Define function
def show_area_ext(lonlat_ext, lons=[], lats=[], sites=[], figsize=(12,8)):

    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0,0,1,1], projection=ccrs.PlateCarree())
    ax.axis('square')
    ax.set_extent(lonlat_ext)

    ax.coastlines()
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.gridlines(draw_labels=['bottom', 'left'], xlabel_style={'size':15}, ylabel_style={'size':15})

    n = len(sites)

    for i in range(n):
        ax.plot(lons[i], lats[i], 'ro' )
        ax.text(lons[i]+0.1, lats[i]+0.1, sites[i])

    return fig, ax


