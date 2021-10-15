import param
import panel as pn
from panel_components.fast import widgets as fast_widgets
# from panel_components.fluent import widgets as fluent_widgets
# from panel_components.html import widgets as html_widgets
# from panel_components.panel import widgets as panel_widgets
# from panel_components.wired import widgets as wired_widgets

pn.config.raw_css.append("""
.pn-component {
   width: 100%;
   height: 100%;
}
"""
)

COMPONENT_TYPES = ["widget"]

WIDGETS = {
    "Fast": [fast_widgets.button.Button.example()],
    # "Fluent": [fluent_widgets.button.Button.example()],
    # "HTML": [html_widgets.button.Button.example()],
    # "Panel": [panel_widgets.button.Button.example()],
    # "Wired": [wired_widgets.button.Button.example()],
}

FRAMEWORKS = list(WIDGETS.keys())
class ComponentExplorer(pn.viewable.Viewer):
    framework = param.Selector(default=FRAMEWORKS[0], objects=FRAMEWORKS)
    component_type = param.Selector(default="widget", objects=COMPONENT_TYPES)
    component = param.Selector(default=WIDGETS[FRAMEWORKS[0]][0], objects=WIDGETS[FRAMEWORKS[0]])

    def __init__(self, **params):
        super().__init__(**params)

        self._settings = pn.Param(
            self,
            parameters=["framework", "component_type", "component"],
            expand_button=False,
            show_name=False,
            default_layout=pn.Row,
            sizing_mode="fixed",
            width=600)
        self._layout = pn.Column(self._settings, sizing_mode="stretch_both")
        self._update_components()
        self._update_layout()

    def __panel__(self):
        return self._layout

    @param.depends("framework", watch=True)
    def _update_components(self):
        widgets=WIDGETS[self.framework]
        self.param.component.objects = widgets
        self.component = self.param.component.default = widgets[0]

    @param.depends("component", watch=True)
    def _update_layout(self):
        try:
            explorer = self.component.explorer(show_name=False)
        except:
            controls=self.component.controls(sizing_mode="fixed", width=300)
            explorer = pn.Row(controls, self)
        self._layout[:] = [
            self._settings,
            explorer,
        ]


if __name__.startswith("bokeh"):
    pn.extension(sizing_mode="stretch_width")

    pn.Column(
        ComponentExplorer(),
        pn.pane.HTML("""
<div>
    <fast-button id="anchor" style="height: 40px; width: 100px; margin: 100px; background: green;">Hover me</fast-button>
    <fast-tooltip anchor="anchor">Tooltip text</fast-tooltip>
</div>
"""),
    ).servable()
