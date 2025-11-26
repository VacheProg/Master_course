import pandas as pd

import pandas as pd
import numpy as np

def analyze_cell_regions(cell_df, grid_df):
    # Step 1: Assign region to each cell
    assigned_regions = []

    for _, cell in cell_df.iterrows():
        cell_center_x = (cell["x_min"] + cell["x_max"]) / 2
        cell_center_y = (cell["y_min"] + cell["y_max"]) / 2

        region_found = None
        for _, reg in grid_df.iterrows():
            if (reg["x_min"] <= cell_center_x <= reg["x_max"] and
                reg["y_min"] <= cell_center_y <= reg["y_max"]):
                region_found = reg["region"]
                break

        assigned_regions.append(region_found)

    cell_df["region"] = assigned_regions

    # Step 2: Summary dataframe: region → number of cells
    region_counts_df = cell_df.groupby("region")["cell_name"].count().reset_index()
    region_counts_df.columns = ["region", "num_cells"]

    # Step 3: Create pivot-style dataframe: region as column → cell names
    region_groups = cell_df.groupby("region")["cell_name"].apply(list)

    # find longest region list for padding
    max_len = max(len(v) for v in region_groups)

    padded = {}
    for region, names in region_groups.items():
        if len(names) < max_len:
            names = names + [np.nan] * (max_len - len(names))
        padded[region] = names

    region_table_df = pd.DataFrame(padded)

    return region_counts_df, region_table_df


def main(cell_path, grid_path):
    cell_df = pd.read_csv(cell_path)
    grid_df = pd.read_csv(grid_path)
    cell_df['x_max'] = cell_df['x']+cell_df['width']
    cell_df['y_max'] = cell_df['y']+cell_df['height']
    cell_df['x_min'] = cell_df['x']
    cell_df['y_min'] = cell_df['y']
    analyze_cell_regions(cell_df, grid_df)
    cell_df_A = cell_df[(cell_df['x_max'] < grid_df["x_max"][0]) & (cell_df['y_max']<grid_df["y_max"][0])]
    print('a')

if __name__ == "__main__":
    cell_path = "cells.csv"
    grid_path = "grid.csv"
    main(cell_path, grid_path)