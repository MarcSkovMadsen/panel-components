import panel as pn
import param
from panel import layout

from panel_components.ant.widgets import AntButton
from panel_components.bootstrap.widgets import BootstrapButton
from panel_components.fast.widgets import FastButton
from panel_components.fluent.widgets import FluentButton
from panel_components.html.widgets import HTMLButton
from panel_components.material.widgets import MaterialButton
from panel_components.panel.widgets import Button
from panel_components.shoelace.widgets import ShoelaceButton
from panel_components.wired.widgets import WiredButton

pn.config.raw_css.append(
    """
.pnc-component, .pnc-container {
   width: 100%;
   height: 100%;
}
"""
)

COMPONENT_TYPES = ["widget"]

WIDGETS = {
    "Bootstrap": [BootstrapButton.example()],
    "Ant": [AntButton.example()],
    "Fast": [FastButton.example()],
    "Fluent": [FluentButton.example()],
    "HTML": [HTMLButton.example()],
    "Material": [MaterialButton.example()],
    "Panel": [Button.example()],
    "Shoelace": [ShoelaceButton.example()],
    "Wired": [WiredButton.example()],
}

FRAMEWORKS = list(WIDGETS.keys())


class ComponentExplorer(pn.viewable.Viewer):
    framework = param.Selector(default=FRAMEWORKS[0], objects=FRAMEWORKS)
    component_type = param.Selector(default="widget", objects=COMPONENT_TYPES)
    component = param.Selector(default=WIDGETS[FRAMEWORKS[0]][0], objects=WIDGETS[FRAMEWORKS[0]])

    def __init__(self, **params):
        super().__init__(**params)

        self._settings = pn.WidgetBox(
            pn.Param(
                self,
                parameters=["framework", "component_type", "component"],
                expand_button=False,
                show_name=False,
                default_layout=pn.Row,
                default_precedence=-1,
                # display_threshold=1e-7,
                sizing_mode="stretch_width",
            )
        )
        self._layout = pn.Column(self._settings, sizing_mode="stretch_both")
        self._update_components()
        self._update_layout()

    def __panel__(self):
        return self._layout

    @param.depends("framework", watch=True)
    def _update_components(self):
        widgets = WIDGETS[self.framework]
        self.param.component.objects = widgets
        self.component = self.param.component.default = widgets[0]

    @property
    def title(self):
        return f"# {type(self.component).name}"

    @param.depends("component", watch=True)
    def _update_layout(self):
        try:
            explorer = self.component.explorer(show_name=False)
        except:
            controls = self.component.controls(sizing_mode="fixed", width=300)
            explorer = pn.Row(controls, self)
        self._layout[:] = [
            self._settings,
            self.title,
            pn.layout.HSpacer(height=10),
            explorer,
        ]


if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    ComponentExplorer().servable()
