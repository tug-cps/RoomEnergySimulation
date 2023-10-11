import os

import joblib
import pandas as pd
from celery import shared_task

absolute_path = os.path.dirname(__file__)


@shared_task(ignore_result=False)
def simulate(
    wall_insulation_thickness: float,
    wall_u_value: float,
    window_u_value: float,
    window_shgc: float,
    window_shading_control: float,
    thermostat_setpoint: float,
) -> dict:
    X = pd.DataFrame(
        {
            "Insulation thickness (m)": [wall_insulation_thickness],
            "Wall U-value (W/m2K)": wall_u_value,
            "Window U-value (W/m2K)": [window_u_value],
            "Window SHGC (ratio)": [window_shgc],
            "Shading control (W/m2)": [window_shading_control],
            "Thermostat settings offset (C)": [thermostat_setpoint],
        }
    )
    model_path = os.path.join(absolute_path, "../ml/linear_model_6_features.pkl")
    model = joblib.load(model_path)
    predictions = model.predict(X)

    return {"heating_energy_consumption": predictions[0][0], "cooling_energy_consumption": predictions[0][1]}
