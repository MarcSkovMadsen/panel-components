"""# Ant Design Widget Functionality

Provides the AntWidget and AntWidgetGenerator
"""
from ...shared.component import ReactComponentGenerator
from ..ant_component import AntComponent


class AntWidget(AntComponent): # pylint: disable=too-few-public-methods
    """Your Ant Widgets should inherits this"""


class AntWidgetGenerator(ReactComponentGenerator):
    """Your Ant Widgets can use this to generate ReactiveHTML _template and _scripts"""
    _tooltip_element = (
        "element=React.createElement("
        "antd.Tooltip,"
        "{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},"
        "element);"
    )
