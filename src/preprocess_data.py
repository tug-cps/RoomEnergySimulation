import pandas as pd
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv('../data/output_files_heating_two_parameters_thickness_U-value.csv')
    df = df.astype(float)

    df = df.rename(columns={'Unnamed: 0': 'U-values'})
    df = df.set_index('U-values')

    df_new = pd.DataFrame()
    df_new['insulation_thickness'] = []
    df_new['u_values'] = []
    df_new['annual_energy_use'] = []

    for col in df.columns:
        for idx in df.index:
            df_new = df_new.append({'insulation_thickness': col, 'u_values': idx, 'annual_energy_use': df.loc[idx, col]}, ignore_index=True)

    df_new.to_csv('../data/preproccesed.csv')