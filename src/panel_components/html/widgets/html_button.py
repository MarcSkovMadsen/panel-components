"""# Basic HTMLButton

See https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button
"""
from panel.widgets.button import BUTTON_TYPES

from ...shared.widgets.button import ButtonBase
from .html_widget import HTMLWidget

if "light" not in BUTTON_TYPES:
    BUTTON_TYPES.append("light")


class HTMLButton(HTMLWidget, ButtonBase):  # pylint: disable=too-many-ancestors
    """# Basic HTMLButton

    See https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button"""

    _template = """<button id="component" onclick="${script('click')}">${name}</button>"""

    def _get_css_names(self):
        return ["btn-" + self.button_type] + super()._get_css_names()

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model")
