import param

from ...shared.widgets.button import ButtonBase
from .fast_widget import FastWidget

FAST_BUTTON_APPEARENCES = [
    "accent",
    "lightweight",
    "neutral",
    "outline",
    "stealth",
]
DEFAULT_FAST_BUTTON_APPEARANCE = "neutral"
BUTTON_TYPE_TO_APPEARANCE = {
    "default": "neutral",
    "primary": "accent",
    "success": "outline",
    "warning": "stealth",
    "danger": "accent",
    "light": "lightweight",
}


class FastButton(FastWidget, ButtonBase):
    appearance = param.ObjectSelector(
        default=DEFAULT_FAST_BUTTON_APPEARANCE,
        objects=FAST_BUTTON_APPEARENCES,
        doc="""Determines the appearance of the button. One of `accent`, `lightweight`, `neutral`,
        `outline` or `stealth`. Defaults to `neutral`.""",
        allow_None=True,
    )

    # For some unknown reason using ${_css_names} gives a js error
    _template = """
<fast-button id="component" onclick="${script('click')}">${name}</fast-button>
"""

    _scripts = {
        **ButtonBase._scripts,
        "render": ButtonBase._scripts["render"]
        + "\n"
        + """
component.appearance=data.appearance;
""",
        "appearance": "component.appearance=data.appearance",
    }

    def _handle_button_type_changed(self, event=None):
        if event:
            self.appearance = BUTTON_TYPE_TO_APPEARANCE[event.new]
        else:
            self.appearance = BUTTON_TYPE_TO_APPEARANCE[self.button_type]

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="primary")

    def _handle_css_names_changed(self, event=None):
        return super()._handle_css_names_changed(event=event)
