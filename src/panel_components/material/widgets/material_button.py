"""# MaterialButton

See https://mui.com/components/buttons/
"""
from collections import namedtuple

import param

from ...shared.widgets.button import ButtonBase
from .material_widget import MaterialWidget

_Config = namedtuple("_Config", "variant color")

BUTTON_TYPE_MAP = {
    "default": _Config("outlined", "primary"),
    "primary": _Config("contained", "primary"),
    "success": _Config("contained", "success"),
    "warning": _Config("contained", "warning"),
    "danger": _Config("contained", "error"),
    "light": _Config("text", "primary"),
}

SIZE_MAP = {
    "small": 32,  # MaterialUI is 30.75 but we keep this consistent with Panels default
    "medium": 36,
    "large": 42,
}
SIZES = list(SIZE_MAP.keys())

SELF_UPDATE = "self.updateElement()"

COLORS = [
    "inherit",
    "primary",
    "secondary",
    "success",
    "error",
    "info",
    "warning",
    "string",
]


class MaterialButton(MaterialWidget, ButtonBase):  # pylint: disable=too-many-ancestors
    """# MaterialButton
    See https://mui.com/components/buttons/"""

    color = param.Selector(
        default="primary",
        objects=COLORS,
        doc="""
        The color of the component""",
    )
    disable_elevation = param.Boolean(
        doc="""
    If True, no elevation is used"""
    )
    disable_focusRipple = param.Boolean(
        doc="""
    If True, the keyboard focus ripple is disabled"""
    )
    disable_ripple = param.Boolean(
        doc="""
    If true, the ripple effect is disabled"""
    )
    full_width = param.Boolean(
        default=True,
        doc="""
    If True, the button will take up the full width of its container""",
    )
    href = param.String(
        doc="""
    The URL to link to when the button is clicked. If defined, an a element will be used as the
    root node"""
    )
    size = param.Selector(
        default="small",
        objects=SIZES,
        doc="""
    The size of the component. small is equivalent to the dense button styling""",
    )
    variant = param.Selector(
        default="outlined",
        objects=["contained", "outlined", "text", "string"],
        doc="""
        The variant to use""",
    )
    start_icon = param.String(doc="""A SVG Icon""")
    end_icon = param.String(doc="""A SVG icon""")

    _child_config = {"start_icon": "literal", "end_icon": "literal"}

    height = param.Integer(default=36, bounds=(0, None))
    width = param.Integer(default=300, bounds=(0, None))

    _scripts = {
        "autofocus": "self.rr()",
        "_css_names": "self.rr()",
        "disabled": "self.rr()",
        "tooltip": "self.rr()",
        "tooltip_placement": "self.rr()",
        "href": "self.rr()",
        "color": "self.rr()",
        "disable_elevation": "self.rr()",
        "disable_focus_ripple": "self.rr()",
        "disable_ripple": "self.rr()",
        "full_width": "self.rr()",
        "size": "self.rr()",
        "variant": "self.rr()",
        "start_icon": "self.rr()",
        "end_icon": "self.rr()",
        "render": "state.cc=component;self.rr()",
        "rr": """
function PncMaterialTooltip({tooltip, tooltip_placement, children}){
    return React.createElement(
        MaterialUI.Tooltip,
        {title: tooltip, placement: tooltip_placement},
        children,
        );
}
function PncMaterialIcon({icon}){
    if (icon){
        if (icon.includes("<svg")){
            icon=`data:image/svg+xml;utf8,${icon}`;
        };
        icon=React.createElement("img", {style: { height: "100%", width: "100%"}, src: icon} );
        return React.createElement(MaterialUI.Icon, null, icon);
    } else {return null}
};
start_icon=React.createElement(PncMaterialIcon, {icon: data.start_icon});
end_icon=React.createElement(PncMaterialIcon, {icon: data.end_icon});
button=React.createElement(
    MaterialUI.Button,
    {
        autofocus: data.autofocus,
        className: data._css_names,
        disabled: data.disabled,
        href: data.href,
        color: data.color,
        disableElevation: data.disable_elevation,
        disableFocusRipple: data.disable_focus_ripple,
        disableRipple: data.disable_ripple,
        fullWidth: data.full_width,
        size: data.size,
        variant: data.variant,
        onClick: ()=>{data.clicks += 1},
        startIcon: start_icon,
        endIcon: end_icon
    },
    [data.name]
)
element=React.createElement(
    PncMaterialTooltip,
    {
        tooltip: data.tooltip,
        tooltip_placement: data.tooltip_placement,

    },
    button
)
ReactDOM.unmountComponentAtNode(state.cc);
ReactDOM.render(element,state.cc)
""",
    }

    def __init__(self, **params):
        super().__init__(**params)

        self._handle_size_changed()

    def _handle_button_type_changed(self, event=None):
        if event:
            button_type = event.new
        else:
            button_type = self.button_type
        config = BUTTON_TYPE_MAP[button_type]
        self.variant = config.variant
        self.color = config.color

    @param.depends("size", watch=True)
    def _handle_size_changed(self):
        self.height = SIZE_MAP[self.size]

    @classmethod
    def example(cls):
        return cls(
            name="Run Pipeline",
            tooltip="Trains the model",
            button_type="primary",
            tooltip_placement="right-start",
            # pylint: disable=line-too-long
            start_icon=r"""<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-play-fill" viewBox="0 0 16 16">   <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"></path></svg>""",
        )
