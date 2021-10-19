"""# Material Widget Functionality

Provides the MaterialWidget
"""
from ...shared.react_generator import ReactGenerator
from ..material_component import MaterialComponent


class MaterialWidget(MaterialComponent):  # pylint: disable=too-few-public-methods
    """All Material widgets should inherit from this class"""

    @staticmethod
    def _scripts(element, properties, events, children):
        widget = ReactGenerator(
            element=element,
            properties=properties,
            events=events,
            children=children,
        )
        widget_with_tooltip = ReactGenerator(
            element="MaterialUI.Tooltip",
            properties={"title": "tooltip", "placement": "tooltip_placement"},
            children=[widget],
        )
        return widget_with_tooltip.scripts
