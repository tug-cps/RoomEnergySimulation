import pandas as pd
from celery import shared_task

from app.ml import model


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
    predictions = model.predict(X)

    return {"heating_energy_consumption": predictions[0][0], "cooling_energy_consumption": predictions[0][1]}
