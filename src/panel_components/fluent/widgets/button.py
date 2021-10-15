from ...fast.widgets.button import Button as Button
from .widget import Widget

class Button(Widget, Button):
    _template="""
<fluent-button id="component" onclick="${script('click')}">${name}</fluent-button>
<fluent-tooltip anchor="component-${id}">${tooltip}</fluent-tooltip>
<div>
    <fluent-button id="anchor" style="height: 40px; width: 100px; margin: 100px; background: green;">Hover me</fluent-button>
    <fluent-tooltip anchor="anchor">Tooltip text</fluent-tooltip>
</div>
"""

    @classmethod
    def example(cls):
        return cls(name="Fluent Button", tooltip="Click Me!", button_type="primary")