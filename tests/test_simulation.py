from unittest.mock import patch, Mock


class TestGet:
    def test_invalid_path(self, app):
        app.get("/api/v1/simulation", status=405)

    def test_empty(self, app):
        app.get("/api/v1/simulation/", status=404)

    @patch("app.controllers.simulation_controller.AsyncResult")
    def test_unknown_job(self, result: Mock, app):
        result.return_value = Mock(state="PENDING")
        app.get("/api/v1/simulation/dummy-id", status=404)

    @patch("app.controllers.simulation_controller.AsyncResult")
    def test_known_job(self, result: Mock, app):
        result.return_value = Mock(
            id="some_id",
            state="SUCCESS",
            result={"heating_energy_consumption": 1.234, "cooling_energy_consumption": 5678},
            date_done=None,
        )

        result = app.get("/api/v1/simulation/dummy-id")

        assert result
        assert result.json["id"] == "some_id"
        assert result.json["heating_energy_consumption"] == 1.234
        assert result.json["cooling_energy_consumption"] == 5678
        assert result.json["status"] == "SUCCESS"
        assert result.json["date_done"] is None


class TestPost:
    def test_invalid_path(self, app):
        app.post_json("/api/v1/simulation/", status=404)

    def test_no_arguments(self, app):
        app.post_json("/api/v1/simulation", status=400)

    def test_empty_body(self, app):
        app.post_json("/api/v1/simulation", {}, status=400)

    @patch("app.controllers.simulation_controller.simulate.delay")
    def test_missing_arguments(self, delay: Mock, app):
        body = {
            "thermostat_setpoint": 0,
            "wall_insulation_thickness": 1,
            "wall_u_value": 2,
            "window_shading_control": 3,
            "window_shgc": 4,
        }

        app.post_json("/api/v1/simulation", body, status=400)

        assert delay.assert_not_called() is None

    @patch("app.controllers.simulation_controller.simulate.delay")
    def test_valid_arguments(self, delay: Mock, app):
        delay.return_value = Mock(id="some_id")
        body = {
            "thermostat_setpoint": 0,
            "wall_insulation_thickness": 1,
            "wall_u_value": 2,
            "window_shading_control": 3,
            "window_shgc": 4,
            "window_u_value": 5,
        }

        result = app.post_json("/api/v1/simulation", body)

        assert delay.assert_called_with(1.0, 2.0, 5.0, 4.0, 3.0, 0.0) is None
        assert result
        assert result.json["id"] == "some_id"
