from ...shared.widgets.button import ButtonBase
from .bootstrap_widget import BootstrapWidget, BootstrapWidgetGenerator
import param

BUTTON_TYPES = [
    "default",
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "link",
    "outline-primary",
    "outline-secondary",
    "outline-success",
    "outline-danger",
    "outline-warning",
    "outline-info",
    "outline-light",
    "outline-dark",
]

TOOLTIP_PLACEMENTS = [
    "auto-start",
    "auto",
    "auto-end",
    "top-start",
    "top",
    "top-end",
    "right-start",
    "right",
    "right-end",
    "bottom-end",
    "bottom",
    "bottom-start",
    "left-end",
    "left",
    "left-start",
]


class BootstrapButton(BootstrapWidget, ButtonBase):
    _template = BootstrapWidgetGenerator.create_template()

    height = param.Integer(default=38, bounds=(0, None))
    button_type = param.ObjectSelector(default="default", objects=BUTTON_TYPES)
    configuration = param.Dict({})

    tooltip_placement = param.Selector(default="right", objects=TOOLTIP_PLACEMENTS)
    tooltip_configuration = param.Dict({})

    _scripts = BootstrapWidgetGenerator.create_scripts(
        element="ReactBootstrap.Button",
        properties={
            # "variant": "button_type",
        },
        events={"click": "data.clicks = data.clicks + 1"},
        children="name",
        # tooltip_element="ReactBootstrap.Tooltip",
    )
    print(_scripts["updateElement"])
    # _scripts = {
    #     "render": "state.component=component;self.updateElement()",
    #     "_css_names": "self.updateElement()",
    #     "disabled": "self.updateElement()",
    #     "tooltip": "self.updateElement()",
    #     "tooltip_placement": "self.updateElement()",
    #     "tooltip_configuration": "self.updateElement()",
    #     "updateElement": """
    #     element=React.createElement(ReactBootstrap.Button,{className:data._css_names,disabled:data.disabled,...data.configuration},data.name);
    #     ReactDOM.unmountComponentAtNode(state.component);
    #     ReactDOM.render(element,state.component)""",
    #     # "updateElement": "element=React.createElement(ReactBootstrap.Button,{className:data._css_names,disabled:data.disabled,...data.configuration},data.name);element=React.createElement(,{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},element);ReactDOM.unmountComponentAtNode(state.component);ReactDOM.render(element,state.component)",
    # }
    # print(_scripts)

    @classmethod
    def example(cls):
        return cls(
            name="Bootstrap Button", tooltip="Click Me!", tooltip_configuration={}
        )
