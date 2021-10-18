"""# BootstrapButton

See https://react-bootstrap.github.io/components/buttons/
"""
import param

from ...shared.widgets.button import ButtonBase
from .bootstrap_widget import BootstrapWidget, BootstrapWidgetGenerator

BUTTON_TYPES = [
    "default",
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "link",
    "outline-primary",
    "outline-secondary",
    "outline-success",
    "outline-danger",
    "outline-warning",
    "outline-info",
    "outline-light",
    "outline-dark",
]

TOOLTIP_PLACEMENTS = [
    "auto-start",
    "auto",
    "auto-end",
    "top-start",
    "top",
    "top-end",
    "right-start",
    "right",
    "right-end",
    "bottom-end",
    "bottom",
    "bottom-start",
    "left-end",
    "left",
    "left-start",
]

SIZES_MAP = {
    "sm": 31,
    "me": 38,
    "lg": 48,
}
SIZES = list(SIZES_MAP.keys())

GENERATOR = BootstrapWidgetGenerator(
    element="ReactBootstrap.Button",
    properties={"variant": "button_type", "size": "size", "active": "active", "href": "href"},
    events={"click": "data.clicks = data.clicks + 1"},
    children="name",
)


class BootstrapButton(BootstrapWidget, ButtonBase): # pylint: disable=too-many-ancestors
    """# BootstrapButton

See https://react-bootstrap.github.io/components/buttons/"""

    _template = GENERATOR.create_template()

    active = param.Boolean(doc="Manually set the visual state of the button to :active")
    button_type = param.ObjectSelector(
        default="light", objects=BUTTON_TYPES, doc="The button's type"
    )
    size = param.Selector(default="me", objects=SIZES, doc="Specifies a large or small button")
    configuration = param.Dict({})
    href = param.String(doc="Providing a href will render an <a> element, styled as a button")

    tooltip_placement = param.Selector(default="right", objects=TOOLTIP_PLACEMENTS)
    tooltip_configuration = param.Dict({})

    height = param.Integer(default=38, bounds=(0, None))

    _scripts = GENERATOR.create_scripts()

    def __init__(self, **params):
        super().__init__(**params)
        self._handle_size_changed()

    @param.depends("size", watch=True)
    def _handle_size_changed(self):
        self.height = SIZES_MAP[self.size]

    @classmethod
    def example(cls):
        return cls(
            name="Run Pipeline",
            button_type="success",
            tooltip="Trains the model",
            tooltip_configuration={},
        )
