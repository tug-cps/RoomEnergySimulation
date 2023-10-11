from celery import shared_task


@shared_task(ignore_result=False)
def simulate(
    wall_insulation_thickness: float,
    window_u_value: float,
    window_shgc: float,
    window_shading_control: float,
    thermostat_setpoint: float,
) -> dict:
    # FIXME:
    # load model
    # start simulation
    # return value
    return {"heating_energy_consumption": 1234, "cooling_energy_consumption": 5678}
