import panel as pn
import pytest

from panel_components.ant.widgets import AntButton
from panel_components.bootstrap.widgets import BootstrapButton
from panel_components.fast.widgets import FastButton
from panel_components.fluent.widgets import FluentButton
from panel_components.html.widgets import HTMLButton
from panel_components.material.widgets import MaterialButton
from panel_components.panel.widgets import Button
from panel_components.shared.widgets.button import ButtonBase
from panel_components.shoelace.widgets import ShoelaceButton
from panel_components.wired.widgets import WiredButton

BUTTONS = (
    AntButton,
    BootstrapButton,
    Button,
    FastButton,
    FluentButton,
    HTMLButton,
    MaterialButton,
    ShoelaceButton,
    WiredButton,
)


@pytest.mark.parametrize("cls", BUTTONS)
def test_button(cls):
    button = cls(name="Click Me", disabled=True)

    assert button.name == "Click Me"
    assert isinstance(button, ButtonBase)
    assert button.clicks == 0
    assert button.value is False
    assert button.disabled

    value = {}

    @pn.depends(event=button.param.value, watch=True)
    def handle(event):
        value["value"] = event

    button.clicks += 1
    assert value

    for button_type in button.param.button_type.objects:
        button.button_type = button_type

    button.example()
    button.explorer()
