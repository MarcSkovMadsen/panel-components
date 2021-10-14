from panel.reactive import ReactiveHTML

class Component(ReactiveHTML):
    __javascript_modules__ = [
        "https://unpkg.com/@microsoft/fast-components"
    ]