import connexion
from celery.result import AsyncResult
from flask import abort

from app.models.t_simulation_parameters import TSimulationParameters  # noqa: E501
from app.models.t_simulation_response import TSimulationResponse
from app.models.t_simulation_result import TSimulationResult
from app.tasks.simulation_tasks import simulate


def simulation_id_get(id_: str):  # noqa: E501
    """Get simulation result by id

    :param id_:
    :type id_: str

    :rtype: Union[TSimulation, Tuple[TSimulation, int], Tuple[TSimulation, int, Dict[str, str]]
    """
    result = AsyncResult(id_)
    if result.state == "PENDING":
        abort(404)

    return TSimulationResult(
        id=result.id,
        heating_energy_consumption=result.result["heating_energy_consumption"] if result.ready() else None,
        cooling_energy_consumption=result.result["cooling_energy_consumption"] if result.ready() else None,
        date_done=result.date_done,
        status=result.state,
    ).to_dict()


def simulation_post(t_simulation_parameters=None):  # noqa: E501
    """Start a simulation

     # noqa: E501

    :param t_simulation_parameters: Simulation parameters
    :type t_simulation_parameters: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        t_simulation_parameters = TSimulationParameters.from_dict(connexion.request.get_json())  # noqa: E501

    result = simulate.delay(
        t_simulation_parameters.wall_insulation_thickness,
        t_simulation_parameters.wall_u_value,
        t_simulation_parameters.window_u_value,
        t_simulation_parameters.window_shgc,
        t_simulation_parameters.window_shading_control,
        t_simulation_parameters.thermostat_setpoint,
    )
    return TSimulationResponse(id=result.id).to_dict()
