from ...fast.widgets.fast_button import FastButton as FluentButton
from .fluent_widget import FluentWidget

class FluentButton(FluentWidget, FluentButton):
    _template="""\
<fluent-button id="component" onclick="${script('click')}">${name}</fluent-button>
<fluent-tooltip anchor="component-${id}">${tooltip}</fluent-tooltip>"""

    @classmethod
    def example(cls):
        return cls(name="Fluent Button", tooltip="Click Me!", button_type="primary")