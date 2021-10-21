"""# MaterialButton

See https://mui.com/components/buttons/
"""
from collections import namedtuple

import param

from ...shared.widgets.widget import Widget
from .material_widget import MaterialWidget


class SliderBase(Widget):  # pylint: disable=too-many-ancestors
    """Base class for sliders"""

    bar_color = param.Color(
        default="#e6e6e6",
        doc="""
        Color of the slider bar as a hexidecimal RGB value.""",
    )

    direction = param.ObjectSelector(
        default="ltr",
        objects=["ltr", "rtl"],
        doc="""
        Whether the slider should go from left-to-right ('ltr') or
        right-to-left ('rtl')""",
    )

    orientation = param.ObjectSelector(
        default="horizontal",
        objects=["horizontal", "vertical"],
        doc="""
        Whether the slider should be oriented horizontally or
        vertically.""",
    )

    show_value = param.Boolean(
        default=True,
        doc="""
        Whether to show the widget value.""",
    )

    tooltips = param.Boolean(
        default=True,
        doc="""
        Whether the slider handle should display tooltips.""",
    )

    @classmethod
    def example(cls):
        raise NotImplementedError()


_Config = namedtuple("_Config", "orientation marks show_value")
_Size = namedtuple("_Size", "height width")

COMPONENT_SIZE = {
    _Config("horizontal", True, True): _Size(70, 300),
    _Config("horizontal", True, False): _Size(50, 300),
    _Config("horizontal", False, True): _Size(50, 300),
    _Config("horizontal", False, False): _Size(30, 300),
    _Config("vertical", True, True): _Size(300, 150),
    _Config("vertical", True, False): _Size(300, 150),
    _Config("vertical", False, True): _Size(300, 100),
    _Config("vertical", False, False): _Size(300, 100),
}
class MaterialSliderBase(MaterialWidget):
    """Base class for MaterialUI Sliders"""

    color = param.Selector(
        default="primary",
        objects=["primary", "secondary"],
        doc="""
    The color of the component""",
    )
    marks = param.ClassSelector(
        default=False,
        class_=(bool, list),
        doc="""
    Marks indicate predetermined values to which the user can move the slider.
    If True the marks are spaced according the value of the step parameter.
    If list, it should contain objects with value and an optional label keys.
    For example [{"value": 0.2, "label": 'Optimal',}].
    """,
    )
    size = param.Selector(
        default="medium",
        objects=["small", "medium"],
        doc="""
    The size of the slider.""",
    )
    track = param.Selector(default="normal", objects=["inverted", "normal", False])
    value_label_display = param.Selector(default="off", objects=["auto", "off", "on"])

    height = param.Integer(default=60, bounds=(0, None))
    width = param.Integer(default=300, bounds=(0, None))

    _template = """
    <div id="component" class="pnc-component"></div>"""

    _scripts = {
        # Widget
        "autofocus": "self.rr()",
        "_css_names": "self.rr()",
        "disabled": "self.rr()",
        "tooltip": "self.rr()",
        "tooltip_placement": "self.rr()",
        # SliderBase
        "show_value": """self.rr()""",
        # MaterialSliderBase
        "color": "self.rr()",
        "marks": """console.log("rerender");self.rr()""",
        "orientation": "h=model.height;w=model.width;model.height=w;model.width=h;self.rr()",
        "size": "self.rr()",
        "track": "self.rr()",
        "value_label_display": "self.rr()",
        # FloatSlider
        "start": "self.rr()",
        "end": "self.rr()",
        "value": """if (!state.updating){self.rr()}else{state.updating=false};
state.cc.getElementsByClassName("pnc-label")[0].innerHTML=(data.name ? data.name + ": " : "") + data.value;""",
        "step": "self.rr()",
        "render": "state.cc=component;state.updating=false;self.rr()",
        "rr": """
function PncMaterialTooltip({tooltip, tooltip_placement, children}){
    return React.createElement(
        MaterialUI.Tooltip,
        {title: tooltip, placement: tooltip_placement},
        children
        );
}
slider_el=React.createElement(
    MaterialUI.Slider,
    {
        ariaLabel: data.name,
        getAriaValueText: ()=>{return (data.name ? data.name + ": " : "") + data.value},
        autofocus: data.autofocus,
        className: data._css_names,
        disabled: data.disabled,
        color: data.color,
        defaultValue: data.value,
        isRtl: data.direction==="rtl",
        step: data.step,
        marks: data.marks,
        min: data.start,
        max: data.end,
        size: data.size,
        track: data.track,
        orientation: data.orientation,
        defaultValue: data.value,
        valueLabelDisplay: data.value_label_display,
        onChange: (e, v)=>{state.updating=true;data.value=v},
        onChangeCommitted: (e,v)=>{data.value_throttled=v}
    }
)
if (data.show_value){
    title=(data.name ? data.name + ": " : "") + data.value
    elem = React.createElement(MaterialUI.Typography,{className: "pnc-label"},title)
    slider_el=React.createElement(MaterialUI.Box,{style:{height: (data.orientation==="vertical" && data.show_value) ? "calc(100% - 40px)" : "100%"}},elem,slider_el)
}
element=React.createElement(
    PncMaterialTooltip,
    {
        tooltip: data.tooltip,
        tooltip_placement:
        data.tooltip_placement,

    },
    slider_el
)
ReactDOM.unmountComponentAtNode(state.cc);
ReactDOM.render(element,state.cc)
""",
    }

    def __init__(self, **params):
        super().__init__(**params)

        if "height" not in params and "width" not in params:
            self._update_size()

    @param.depends("direction", "marks", "show_value", watch=True)
    def _update_size(self):
        config = _Config(self.orientation, isinstance(self.marks, list), self.show_value)
        size = COMPONENT_SIZE[config]
        self.height = size.height
        self.width = size.width

class MaterialIntSlider(MaterialSliderBase, SliderBase):
    """A Material Int Slider

    Based on

    - [MaterialUI Slider API](https://mui.com/api/slider/) and
    [MaterialUI Slider Examples](https://mui.com/components/slider/)
    - [Panel IntSlider](https://panel.holoviz.org/reference/widgets/IntSlider.html)

    """
    start = param.Integer(
        default=0,
        doc="""
    The minimum allowed value of the slider. Should not be equal to max.""",
    )

    end = param.Integer(
        default=100,
        doc="""
    The maximum allowed value of the slider. Should not be equal to min.""",
    )

    value = param.Integer(default=0)

    value_throttled = param.Integer(default=None, constant=True)

    step = param.Integer(
        default=1,
        doc="""
    The granularity with which the slider can step through values. (A "discrete" slider.) The min prop serves as the origin for the valid values. We recommend (max - min) to be evenly divisible by the step.
When step is null, the thumb can only be slid onto marks provided with the marks prop""",
    )

    @classmethod
    def example(cls):
        return cls(
            name="Temperature",
            tooltip="The temperature in °C",
            start=0,
            end=100,
            value=37,
            step=1,
            marks=[
                {
                    "value": 0,
                    "label": '0°C',
                },
                {
                    "value": 20,
                    "label": '20°C',
                },
                {
                    "value": 37,
                    "label": '37°C',
                },
                {
                    "value": 100,
                    "label": '100°C',
                },
                ]
        )

class ContinuousSliderBase(SliderBase):  # pylint: disable=too-many-ancestors
    """Base class for continous sliders"""

    format = param.String(
        doc="""
        Allows defining a custom format string."""
    )

    @classmethod
    def example(cls):
        raise NotImplementedError()
class MaterialFloatSlider(
    MaterialSliderBase, ContinuousSliderBase
):  # pylint: disable=too-many-ancestors
    """A Material Float Slider

    Based on

    - [MaterialUI Slider API](https://mui.com/api/slider/) and
    [MaterialUI Slider Examples](https://mui.com/components/slider/)
    - [Panel FloatSlider](https://panel.holoviz.org/reference/widgets/FloatSlider.html)

    """

    start = param.Number(
        default=0.0,
        doc="""
    The minimum allowed value of the slider. Should not be equal to max.""",
    )

    end = param.Number(
        default=1.0,
        doc="""
    The maximum allowed value of the slider. Should not be equal to min.""",
    )

    value = param.Number(default=0.0)

    value_throttled = param.Number(default=None, constant=True)

    step = param.Number(
        default=0.1,
        doc="""
    The granularity with which the slider can step through values. (A "discrete" slider.) The min prop serves as the origin for the valid values. We recommend (max - min) to be evenly divisible by the step.
When step is null, the thumb can only be slid onto marks provided with the marks prop""",
    )

    @classmethod
    def example(cls):
        return cls(
            name="Gamma",
            tooltip="Gamma is the inverse of the standard deviation of the RBF kernel",
            start=0.0,
            end=1.0,
            value=0.2,
            step=0.1,
            marks=[
                {
                    "value": 0.2,
                    "label": "Best",
                },
                {
                    "value": 0.8,
                    "label": "Worst",
                },
            ],
        )

