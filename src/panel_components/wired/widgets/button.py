from ...shared.widgets.button import ButtonBase
from .widget import Widget
import param

class Button(Widget, ButtonBase):
    elevation = param.Integer(default=1, bounds=(1,5))

    _template="""
<wired-button id="component" onclick="${script('click')}">${name}</wired-button>
"""
    __javascript_modules__ = [
        "https://unpkg.com/wired-elements/lib/wired-button.js?module"
    ]
    _scripts = {
        **ButtonBase._scripts,
        "render": ButtonBase._scripts["render"] + "\n" + """
component.elevation=data.elevation
""",
    "elevation": "component.elevation=data.elevation"
    }

    @classmethod
    def example(cls):
        return cls(name="Wired", tooltip="Click Me!", button_type="primary")

if __name__.startswith("bokeh"):
    Button().explorer().servable()