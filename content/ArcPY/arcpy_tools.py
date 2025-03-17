###======================   Check Feature Classes were created and have the expected Characteristics
import arcpy
import os 

# Instead of re-writing this we will wrap the operations into a function called def listFC_dataset_Attributes():

def listFC_dataset_Attributes(workspace=None): # accepts a workspace path parameter,By default uses the existing one if left as None
    """List feature classes in the workspace and their attributes"""
    if workspace:
        arcpy.env.workspace= workspace

    if not arcpy.env.workspace:
        print("No workspace is set! Please specify a workspace")
        return # ensures we exit the function if not workspace is set
    try:
        ## Get all the fc classes from the gdb
        list_fc = arcpy.ListFeatureClasses()
        wksp_path= arcpy.env.workspace
        print(f"Workspace is set here {wksp_path}\n")

        if not list_fc:
            print("No feature classes found in the workspace")
            return # exit the function if not fc found
        wkid_list = set()
        CS_types = set() 
        fc_counter= 0
        for fc in list_fc:
            desc= arcpy.Describe(fc) ## Use the Describe Object to access properties of a Feature class like its Spatial Reference

            sr = desc.SpatialReference
            wkid_list.add(sr.factorycode)
            CS_types.add(sr.type)
            fc_counter+=1
            
            print(f"Feature class: , {fc}, Spatial Reference name :, {sr.name}, Spatial Ref Type : {sr.type}, Geometry{desc.shapetype}, WKID: {sr.factorycode}")
            print("-"*150,"\n") # add line and space between prints
        
        print(f"\n{fc_counter} Feature classes found in the workspace path\n")
    
        if len(wkid_list) >1:
            print("Warning Different wkid detected among feature Classes: " , wkid_list)
        if len(CS_types) >1:
            print("Warning Different Coordinate Systems types found among Feature Classes: ", CS_types)
    except Exception as e:
        print(f"Error occurred. Description: {e}, Error Category: {type(e).__name__}")
    except arcpy.ExecuteError:
        arcpy.GetMessages(2)