"""Shared functionality to create Buttons"""
import param
from panel.widgets.button import BUTTON_TYPES

from .widget import Widget

if "light" not in BUTTON_TYPES:
    BUTTON_TYPES = BUTTON_TYPES + ["light"]


class ButtonBase(Widget):  # pylint: disable=too-many-ancestors
    """The Buttons in `panel_components` should inherit from this"""

    value = param.Event(precedence=-1)
    clicks = param.Integer(default=0)
    button_type = param.ObjectSelector(default="default", objects=BUTTON_TYPES)
    css_names = param.List([])

    height = param.Integer(default=32, bounds=(0, None))
    width = param.Integer(default=300, bounds=(0, None))

    _css_names = param.String("")

    _scripts = {
        **Widget._scripts,
        "click": "data.clicks += 1",
    }
    _properties = {**Widget._properties}
    _events = {
        **Widget._events,
        "onclick": "data.clicks += 1",
    }

    def __init__(self, **params):
        super().__init__(**params)

        self.param.watch(self._handle_button_type_changed, "button_type")

        self._handle_button_type_changed()

    @param.depends("clicks", watch=True)
    def _trigger_value_event(self):
        self.param.trigger("value")

    def _handle_button_type_changed(self, event=None):
        self._handle_css_names_changed(event=event)

    @classmethod
    def example(cls):
        raise NotImplementedError()
