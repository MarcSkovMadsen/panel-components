from typing import Dict, List, Optional
from panel.reactive import ReactiveHTML
from panel import Row, Column
import param


class Component(ReactiveHTML):
    @classmethod
    def example(cls):
        raise NotImplementedError()

    def explorer(self, show_name=True):
        controls = self.controls(sizing_mode="fixed", width=300)
        panel = Row(controls, self)
        if show_name:
            title = "# " + self.name
            return Column(title, panel)
        else:
            return panel

    _child_config = {"name": "literal"}

class WebComponentGenerator(param.Parameterized):
    element = param.String(default="div")
    id = param.String(default="component")
    class_name = param.String(None)
    properties = param.Dict()
    events = param.Dict()
    children = param.String()
    tooltip_element = param.String()
    tooltip_id = param.String("tooltip")
    tooltip_properties = param.Dict()

    def create_template(self) -> str:
        template = f"""<{self.element}"""
        if self.id:
            template += f''' id="{self.id}"'''
        if self.class_name:
            template += f''' class="{self.class_name}"'''
        template += ">"
        if self.children:
            template += f"${{{self.children}}}"
        template += f"""</{self.element}>"""

        if self.tooltip_element:
            template = f"""<{self.tooltip_element} id="{self.tooltip_id}">{template}</{self.tooltip_element}>"""

        template = f"""<div class="pnc-container">{template}</div>"""
        return template

    def create_scripts(self) -> Dict:
        scripts = {}
        render_script=""

        if self.properties:
            properties = {**self.default_properties, **self.properties}
        else:
            properties = self.default_properties

        if properties:
            for property, parameter in properties.items():
                scripts[parameter] = f"{self.id}.{property}=data.{parameter}"
                if render_script:
                    render_script += ";"
                render_script+= scripts[parameter]
        events = self.events
        if self.tooltip_element:
            tooltip_properties = self.tooltip_properties
            for property, parameter in tooltip_properties.items():
                scripts[parameter] = f"{self.tooltip_id}.{property}=data.{parameter}"
                if render_script:
                    render_script += ";"
                render_script+= scripts[parameter]
        if events:
            for event, handler in events.items():
                if render_script:
                    render_script += ";"
                render_script += f"component.{event}=()=>{{{handler}}}"

        if render_script:
            scripts["render"]=render_script
        return scripts

    @property
    def default_properties(self):
        properties = {
            "disabled": "disabled",
            "autofocus": "autofocus",
            "className": "_css_names",
        }
        if not self.tooltip_element:
            properties["title"]="tooltip"
        return properties


class ReactComponentGenerator:
    _self_rerender = """self.updateElement()"""
    _self_render = "state.component=component;self.updateElement()"

    __javascript__ = [
        "https://unpkg.com/react@17.0.2/umd/react.development.js",
        "https://unpkg.com/react-dom@17.0.2/umd/react-dom.development.js",
        "https://unpkg.com/babel-standalone@latest/babel.min.js",
    ]

    @staticmethod
    def _to_string(config: Dict) -> str:
        return f"{config}".replace("'", "").replace(" ", "")

    @classmethod
    def _create_update_element_script(cls, element, config, children, tooltip_element=""):
        config_str = cls._to_string(f"{config}".replace("'", "").replace(" ", ""))
        config_str = config_str[:-1] + ",...data.configuration}"
        tooltip_str = (
            "{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration}"
        )
        return (
            f"""element=React.createElement({element},{config_str},{children});"""
            f"""element=React.createElement({tooltip_element},{tooltip_str},element);"""
            """ReactDOM.unmountComponentAtNode(state.component);"""
            """ReactDOM.render(element,state.component)"""
        )

    @classmethod
    def create_template(
        cls, element="div", id: str = "component", class_name: str = "pnc-container"
    ) -> str:
        return f"""<{element} id="{id}" class="{class_name}"></{element}>"""

    @classmethod
    def create_scripts(
        cls, element: str, properties: Dict, events: Dict, children: str, tooltip_element=""
    ) -> Dict:
        properties = {"className": "_css_names", "disabled": "disabled", **properties}
        updates = {parameter: cls._self_rerender for parameter in properties.values()}
        tooltip_updates = {
            "tooltip": cls._self_rerender,
            "tooltip_placement": cls._self_rerender,
            "tooltip_configuration": cls._self_rerender,
        }
        updates = {**updates, **tooltip_updates}
        properties = {property: f"data.{parameter}" for property, parameter in properties.items()}
        events = {
            f"on{parameter.capitalize()}": f"()=>{{{value}}}" for parameter, value in events.items()
        }
        children = f"data.{children}"
        return {
            "render": cls._self_render,
            **updates,
            "updateElement": cls._create_update_element_script(
                element, {**properties, **events}, children, tooltip_element
            ),
        }
