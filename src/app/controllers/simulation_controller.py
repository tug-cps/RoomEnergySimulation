import connexion
from celery.result import AsyncResult

from app.models.t_simulation_parameters import TSimulationParameters  # noqa: E501
from app.tasks.simulation_tasks import simulate
from flask import abort


def simulation_id_get(id_: str):  # noqa: E501
    """Get simulation result by id

    :param id:
    :type id: str

    :rtype: Union[TSimulation, Tuple[TSimulation, int], Tuple[TSimulation, int, Dict[str, str]]
    """
    result = AsyncResult(id_)
    if result.state == "PENDING":
        abort(404)

    return {
        "id": result.id,
        "result": result.result if result.ready() else None,
        "status": result.state,
        "date_done": result.date_done,
    }


def simulation_post(t_simulation_parameters=None):  # noqa: E501
    """Start a simulation

     # noqa: E501

    :param t_simulation_parameters: Simulation parameters
    :type t_simulation_parameters: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        t_simulation_parameters = TSimulationParameters.from_dict(connexion.request.get_json())  # noqa: E501

    result = simulate.delay()
    return {"id": result.id}
