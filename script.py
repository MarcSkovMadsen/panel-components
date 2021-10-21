import panel as pn

pn.config.raw_css = [
    (
        """
.pnc-container, .pnc-component {
   width: 100%;
   height: 100%;
   border-width: 1px;
   border-style: solid;
   border-color: lightgray;
}
"""
    )
]

from panel_components.material.widgets import MaterialFloatSlider, MaterialIntSlider

pn.Column(
    MaterialIntSlider.example().explorer(),
    pn.widgets.IntSlider(name="name", orientation="vertical", show_value=True),
).servable()
