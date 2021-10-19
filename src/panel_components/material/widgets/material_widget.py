"""# Material Widget Functionality

Provides the MaterialWidget and MaterialWidgetGenerator
"""
from ...shared.component import ReactComponentGenerator
from ..material_component import MaterialComponent


class MaterialWidget(MaterialComponent):  # pylint: disable=too-few-public-methods
    """Your Material Widgets should inherits this"""


class MaterialWidgetGenerator(ReactComponentGenerator):
    """This class can generate the _template and _scripts for ReactiveHTML MaterialUI widgets"""

    _tooltip_element = (
        """element=React.createElement("""
        """MaterialUI.Tooltip,"""
        """{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},"""
        """element"""
        """);"""
    )
