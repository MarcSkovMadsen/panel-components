"""A Panel Button

Reimplementation of the original using ReactiveHTML"""
from panel.widgets.button import BUTTON_TYPES

from ...shared.widgets.button import ButtonBase
from .widget import Widget

if "light" not in BUTTON_TYPES:
    BUTTON_TYPES.append("light")

CSS_NAMES_DEFAULT = ["bk", "bk-btn"]
# Widget, _Button
class Button(Widget, ButtonBase):  # pylint: disable=too-many-ancestors
    """A Panel Button

    Reimplementation of the original using ReactiveHTML"""

    _template = """
<div id="buttonGroup" class="bk bk-btn-group">
    <button id="component" onclick="${script('click')}">${name}</button>
</div>"""

    def _get_css_names(self):
        return CSS_NAMES_DEFAULT + ["bk-btn-" + self.button_type] + super()._get_css_names()

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="success")
