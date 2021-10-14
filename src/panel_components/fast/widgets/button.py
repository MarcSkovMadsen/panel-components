from ...shared.widgets.button import ButtonBase
from .widget import Widget
import param

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
    "light": "lightweight"
}
class Button(Widget, ButtonBase):
    appearance = param.ObjectSelector(
        default=DEFAULT_FAST_BUTTON_APPEARANCE,
        objects=FAST_BUTTON_APPEARENCES,
        doc="""Determines the appearance of the button. One of `accent`, `lightweight`, `neutral`,
        `outline` or `stealth`. Defaults to `neutral`.""",
        allow_None=True,
    )
    autofocus = param.Boolean(
        default=False,
        doc="""The autofocus attribute. Defaults to `False`""",
    )

    _template="""
<fast-button id="button" class="${_css_names}" onclick="${script('click')}">{{name}}</fast-button>
"""

    _scripts = {
        **ButtonBase._scripts,
        "render": ButtonBase._scripts["render"] + "\n" + """
button.appearance=data.appearance;
button.autofocus=data.autofocus;
""",
        "appearance": "button.appearance=data.appearance",
        "autofocus": "button.autofocus=data.autofocus",
    }

    def _handle_button_type_changed(self, event=None):
        self.appearance = BUTTON_TYPE_TO_APPEARANCE[event.new]

if __name__.startswith("bokeh"):
    Button().explorer().servable()