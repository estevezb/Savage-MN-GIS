README: Enhanced Food Resources GIS Layer for Scott County
----------------------------------------------------------

Submitted by: Brian Estevez  
Date: May 16, 2025  
Contact: bestevez100@gmail.com OR brian.estevez@du.edu  
Portfolio: https://estevezb.github.io/Savage-MN-GIS/pages/about-me.html

Purpose:
--------
This package includes an enhanced version of the Scott County food resource dataset. The goal of this project is to support the development of a public-facing food resource map, modeled after Hennepin County’s Experience Builder map. My contributions focus on expanding coverage for home-delivered meals and additional service providers not currently included in the public dataset.

Key Enhancements:
-----------------
- Added 22 new records for **Meals on Wheels** and **Open Arms** service locations
- Verified service relevance based on volunteer experience and independent research
- Used `TYP = "Food Program"` to match existing schema
- Added a `Service Type` field to distinguish "Home Delivered Meals" where applicable
- Added a `SOURCE` field to distinguish between original Scott County data and new records


Source Data for Enhancements:
-----------------
- Open Arms : https://www.openarmsmn.org/get-meals/ourdeliveryarea/
- Meals On Wheels : https://www.mealsonwheelsamerica.org/signup/aboutmealsonwheels/find-programs?filter=55378
- Scott County food : resource Guide https://www.scottcountymn.gov/DocumentCenter/View/21414/Full-Food-Resource-Guide-12-23

Files Included:
---------------
- `Enhanced_FoodResources_ScottCo.gdb/`  
    File geodatabase containing the updated feature class with all enhancements

- `Enhanced_FoodResources.lyrx`  
    Layer file that preserves symbology, pop-ups, and classification by TYP

- `Added_Records.csv`  
    A flat file listing all newly added entries for transparency and review

- `Scott_County_Resources.mapx` *(optional)*  
    ArcGIS Pro map document file (if included) showing how data is used in layout

- 'DataSources_List.csv
	List of Data source URLs (shown above)

Instructions:
-------------
To view the data with symbology:
1. Add the layer from `Enhanced_FoodResources_ScottCo.gdb` into a new map
2. Apply the symbology by importing `Enhanced_FoodResources.lyrx`
   - Or simply add the `.lyrx` file directly to your map

To review only the new records:
- Filter the attribute table by `SOURCE = 'User Added'`
- Or view the full list in `Added_Records.csv`

Disclaimer:
-----------
All added data has been sourced to the best of my knowledge, and field names have been matched to the Scott County schema for easy review and integration. Please feel free to reach out with any questions (bestevez100@gmail.com), suggested edits, or if you'd like a version published to ArcGIS Online.

Thank you for maintaining accessible and high-quality GIS data for the public.
