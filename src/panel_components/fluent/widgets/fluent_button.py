from ...fast.widgets.fast_button import FastButton
from .fluent_widget import FluentWidget


class FluentButton(FluentWidget, FastButton):
    _template = """\
<fluent-button id="component" onclick="${script('click')}">${name}</fluent-button>
<fluent-tooltip anchor="component-${id}">${tooltip}</fluent-tooltip>"""

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="primary")
