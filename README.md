# Panel Components

A package of components for Panel.

## Installation

```bash
pip install -e .
```

## Known Issues

- `@pn.depends(event=button, watch=True)` does not work

## Open Questions

- Should widgets have their framework size or Panels size?
  - For example the Fast Button height 50px or 32px?
- Should buttons have children instead of value?
- Should all widgets have tooltips?