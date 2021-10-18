import param

from ...shared.widgets.button import ButtonBase
from .wired_widget import WiredWidget


class WiredButton(WiredWidget, ButtonBase):
    elevation = param.Integer(default=1, bounds=(1, 5))

    _template = """
<wired-button id="component" onclick="${script('click')}">${name}</wired-button>
"""
    __javascript_modules__ = [
        "https://unpkg.com/wired-elements@3.0.0-rc.6/lib/wired-button.js?module"
    ]
    _scripts = {
        **ButtonBase._scripts,
        "render": ButtonBase._scripts["render"]
        + "\n"
        + """
component.elevation=data.elevation
""",
        "elevation": "component.elevation=data.elevation",
    }

    @classmethod
    def example(cls):
        return cls(name="Run Pipeline", tooltip="Trains the model", button_type="primary")


if __name__.startswith("bokeh"):
    WiredButton().explorer().servable()
