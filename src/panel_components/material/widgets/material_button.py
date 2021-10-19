"""# MaterialButton

See https://mui.com/components/buttons/
"""
from collections import namedtuple

import param

from ...shared.widgets.button import ButtonBase
from .material_widget import MaterialWidget

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

_Config = namedtuple("_Config", "variant color")

BUTTON_TYPE_MAP = {
    "default": _Config("outlined", "primary"),
    "primary": _Config("contained", "primary"),
    "success": _Config("contained", "success"),
    "warning": _Config("contained", "warning"),
    "danger": _Config("contained", "error"),
    "light": _Config("text", "primary"),
}

SIZE_MAP = {
    "small": 32,  # MaterialUI is 30.75 but we keep this consistent with Panels default
    "medium": 36,
    "large": 42,
}
SIZES = list(SIZE_MAP.keys())

SELF_UPDATE = "self.updateElement()"


class MaterialButton(MaterialWidget, ButtonBase):  # pylint: disable=too-many-ancestors
    """# MaterialButton

    See https://mui.com/components/buttons/"""

    variant = param.Selector(
        default="outlined", objects=["contained", "outlined", "text", "string"]
    )
    color = param.Selector(
        default="primary",
        objects=[
            "inherit",
            "primary",
            "secondary",
            "success",
            "error",
            "info",
            "warning",
            "string",
        ],
    )
    size = param.Selector(default="small", objects=SIZES)
    disable_elevation = param.Boolean()
    disable_focusRipple = param.Boolean()
    disable_ripple = param.Boolean()

    tooltip = param.String("Click Me!")
    tooltip_placement = param.Selector(default="bottom", objects=TOOLTIP_PLACEMENTS)

    width = param.Integer(default=300, bounds=(0, None))
    full_width = param.Boolean(default=True)

    height = param.Integer(default=36, bounds=(0, None))

    _scripts = MaterialWidget._scripts(
        element="MaterialUI.Button",
        properties={
            # Widget
            "autofocus": "autofocus",
            "className": "_css_names",
            "disabled": "disabled",
            # MaterialButton
            "color": "color",
            "disableElevation": "disable_elevation",
            "disableFocusRipple": "disable_focus_ripple",
            "disableRipple": "disable_ripple",
            "fullWidth": "full_width",
            "size": "size",
            "variant": "variant",
        },
        events={"onClick": "data.clicks += 1"},
        children=["data.name"],
    )

    def __init__(self, **params):
        super().__init__(**params)

        self._handle_size_changed()

    def _handle_button_type_changed(self, event=None):
        if event:
            button_type = event.new
        else:
            button_type = self.button_type
        config = BUTTON_TYPE_MAP[button_type]
        self.variant = config.variant
        self.color = config.color

    @param.depends("size", watch=True)
    def _handle_size_changed(self):
        self.height = SIZE_MAP[self.size]

    @classmethod
    def example(cls):
        return cls(
            name="Run Pipeline",
            tooltip="Trains the model",
            button_type="primary",
            tooltip_placement="right-start",
            tooltip_configuration={"enterDelay": 200},
        )
