from panel_components.shared.widgets.button import ButtonBase
from panel_components.panel.widgets import Button as PanelButton
from panel_components.html.widgets import Button as HTMLButton
from panel_components.fast.widgets import Button as FastButton
from panel_components.wired.widgets import Button as WiredButton

import pytest
import panel as pn

BUTTONS = (
    FastButton,
    HTMLButton,
    PanelButton,
    WiredButton,
)

@pytest.mark.parametrize("cls", BUTTONS)
def test_button(cls):
    button = cls(name="Click Me", disabled=True)

    assert button.name == "Click Me"
    assert isinstance(button, ButtonBase)
    assert button.clicks==0
    assert button.value is False
    assert button.disabled

    value = {}
    @pn.depends(event=button.param.value, watch=True)
    def handle(event):
        value["value"]=event

    button.clicks+=1
    assert value

    for button_type in button.param.button_type.objects:
        button.button_type = button_type

    button.example()
    button.explorer()