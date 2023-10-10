import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from app.models.simulation_get_default_response_inner import SimulationGetDefaultResponseInner  # noqa: E501
from app.models.simulation_id_get200_response import SimulationIdGet200Response  # noqa: E501
from app.models.simulation_post_request import SimulationPostRequest  # noqa: E501
from app import util


def simulation_get():  # noqa: E501
    """Get a list of all simulations

     # noqa: E501


    :rtype: Union[List[SimulationGetDefaultResponseInner], Tuple[List[SimulationGetDefaultResponseInner], int], Tuple[List[SimulationGetDefaultResponseInner], int, Dict[str, str]]
    """
    return 'do some magic!'


def simulation_id_get(id):  # noqa: E501
    """Get simulation result by id

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[SimulationIdGet200Response, Tuple[SimulationIdGet200Response, int], Tuple[SimulationIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def simulation_post(simulation_post_request=None):  # noqa: E501
    """Start a simulation

     # noqa: E501

    :param simulation_post_request: Simulation parameters
    :type simulation_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        simulation_post_request = SimulationPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
