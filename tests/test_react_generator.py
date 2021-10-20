# """Tests of the `ReactGenerator`"""
# # pylint: disable=redefined-outer-name
# import pytest

# from panel_components.shared.react_generator import ReactGenerator


# @pytest.fixture()
# def button():
#     """A Button ReactGenerator"""
#     return ReactGenerator(
#         element="M.B",
#         properties={"t": "b"},
#         events={},
#         children=["data.n"],
#     )


# @pytest.fixture()
# def tooltip(button):
#     """A Tooltip ReactGenerator"""
#     return ReactGenerator(element="M.T", properties={"tool": "tool"}, children=[button])


# def test_button(button: ReactGenerator):
#     """Test the properties of the button"""
#     assert button.template == """<div id="component" class="pnc-component"></div>"""
#     assert button.render_script == "state.component=component;self.updateElement()"
#     assert button.create_element == """React.createElement(M.B,{t: data.b},data.n)"""
#     assert button.update_element == (
#         (
#             f"""element={button.create_element};"""
#             """ReactDOM.unmountComponentAtNode(state.component);"""
#             """ReactDOM.render(element,state.component)"""
#         )
#     )
#     assert button.update_scripts == {"b": "self.updateElement()"}
#     assert button.scripts == {
#         "render": button.render_script,
#         "updateElement": button.update_element,
#         **button.update_scripts,
#     }


# def test_tooltip(button: ReactGenerator, tooltip: ReactGenerator):
#     """Test the properties of the nested component"""
#     assert tooltip.template == """<div id="component" class="pnc-component"></div>"""
#     assert tooltip.render_script == "state.component=component;self.updateElement()"
#     assert (
#         tooltip.create_element
#         == f"""React.createElement(M.T,{{tool: data.tool}},{button.create_element})"""
#     )
#     assert tooltip.update_element == (
#         (
#             f"""element={tooltip.create_element};"""
#             """ReactDOM.unmountComponentAtNode(state.component);"""
#             """ReactDOM.render(element,state.component)"""
#         )
#     )
#     assert tooltip.update_scripts == {"tool": "self.updateElement()", "b": "self.updateElement()"}
#     assert tooltip.scripts == {
#         "render": tooltip.render_script,
#         "updateElement": (
#             f"""element={tooltip.create_element};"""
#             """ReactDOM.unmountComponentAtNode(state.component);"""
#             """ReactDOM.render(element,state.component)"""
#         ),
#         **tooltip.update_scripts,
#     }


# def test_properties_and_events():
#     """Test that properties and events work as expected"""
#     assert ReactGenerator().configuration == {}
#     assert ReactGenerator(properties={"a": "b"}).configuration == {"a": "data.b"}
#     assert ReactGenerator(events={"onClick": "data.clicks+=1"}).configuration == {
#         "onClick": "()=>{data.clicks+=1}"
#     }
#     assert ReactGenerator(
#         properties={"a": "b"}, events={"onClick": "data.clicks+=1"}
#     ).configuration == {"a": "data.b", "onClick": "()=>{data.clicks+=1}"}
#     assert (
#         ReactGenerator(properties={"a": "b"}, events={"onClick": "data.clicks+=1"}).create_element
#         == "React.createElement(,{a: data.b, onClick: ()=>{data.clicks+=1}},[])"
#     )


# def test_elements():
#     """Test the create_element function"""
#     assert ReactGenerator(element="'div'").create_element == "React.createElement('div',{},[])"
#     assert (
#         ReactGenerator(element="MaterialUI.Button").create_element
#         == "React.createElement(MaterialUI.Button,{},[])"
#     )


# def test_children(button):
#     """Test the children argument"""
#     assert (
#         ReactGenerator(children=["'element'"]).create_element
#         == """React.createElement(,{},'element')"""
#     )
#     assert (
#         ReactGenerator(children=["data.name"]).create_element
#         == "React.createElement(,{},data.name)"
#     )
#     assert (
#         ReactGenerator(children=["'element'", button]).create_element
#         == f"""React.createElement(,{{}},["element", {button.create_element}])"""
#     )


# class ChildReactGenerator(ReactGenerator):
#     """Dummy Child ReactGenerator"""

#     _properties = {"x": "y"}
#     _events = {"onClick": "data.z+=1"}


# def test_child_react_generator():
#     """Test that we can create a Child ReactGenerator class"""
#     # When
#     child = ChildReactGenerator(element="M.B")
#     # Then
#     assert child.template == """<div id="component" class="pnc-component"></div>"""
#     assert child.render_script == "state.component=component;self.updateElement()"
#     assert (
#         child.create_element
#         == """React.createElement(M.B,{x: data.y, onClick: ()=>{data.z+=1}},[])"""
#     )
#     assert child.update_element == (
#         (
#             f"""element={child.create_element};"""
#             """ReactDOM.unmountComponentAtNode(state.component);"""
#             """ReactDOM.render(element,state.component)"""
#         )
#     )
#     assert child.update_scripts == {"y": "self.updateElement()"}
#     assert child.scripts == {
#         "render": child.render_script,
#         "updateElement": child.update_element,
#         **child.update_scripts,
#     }
