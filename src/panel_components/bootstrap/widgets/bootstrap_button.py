from ...shared.widgets.button import ButtonBase
from .bootstrap_widget import BootstrapWidget
import param

BUTTON_TYPES_MAP = {
    "default": "btn-primary",
    "primary": "btn-primary",
    "secondary": "btn-secondary",
    "success": "btn-success",
    "danger": "btn-danger",
    "warning": "btn-warning",
    "info": "btn-info",
    "light": "btn-light",
    "dark": "btn-dark",
    "link": "btn-link",
    "outline-primary": "btn-outline-primary",
    "outline-secondary": "btn-outline-secondary",
    "outline-success": "btn-outline-success",
    "outline-danger": "btn-outline-danger",
    "outline-warning": "btn-outline-warning",
    "outline-info": "btn-outline-info",
    "outline-light": "btn-outline-light",
    "outline-dark": "btn-outline-dark",
}

BUTTON_TYPES = list(BUTTON_TYPES_MAP.keys())

class BootstrapButton(BootstrapWidget, ButtonBase):
    _template="""<button id="component" type="button" data-bs-toggle="tooltip" onclick="${script('click')}">${name}</button>"""

    height = param.Integer(default=38, bounds=(0, None))
    button_type = param.ObjectSelector(default='default', objects=BUTTON_TYPES)
    tooltip_options = param.Dict({})

    _css_names_component = ButtonBase._css_names_component + ["btn"]

    def _get_css_names(self):
        return  [BUTTON_TYPES_MAP[self.button_type]] + super()._get_css_names()

    @classmethod
    def example(cls):
        return cls(name="HTML Button", tooltip="Click Me!", tooltip_options={"placement": "right"})

    _scripts = {
        **ButtonBase._scripts,
        "render": ButtonBase._scripts["render"] + ";new bootstrap.Tooltip(component, data.tooltip_options)",
        "render": "component.disabled=data.disabled;component.title=data.tooltip;new bootstrap.Tooltip(component, data.tooltip_options);component.autofocus=data.autofocus;component.className=data._css_names",
        "tooltip": "component.title = data.tooltip;new bootstrap.Tooltip(component, data.tooltip_options)",
        "tooltip_options": "component.title = data.tooltip;new bootstrap.Tooltip(component, data.tooltip_options)",
    }