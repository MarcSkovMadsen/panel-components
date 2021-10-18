from collections import namedtuple

import param
from panel.io.loading import stop_loading_spinner

from ...shared.component import ComponentGenerator
from ...shared.widgets.button import ButtonBase
from .shoelace_widget import ShoelaceWidget

_Config = namedtuple("_ButtonTypeConfig", "type")
BUTTON_TYPE_ALL_MAP = {
    "default": _Config("default"),
    "primary": _Config("primary"),
    "success": _Config("success"),
    "neutral": _Config("neutral"),
    "warning": _Config("warning"),
    "danger": _Config("danger"),
    "light": _Config("default"),
}
BUTTON_TYPES_ALL = list(BUTTON_TYPE_ALL_MAP.keys())
BUTTON_TYPES_SHOELACE = [
    "default",
    "primary",
    "success",
    "neutral",
    "warning",
    "danger",
]

TOOLTIP_PLACEMENTS = [
    "top",
    "top-start",
    "top-end",
    "right",
    "right-start",
    "right-end",
    "bottom",
    "bottom-start",
    "bottom-end",
    "left",
    "left-start",
    "left-end",
]

SIZES_MAP = {
    "small": 30,
    "medium": 40,
    "large": 50,
}
SIZES = list(SIZES_MAP)

GENERATOR = ComponentGenerator(
    element="sl-button",
    properties={
        "type": "_button_type",
        "size": "size",
        "loading": "_loading",
        "outline": "outline",
        "pill": "pill",
        "circle": "circle",
    },
    events={"onclick": "data.clicks += 1"},
    children="name",
    tooltip_element="sl-tooltip",
    tooltip_properties={"content": "tooltip", "placement": "tooltip_placement"},
)


class ShoelaceButton(ShoelaceWidget, ButtonBase):
    button_type = param.Selector(
        default="default", objects=BUTTON_TYPES_ALL, doc="""The button's type.""", precedence=0.1
    )
    size = param.Selector(
        default="medium", objects=SIZES, doc="""The button's size""", precedence=0.1
    )
    outline = param.Boolean(doc="Draws an outlined button")
    pill = param.Boolean(doc="Draws a pill-style button with rounded edges")
    circle = param.Boolean(doc="Draws a circle button")

    tooltip_placement = param.Selector(default="bottom", objects=TOOLTIP_PLACEMENTS, precedence=0.2)

    _button_type = param.Selector(default="default", objects=BUTTON_TYPES_SHOELACE)
    _loading = param.Boolean()

    _template = GENERATOR.create_template()
    _scripts = GENERATOR.create_scripts()

    def __init__(self, **params):
        super().__init__(**params)

        self._handle_size_changed()

    def _handle_button_type_changed(self, event=None):
        if event:
            self._button_type = BUTTON_TYPE_ALL_MAP[event.new].type
        else:
            self._button_type = BUTTON_TYPE_ALL_MAP[self.button_type].type

    @param.depends("size", watch=True)
    def _handle_size_changed(self):
        self.height = SIZES_MAP[self.size]

    def _update_loading(self, *_):
        self._loading = self.loading
        stop_loading_spinner(self)

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="primary")
