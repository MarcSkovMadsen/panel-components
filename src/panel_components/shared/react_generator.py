"""Utility functionality to generate `ReactiveHTML._scripts` for React Components"""
from typing import Dict

import param


class ReactGenerator(param.Parameterized):
    """Utility Class to generate `ReactiveHTML._scripts` for React Components"""

    template = param.String(
        default="""<div id="component" class="pnc-component"></div>""", constant=True
    )

    element = param.String(doc="The name of the Element")
    properties = param.Dict({}, doc="A dict of properties")
    events = param.Dict({}, doc="A dict of events")
    children = param.List(doc="A list of children")

    # Extra/ default events and properties to add on top of the ones specified
    _events: Dict[str, str] = {}
    _properties: Dict[str, str] = {}

    __javascript__ = [
        "https://unpkg.com/react@17.0.2/umd/react.production.min.js",
        "https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js",
    ]

    @staticmethod
    def _create_element(child):
        if isinstance(child, ReactGenerator):
            return child.create_element
        if isinstance(child, str):
            return child
        raise NotImplementedError()

    @property
    def all_properties(self) -> Dict[str, str]:
        """Returns the combined dict of _properties and properties"""
        return {**self._properties, **self.properties}

    @property
    def all_events(self) -> Dict[str, str]:
        """Returns the combined dict of _events and events"""
        return {**self._events, **self.events}

    @property
    def configuration(self) -> Dict[str, str]:
        """Returns a configuration dict from all properties and events"""
        properties = {k: "data." + v for k, v in self.all_properties.items()}
        events = {k: f"()=>{{{v}}}" for k, v in self.all_events.items()}

        return {**properties, **events}

    @property
    def configuration_str(self) -> str:
        """Returns the configuration as a string. Ready for use"""
        return f"{self.configuration}".replace("'", "")

    @property
    def children_str(self) -> str:
        """Returns the children as a string. Ready for use"""
        children = [self._create_element(child) for child in self.children]
        if len(children) == 1:
            children_str = children[0]
        else:
            children_str = f"{children}".replace("'", "")
        return children_str

    @property
    def create_element(self) -> str:
        """Returns the core React.createElement script"""
        # pylint: disable=line-too-long
        return f"""(props)=>{{return React.createElement({self.element},{self.configuration_str},{self.children_str})}}"""

    @property
    def update_element(self):
        """Returns the "updateElement" script"""
        return (
            f"""element=React.createElement({self.create_element});"""
            """ReactDOM.unmountComponentAtNode(state.component);"""
            """ReactDOM.render(element,state.component)"""
        )

    @property
    def update_scripts(self) -> Dict[str, str]:
        """Returns a Dict with all the "self.updateElement()" script for all parameters"""
        if self.all_properties:
            scripts = {v: "self.updateElement()" for v in self.all_properties.values()}
        else:
            scripts = {}
        for child in self.children:
            if isinstance(child, ReactGenerator):
                scripts.update(child.update_scripts)
        return scripts

    @property
    def render_script(self):
        """Returns the "render" script"""
        return "state.component=component;self.updateElement()"

    @property
    def scripts(self) -> Dict:
        """Returns the `_scripts` of the component"""
        return {
            "render": self.render_script,
            "updateElement": self.update_element,
            **self.update_scripts,
        }
