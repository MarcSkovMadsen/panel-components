from collections import namedtuple

import param

from ...shared.widgets.button import ButtonBase
from .ant_widget import AntWidget, AntWidgetGenerator

TOOLTIP_PLACEMENT_DEFAULT = "top"
TOOLTIP_PLACEMENTS = [
    "top",
    "left",
    "right",
    "bottom",
    "topLeft",
    "topRight",
    "bottomLeft",
    "bottomRight",
    "leftTop",
    "leftBottom",
    "rightTop",
    "rightBottom",
]

_Config = namedtuple("_ButtonTypeConfig", "type danger")

BUTTON_TYPE_MAP = {
    "default": _Config("default", False),
    "primary": _Config("primary", False),
    "ghost": _Config("ghost", False),
    "dashed": _Config("dashed", False),
    "link": _Config("link", False),
    "text": _Config("text", False),
    "success": _Config("dashed", False),
    "warning": _Config("dashed", True),
    "danger": _Config("primary", True),
    "light": _Config("default", False),

}
BUTTON_TYPES_ALL = list(BUTTON_TYPE_MAP.keys())
BUTTON_TYPES_ANT = [
    "default",
    "primary",
    "ghost",
    "dashed",
    "link",
    "text",
]

SIZE_MAP = {
    "small": 24,
    "middle": 32,
    "large": 40,
}
SIZES = list(SIZE_MAP.keys())

SELF_UPDATE = "self.updateElement()"

GENERATOR = AntWidgetGenerator(
    element="antd.Button",
    properties={
        "danger": "danger",
        "ghost": "ghost",
        # "href": "href",
        # "loading": "loading",
        "shape": "shape",
        "size": "size",
        # "target": "target",
        "type": "_button_type",
    },
    events={"click": "data.clicks = data.clicks + 1"},
    children="name",
)
class AntButton(AntWidget, ButtonBase):
    """Ant Design Button

    See https://ant.design/components/button/
    """
    _template = GENERATOR.create_template()

    danger = param.Boolean(False, doc="Set the danger status of button", precedence=0)
    ghost = param.Boolean(False, doc="Make background transparent and invert text and border colors", precedence=0)
    # href = param.String(None, doc="Redirect url of link button", precedence=0)
    # loading = param.Boolean(False, doc="Set the loading status of button", precedence=0)
    shape = param.Selector(default="default", objects=["default", "circle", "round"], precedence=0)
    size = param.Selector(default="middle", objects=["large", "middle", "small"], precedence=0)
    # target = param.Selector(default="_blank", objects=["_blank"])
    button_type = param.Selector(default="default", objects=BUTTON_TYPES_ALL, precedence=0.1)
    _button_type = param.Selector(default="default", objects=BUTTON_TYPES_ANT, precedence=0)
    tooltip_placement = param.Selector(default="bottom", objects=TOOLTIP_PLACEMENTS, precedence=0.2)
    tooltip_configuration = param.Dict({}, precedence=0.2)


    _scripts = GENERATOR.create_scripts()

    def __init__(self, **params):
        super().__init__(**params)
        self._handle_size_changed()


    @param.depends("size", watch=True)
    def _handle_size_changed(self):
        self.height = SIZE_MAP[self.size]

    @param.depends("button_type", watch=True)
    def _handle_button_type_changed(self, event=None):
        if event:
            config = BUTTON_TYPE_MAP[event.new]
        else:
            config = BUTTON_TYPE_MAP[self.button_type]
        self._button_type = config.type
        self.danger = config.danger

    @classmethod
    def example(cls):
        return cls(
            name="Run Pipeline",
            tooltip="Trains the model",
            button_type="primary",
        )
