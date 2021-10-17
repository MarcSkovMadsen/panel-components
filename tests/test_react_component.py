from panel_components.shared.component import ReactComponent


def test_react_component():
    assert ReactComponent.create_template() == """<div id="component" class="pn-component-wrapper"></div>"""
    assert ReactComponent._self_rerender == "self.updateElement()"


def test_create_component_scripts():
    # Given
    el = "MaterialUI.Button"
    properties = {}
    events = {}
    children = "name"
    # When
    scripts = ReactComponent.create_scripts(
        element=el,
        properties=properties,
        events=events,
        children=children,
        tooltip_element="MaterialUI.Tooltip",
    )
    # Then
    assert scripts["render"] == "state.component=component;self.updateElement()"
    assert scripts["disabled"] == "self.updateElement()"
    assert (
        scripts["updateElement"]
        == """element=React.createElement(MaterialUI.Button,{className:data._css_names,disabled:data.disabled,...data.configuration},data.name);element=React.createElement(MaterialUI.Tooltip,{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},element);ReactDOM.unmountComponentAtNode(state.component);ReactDOM.render(element,state.component)"""
    )
    assert {"render", "disabled", "updateElement"}.issubset(set(scripts.keys()))

def test_create_complex_component_script():
    scripts=ReactComponent.create_scripts(
            element="MaterialUI.Button",
            properties={"variant": "variant", "disabled": "disabled", "className": "_css_names", "color": "color", "disableElevation": "disable_elevation", "disableFocusRipple": "disable_focus_ripple", "disableRipple": "disable_ripple"},
            events={"click": "data.clicks=data.clicks+1}"},
            children="name",
        )
    assert scripts["render"] == "state.component=component;self.updateElement()"
    assert scripts["disabled"] == "self.updateElement()"

def test_different_prop_param_names():
    # Given
    el = "MaterialUI.Button"
    properties = {"disableElevation": "disable_elevation"}
    events = {}
    children = "name"
    scripts = ReactComponent.create_scripts(element=el, properties=properties, events=events, children=children, tooltip_element="MaterialUI.Tooltip")
    assert scripts["render"] == "state.component=component;self.updateElement()"
    assert scripts["disable_elevation"] == "self.updateElement()"
    assert (
        scripts["updateElement"]
        == """element=React.createElement(MaterialUI.Button,{className:data._css_names,disabled:data.disabled,disableElevation:data.disable_elevation,...data.configuration},data.name);element=React.createElement(MaterialUI.Tooltip,{title:data.tooltip,placement:data.tooltip_placement,...data.tooltip_configuration},element);ReactDOM.unmountComponentAtNode(state.component);ReactDOM.render(element,state.component)"""
    )
    assert {"render", "disable_elevation", "updateElement"}.issubset(set(scripts.keys()))