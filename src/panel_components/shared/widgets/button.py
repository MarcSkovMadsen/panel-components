import param
from panel.widgets.button import BUTTON_TYPES

from .widget import Widget

if not "light" in BUTTON_TYPES:
    BUTTON_TYPES = BUTTON_TYPES + ["light"]
class Button():
    pass

class ButtonBase(Widget):
    value = param.Event(precedence=-1)
    clicks = param.Integer(default=0)
    button_type = param.ObjectSelector(default='default', objects=BUTTON_TYPES)
    css_names = param.List([])

    height = param.Integer(default=32, bounds=(0, None))
    width = param.Integer(default=300, bounds=(0, None))

    _css_names = param.String("")

    _scripts={
        **Widget._scripts,
        "click": "data.clicks += 1",
    }

    _css_names_component = ["pnc-component"]

    def __init__(self, **params):
        super().__init__(**params)

        self.param.watch(self._handle_button_type_changed, "button_type")
        self.param.watch(self._handle_css_names_changed, "css_names")

        self._handle_button_type_changed()
        self._handle_css_names_changed()

    @param.depends("clicks", watch=True)
    def _trigger_value_event(self):
        self.param.trigger('value')

    def _handle_button_type_changed(self, event=None):
        self._handle_css_names_changed()

    def _handle_css_names_changed(self, event=None):
        css_names = self._get_css_names()
        self._set_css_names(css_names)

    def _get_css_names(self):
        return list(set(self._css_names_component + self.css_names))

    def _set_css_names(self, css_names):
        with param.edit_constant(self):
            self._css_names=" ".join(css_names)