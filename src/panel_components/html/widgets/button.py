from panel.widgets.button import BUTTON_TYPES

from ...shared.widgets.button import ButtonBase
from .widget import Widget

if not "light" in BUTTON_TYPES:
    BUTTON_TYPES.append("light")

class Button(Widget, ButtonBase):
    _template="""<button id="component" onclick="${script('click')}">${name}</button>"""

    def _get_css_names(self):
        return  ["btn-" + self.button_type] + super()._get_css_names()

    @classmethod
    def example(cls):
        return cls(name="HTML Button", tooltip="Click Me!")
