Title: About Me
Date: 2024-05-23
Category: About Me
Tags: Python, Data Analysis, GIS, Drones
Slug: about-me
Authors: Brian Estevez
Summary: Hello!

Hello! My name is Brian Estevez. My background is as an academic rare blood disease cell and molecular pharmacologist. Came into Geospatial data by accident while working as a life science consultant making simple maps of medical claims volume and hospitals treating rare diseases. 

I enjoy learning Python programming, Unmanned Aerial Vehicle (UAV) / Drone technology, and Geographical Information Systems (GIS).
This site is a place to share in the exploration of these topics.

### **Key projects:**

- **UAV-Based Road Mapping and Infrastructure Extraction**
This project demonstrates how UAV imagery can be used to map and assess road conditions and adjacent infrastructure. I collected imagery with a drone, processed the imagery into a point cloud using Pix4Dmatic, then imported it into Pix4Dsurvey to automatically detect road centerlines, manholes, storm drains, and lamp posts. These features were exported as shapefiles and finalized in ArcGIS Pro, symbology added and integrated with the orthomosaic for presentation. This workflow demonstrates how UAVs and intelligent extraction tools can support efficient, repeatable infrastructure mapping for local governments. (3D animation example and map below)
<video width="600" controls>
  <source src="{static}/videos/CitySavage_Road.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

<img src= "{static}/images/CitySavageRoadsExample.svg" alt ="UAV images processed in Pix4DMatic with objects automatically detected in Pix4DSurvey. Mapping in ArcGIS Pro" style= " width 350px; height: 350px;">

- **UAV-Based Road Mapping with Open-Source Photogrammetry Software**
This project is a variation of the road infrastructure mapping one above. I flew the same mission flight path but this time also layed down and surveyed ground control points using a GNSS receiver. Another key difference was the image processing pipeline. Here OpenDroneMap command line version was used to construct the orthomosaic and georeference the photos. This workflow demonstrates two main points: First, ODM uses WGS84-based referencing as the default, which is not configurable, so results must be projected to the local CS. Second, it is possible to achieve high-quality and potentially survey-grade mapping results (here ~4 cm absolute horizontal error) using open-source photogrammetry software and ground control points.


<img src= "{static}/images/ODM_GCP_Corrected_NAD83Example.svg" alt ="Orthomosaic created in OpenDroneMap with Ground Control Points and projected in ArcGIS Pro to NAD83 UTM Zone15" style= " width 350px; height: 350px;">

<video width="600" controls>
<source src = "{static}/videos/ODM_QualityReport_Example.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>


- **Scott County Food Resource Map (ArcGIS Experience Builder)**
Inspired by Hennepin County’s public food resource map, this project expands Scott County’s internal dataset into a public-facing tool. I discovered, through volunteering with Meals on Wheels, that local service areas like Savage weren’t fully represented. I extended their dataset, aligned my edits to their schema, resolved symbology, and published an interactive map using Experience Builder. A local .gdb copy preserves source attribution for future collaboration. [Link](https://experience.arcgis.com/experience/734735727e6741f59f0efe021dcbc89c/)

- **Groundwater Contamination Dashboard** 
Integrated state well data with ArcGIS Pro and Python [Link](https://www.arcgis.com/apps/dashboards/e53b8dee993d458c858cb53a1ed56b99)

- **Custom ArcPy Tools** 
Developed scripts and workflows for automating geoprocessing [Link](https://github.com/estevezb/GIS-Tools/tree/main/ArcGISPro/Arcpy) 
ETL script to process and align CSV inputs using a feature class schema with GUI-guided workflow: 

<video width="600" controls>
<source src = "https://github.com/estevezb/GIS-Tools/raw/main/VideoExamples/ArcGIS_Pro_DataIngestion_Demo1.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>



- **Disaster Damage Assessment**
 Applied ArcGIS Deep Learning for hurricane damage mapping [Link](https://estevezb.github.io/Savage-MN-GIS/category/disasters.html) and online map here: [AGOL](https://www.arcgis.com/home/item.html?id=a98ff2773b7c4e3eb36b6a1a7f1288ef)

- **Search Database for GIS Data** 
Developed a search engine web app allows users to query for trusted GIS databases: [Link](https://estevezb.github.io/Savage-MN-GIS/category/gis-data-sources.html)
