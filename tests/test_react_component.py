"""Test of the ReactComponentGenerator"""
from panel_components.shared.component import ReactComponentGenerator


def test_react_component():
    """Tests that the Basic Functionality of ReactComponentGenerator works"""
    assert (
        ReactComponentGenerator().create_template()
        == """<div id="component" class="pnc-component"></div>"""
    )
    # pylint: disable=protected-access
    assert ReactComponentGenerator._self_rerender == "self.updateElement()"


def test_create_complex_component_script():
    """Tests that a more advanced use of ReactComponentGenerator works"""
    scripts = ReactComponentGenerator(
        element="MaterialUI.Button",
        properties={
            "variant": "variant",
            "disabled": "disabled",
            "className": "_css_names",
            "color": "color",
            "disableElevation": "disable_elevation",
            "disableFocusRipple": "disable_focus_ripple",
            "disableRipple": "disable_ripple",
        },
        events={"click": "data.clicks=data.clicks+1}"},
        children="name",
    ).create_scripts()
    assert scripts["render"] == "state.component=component;self.updateElement()"
    assert scripts["disabled"] == "self.updateElement()"
