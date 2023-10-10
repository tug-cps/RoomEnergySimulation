import connexion
from flask import abort

from app.models.t_simulation_parameters import TSimulationParameters


def simulation_get():
    """Get a list of all simulations

    :rtype: Union[List[TSimulation], Tuple[List[TSimulation], int], Tuple[List[TSimulation], int, Dict[str, str]]
    """
    return []


def simulation_id_get(id):
    """Get simulation result by id

    :param id:
    :type id: str

    :rtype: Union[TSimulation, Tuple[TSimulation, int], Tuple[TSimulation, int, Dict[str, str]]
    """
    abort(404)
    return 'do some magic!'


def simulation_post(t_simulation_parameters=None):
    """Start a simulation

    :param t_simulation_parameters: Simulation parameters
    :type t_simulation_parameters: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    abort(500)
    if connexion.request.is_json:
        t_simulation_parameters = TSimulationParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
