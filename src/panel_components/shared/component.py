from panel.reactive import ReactiveHTML
from panel import Row, Column, Spacer

class Component(ReactiveHTML):
    @classmethod
    def example(cls):
        raise NotImplementedError()

    def explorer(self, show_name=True):
        controls=self.controls(sizing_mode="fixed", width=300)
        panel = Row(controls, self)
        if show_name:
            title="# " + self.name
            return Column(title, panel)
        else:
            return panel

    _child_config = {'name': 'literal'}