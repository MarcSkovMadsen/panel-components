from panel_components.shared.component import ComponentGenerator


def test_create_template():
    assert (
        ComponentGenerator().create_template()
        == """<div class="pnc-container"><div id="component"></div></div>"""
    )
    assert (
        ComponentGenerator(children="name").create_template()
        == """<div class="pnc-container"><div id="component">${name}</div></div>"""
    )
    assert (
        ComponentGenerator(element="fast-button").create_template()
        == """<div class="pnc-container"><fast-button id="component"></fast-button></div>"""
    )
    assert (
        ComponentGenerator(class_name="test-class").create_template()
        == """<div class="pnc-container"><div id="component" class="test-class"></div></div>"""
    )
    assert (
        ComponentGenerator(tooltip_element="sl-tooltip").create_template()
        == """<div class="pnc-container"><sl-tooltip id="tooltip"><div id="component"></div></sl-tooltip></div>"""
    )


def test_create_scripts():
    # When
    scripts = ComponentGenerator().create_scripts()
    # Then
    assert isinstance(scripts, dict)


def test_create_scripts_with_property():
    # Given
    properties = {"buttonType": "_button_type"}
    # When
    scripts = ComponentGenerator(properties=properties).create_scripts()
    # Then
    assert "component.buttonType=data._button_type" in scripts["render"]
    assert scripts["_button_type"] == "component.buttonType=data._button_type"


def test_create_scripts_with_two_properties():
    # Given
    properties = {"a": "b", "c": "d"}
    # When
    scripts = ComponentGenerator(properties=properties).create_scripts()
    # Then
    assert "component.a=data.b;component.c=data.d" in scripts["render"]
    assert scripts["b"] == "component.a=data.b"
    assert scripts["d"] == "component.c=data.d"


def test_create_scripts_with_events():
    # Given
    events = {"onclick": "data.clicks += 1"}
    # When
    scripts = ComponentGenerator(events=events).create_scripts()
    # Then
    assert "component.onclick=()=>{data.clicks += 1}" in scripts["render"]


def test_create_scripts_with_tooltip_properties():
    # When
    scripts = ComponentGenerator(
        tooltip_element="sl-button", tooltip_properties={"content": "tooltip"}
    ).create_scripts()
    # Then
    assert "tooltip.content=data.tooltip" in scripts["render"]
    assert scripts["tooltip"] == "tooltip.content=data.tooltip"
