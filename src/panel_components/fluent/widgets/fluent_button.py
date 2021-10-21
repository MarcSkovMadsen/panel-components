"""# FluentButton

See See https://github.com/microsoft/fluentui/tree/master/packages/web-components
"""
from ...fast.widgets.fast_button import FastButton
from .fluent_widget import FluentWidget


class FluentButton(FluentWidget, FastButton):  # pylint: disable=too-many-ancestors
    """# FluentButton

    See See https://github.com/microsoft/fluentui/tree/master/packages/web-components"""

    _template = """\
<fluent-button id="component" onclick="${script('click')}">${name}</fluent-button>
<fluent-tooltip anchor="component-${id}">${tooltip}</fluent-tooltip>
"""


    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="primary")
