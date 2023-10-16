
import os
import pandas as pd

def combine_csv():
    # Iterate through all files in the folder
    for file in os.listdir("folder"):
        # Read each file as a dataframe
        df = pd.read_csv(os.path.join("folder", file))
        
        # Combine all dataframes into a single one
        combined_df = pd.concat([df for df in [df] ], ignore_index=True)
        
        # Return the combined dataframe
        return combined_df

