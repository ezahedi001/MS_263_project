# Package ID: knb-lter-sbc.145.1 Cataloging System:https://pasta.edirepository.org.
# Data set title: SBC LTER: Sea urchin foraging rates on giant kelp.
# Data set creator:    - Santa Barbara Coastal LTER 
# Data set creator:  Bartholomew DiFiore -  
# Data set creator:  Mae Rennick -  
# Data set creator:  Joseph Curtis -  
# Data set creator:  Daniel C Reed -  
# Data set creator:  Adrian Stier -  
# Contact:    - Information Manager, Santa Barbara Coastal LTER   - sbclter@msi.ucsb.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-sbc/145/1/adddbb021b16819a5fbac2475b5478b9".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "date",     
                    "trial_number",     
                    "p_r",     
                    "trial_id",     
                    "total_time",     
                    "tank",     
                    "urchin_density",     
                    "urchin_size",     
                    "urchin_mass",     
                    "kelp_in",     
                    "kelp_out",     
                    "mortality"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={ 
#             'date':'str' ,  
#             'trial_number':'str' ,  
#             'p_r':'str' ,  
#             'trial_id':'str' , 
#             'total_time':'float' ,  
#             'tank':'str' , 
#             'urchin_density':'int' , 
#             'urchin_size':'int' , 
#             'urchin_mass':'int' , 
#             'kelp_in':'float' , 
#             'kelp_out':'float' , 
#             'mortality':'int'  
#        }
          ,parse_dates=[
                        'date',
                ] 
    )
# Coerce the data into the types specified in the metadata 
# Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
# This new column is added to the dataframe but does not show up in automated summaries below. 
dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))  
dt1.trial_number=dt1.trial_number.astype('category')  
dt1.p_r=dt1.p_r.astype('category')  
dt1.trial_id=dt1.trial_id.astype('category') 
dt1.total_time=pd.to_numeric(dt1.total_time,errors='coerce')  
dt1.tank=dt1.tank.astype('category') 
dt1.urchin_density=pd.to_numeric(dt1.urchin_density,errors='coerce',downcast='integer') 
dt1.urchin_size=pd.to_numeric(dt1.urchin_size,errors='coerce',downcast='integer') 
dt1.urchin_mass=pd.to_numeric(dt1.urchin_mass,errors='coerce',downcast='integer') 
dt1.kelp_in=pd.to_numeric(dt1.kelp_in,errors='coerce') 
dt1.kelp_out=pd.to_numeric(dt1.kelp_out,errors='coerce') 
dt1.mortality=pd.to_numeric(dt1.mortality,errors='coerce',downcast='integer') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.date.describe())               
print("--------------------\n\n")
                    
print(dt1.trial_number.describe())               
print("--------------------\n\n")
                    
print(dt1.p_r.describe())               
print("--------------------\n\n")
                    
print(dt1.trial_id.describe())               
print("--------------------\n\n")
                    
print(dt1.total_time.describe())               
print("--------------------\n\n")
                    
print(dt1.tank.describe())               
print("--------------------\n\n")
                    
print(dt1.urchin_density.describe())               
print("--------------------\n\n")
                    
print(dt1.urchin_size.describe())               
print("--------------------\n\n")
                    
print(dt1.urchin_mass.describe())               
print("--------------------\n\n")
                    
print(dt1.kelp_in.describe())               
print("--------------------\n\n")
                    
print(dt1.kelp_out.describe())               
print("--------------------\n\n")
                    
print(dt1.mortality.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/knb-lter-sbc/145/1/5fea89735f07cf6aefc2b239518e6120".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,storage_options={'User-Agent':'EDI_CodeGen'}
          ,skiprows=1
            ,sep=","  
           , names=[
                    "trial_id",     
                    "sp",     
                    "urchin_density",     
                    "size_class",     
                    "test_diameter",     
                    "mass",     
                    "kelp_in",     
                    "kelp_out",     
                    "time_ran"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'trial_id':'str' ,  
#             'sp':'str' , 
#             'urchin_density':'int' ,  
#             'size_class':'str' , 
#             'test_diameter':'int' , 
#             'mass':'float' , 
#             'kelp_in':'float' , 
#             'kelp_out':'float' , 
#             'time_ran':'float'  
#        }
            ,na_values={
                  'mass':[
                          'NA',],} 
            
    )
# Coerce the data into the types specified in the metadata  
dt2.trial_id=dt2.trial_id.astype('category')  
dt2.sp=dt2.sp.astype('category') 
dt2.urchin_density=pd.to_numeric(dt2.urchin_density,errors='coerce',downcast='integer')  
dt2.size_class=dt2.size_class.astype('category') 
dt2.test_diameter=pd.to_numeric(dt2.test_diameter,errors='coerce',downcast='integer') 
dt2.mass=pd.to_numeric(dt2.mass,errors='coerce') 
dt2.kelp_in=pd.to_numeric(dt2.kelp_in,errors='coerce') 
dt2.kelp_out=pd.to_numeric(dt2.kelp_out,errors='coerce') 
dt2.time_ran=pd.to_numeric(dt2.time_ran,errors='coerce') 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt2.trial_id.describe())               
print("--------------------\n\n")
                    
print(dt2.sp.describe())               
print("--------------------\n\n")
                    
print(dt2.urchin_density.describe())               
print("--------------------\n\n")
                    
print(dt2.size_class.describe())               
print("--------------------\n\n")
                    
print(dt2.test_diameter.describe())               
print("--------------------\n\n")
                    
print(dt2.mass.describe())               
print("--------------------\n\n")
                    
print(dt2.kelp_in.describe())               
print("--------------------\n\n")
                    
print(dt2.kelp_out.describe())               
print("--------------------\n\n")
                    
print(dt2.time_ran.describe())               
print("--------------------\n\n")
                    
                    
                




