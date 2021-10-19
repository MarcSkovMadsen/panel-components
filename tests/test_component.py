"""Test of the Shared Component Class"""
import param
from panel.widgets import Button

from panel_components.shared.component import Component


class MyComponent(Component):  # pylint: disable=too-many-ancestors
    """Dummy Component for Testing"""

    b = param.Integer()
    _c = param.Integer()
    a = param.Integer()

    @classmethod
    def example(cls):
        return Button(name="Run Pipeline")


def test_can_sort_controls():
    """Test that the _sort_controls function works"""
    # Given
    component = MyComponent()
    controls = component.controls()
    # When
    component._sort_controls(controls)  # pylint: disable=protected-access
    # then
    assert controls[0][0].name == ""
    assert controls[0][1].name == "A"
    assert controls[0][2].name == "B"
    assert len(controls[0]) == 3  # I.e. _c has been removed
