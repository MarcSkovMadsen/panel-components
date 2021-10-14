from panel.widgets.button import BUTTON_TYPES

from ...shared.widgets.button import ButtonBase
from .widget import Widget

if not "light" in BUTTON_TYPES:
    BUTTON_TYPES.append("light")

CSS_NAMES_DEFAULT = ["bk", "bk-btn"]
# Widget, _Button
class Button(Widget, ButtonBase):
    _template="""
<div id="buttonGroup" class="bk bk-btn-group">
    <button id="button" class="${_css_names}" onclick="${script('click')}">{{name}}</button>
</div>"""

    def _get_css_names(self):
        return CSS_NAMES_DEFAULT  + ["bk-btn-" + self.button_type] + super()._get_css_names()

if __name__.startswith("bokeh"):
    Button().explorer().servable()
