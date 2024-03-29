from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model import Model
from app import util


class TSimulationParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        wall_insulation_thickness=None,
        wall_u_value=None,
        window_u_value=None,
        window_shgc=None,
        window_shading_control=None,
        thermostat_setpoint=None,
    ):  # noqa: E501
        """TSimulationParameters - a model defined in OpenAPI

        :param wall_insulation_thickness: The wall_insulation_thickness of this TSimulationParameters.  # noqa: E501
        :type wall_insulation_thickness: float
        :param wall_u_value: The wall_u_value of this TSimulationParameters.  # noqa: E501
        :type wall_u_value: float
        :param window_u_value: The window_u_value of this TSimulationParameters.  # noqa: E501
        :type window_u_value: float
        :param window_shgc: The window_shgc of this TSimulationParameters.  # noqa: E501
        :type window_shgc: float
        :param window_shading_control: The window_shading_control of this TSimulationParameters.  # noqa: E501
        :type window_shading_control: float
        :param thermostat_setpoint: The thermostat_setpoint of this TSimulationParameters.  # noqa: E501
        :type thermostat_setpoint: float
        """
        self.openapi_types = {
            "wall_insulation_thickness": float,
            "wall_u_value": float,
            "window_u_value": float,
            "window_shgc": float,
            "window_shading_control": float,
            "thermostat_setpoint": float,
        }

        self.attribute_map = {
            "wall_insulation_thickness": "wall_insulation_thickness",
            "wall_u_value": "wall_u_value",
            "window_u_value": "window_u_value",
            "window_shgc": "window_shgc",
            "window_shading_control": "window_shading_control",
            "thermostat_setpoint": "thermostat_setpoint",
        }

        self._wall_insulation_thickness = wall_insulation_thickness
        self._wall_u_value = wall_u_value
        self._window_u_value = window_u_value
        self._window_shgc = window_shgc
        self._window_shading_control = window_shading_control
        self._thermostat_setpoint = thermostat_setpoint

    @classmethod
    def from_dict(cls, dikt) -> "TSimulationParameters":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The T_SimulationParameters of this TSimulationParameters.  # noqa: E501
        :rtype: TSimulationParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def wall_insulation_thickness(self) -> float:
        """Gets the wall_insulation_thickness of this TSimulationParameters.

        Wall insulation thickness (m)  # noqa: E501

        :return: The wall_insulation_thickness of this TSimulationParameters.
        :rtype: float
        """
        return self._wall_insulation_thickness

    @wall_insulation_thickness.setter
    def wall_insulation_thickness(self, wall_insulation_thickness: float):
        """Sets the wall_insulation_thickness of this TSimulationParameters.

        Wall insulation thickness (m)  # noqa: E501

        :param wall_insulation_thickness: The wall_insulation_thickness of this TSimulationParameters.
        :type wall_insulation_thickness: float
        """
        if wall_insulation_thickness is None:
            raise ValueError("Invalid value for `wall_insulation_thickness`, must not be `None`")  # noqa: E501

        self._wall_insulation_thickness = wall_insulation_thickness

    @property
    def wall_u_value(self) -> float:
        """Gets the wall_u_value of this TSimulationParameters.

        Wall U-Value (W/m2K)  # noqa: E501

        :return: The wall_u_value of this TSimulationParameters.
        :rtype: float
        """
        return self._wall_u_value

    @wall_u_value.setter
    def wall_u_value(self, wall_u_value: float):
        """Sets the wall_u_value of this TSimulationParameters.

        Wall U-Value (W/m2K)  # noqa: E501

        :param wall_u_value: The wall_u_value of this TSimulationParameters.
        :type wall_u_value: float
        """
        if wall_u_value is None:
            raise ValueError("Invalid value for `wall_u_value`, must not be `None`")  # noqa: E501

        self._wall_u_value = wall_u_value

    @property
    def window_u_value(self) -> float:
        """Gets the window_u_value of this TSimulationParameters.

        Window U-value (W/m2K)  # noqa: E501

        :return: The window_u_value of this TSimulationParameters.
        :rtype: float
        """
        return self._window_u_value

    @window_u_value.setter
    def window_u_value(self, window_u_value: float):
        """Sets the window_u_value of this TSimulationParameters.

        Window U-value (W/m2K)  # noqa: E501

        :param window_u_value: The window_u_value of this TSimulationParameters.
        :type window_u_value: float
        """
        if window_u_value is None:
            raise ValueError("Invalid value for `window_u_value`, must not be `None`")  # noqa: E501

        self._window_u_value = window_u_value

    @property
    def window_shgc(self) -> float:
        """Gets the window_shgc of this TSimulationParameters.

        Window SHGC (ratio)  # noqa: E501

        :return: The window_shgc of this TSimulationParameters.
        :rtype: float
        """
        return self._window_shgc

    @window_shgc.setter
    def window_shgc(self, window_shgc: float):
        """Sets the window_shgc of this TSimulationParameters.

        Window SHGC (ratio)  # noqa: E501

        :param window_shgc: The window_shgc of this TSimulationParameters.
        :type window_shgc: float
        """
        if window_shgc is None:
            raise ValueError("Invalid value for `window_shgc`, must not be `None`")  # noqa: E501

        self._window_shgc = window_shgc

    @property
    def window_shading_control(self) -> float:
        """Gets the window_shading_control of this TSimulationParameters.

        Window shading control (W/m2)  # noqa: E501

        :return: The window_shading_control of this TSimulationParameters.
        :rtype: float
        """
        return self._window_shading_control

    @window_shading_control.setter
    def window_shading_control(self, window_shading_control: float):
        """Sets the window_shading_control of this TSimulationParameters.

        Window shading control (W/m2)  # noqa: E501

        :param window_shading_control: The window_shading_control of this TSimulationParameters.
        :type window_shading_control: float
        """
        if window_shading_control is None:
            raise ValueError("Invalid value for `window_shading_control`, must not be `None`")  # noqa: E501

        self._window_shading_control = window_shading_control

    @property
    def thermostat_setpoint(self) -> float:
        """Gets the thermostat_setpoint of this TSimulationParameters.

        Cooling/heating thermostat setpoints (C)  # noqa: E501

        :return: The thermostat_setpoint of this TSimulationParameters.
        :rtype: float
        """
        return self._thermostat_setpoint

    @thermostat_setpoint.setter
    def thermostat_setpoint(self, thermostat_setpoint: float):
        """Sets the thermostat_setpoint of this TSimulationParameters.

        Cooling/heating thermostat setpoints (C)  # noqa: E501

        :param thermostat_setpoint: The thermostat_setpoint of this TSimulationParameters.
        :type thermostat_setpoint: float
        """
        if thermostat_setpoint is None:
            raise ValueError("Invalid value for `thermostat_setpoint`, must not be `None`")  # noqa: E501

        self._thermostat_setpoint = thermostat_setpoint
