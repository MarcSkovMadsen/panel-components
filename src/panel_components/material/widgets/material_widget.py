"""# Material Widget Functionality

Provides the MaterialWidget
"""
import param

from ..material_component import MaterialComponent

TOOLTIP_PLACEMENT_DEFAULT = "bottom"
TOOLTIP_PLACEMENTS = [
    "bottom-end",
    "bottom-start",
    "bottom",
    "left-end",
    "left-start",
    "left",
    "right-end",
    "right-start",
    "right",
    "top-end",
    "top-start",
    "top",
]


class MaterialWidget(
    MaterialComponent
):  # pylint: disable=too-few-public-methods, too-many-ancestors
    """All Material widgets should inherit from this class"""

    tooltip = param.String("Tooltip")
    tooltip_placement = param.Selector(default="bottom", objects=TOOLTIP_PLACEMENTS)
