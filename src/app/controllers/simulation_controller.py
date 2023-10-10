import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from app.models.t_simulation import TSimulation  # noqa: E501
from app.models.t_simulation_parameters import TSimulationParameters  # noqa: E501
from app import util


def simulation_get():  # noqa: E501
    """Get a list of all simulations

     # noqa: E501


    :rtype: Union[List[TSimulation], Tuple[List[TSimulation], int], Tuple[List[TSimulation], int, Dict[str, str]]
    """
    return 'do some magic!'


def simulation_id_get(id):  # noqa: E501
    """Get simulation result by id

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[TSimulation, Tuple[TSimulation, int], Tuple[TSimulation, int, Dict[str, str]]
    """
    return 'do some magic!'


def simulation_post(t_simulation_parameters=None):  # noqa: E501
    """Start a simulation

     # noqa: E501

    :param t_simulation_parameters: Simulation parameters
    :type t_simulation_parameters: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        t_simulation_parameters = TSimulationParameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
