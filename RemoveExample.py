def size_hint(self, expr: Expr) -> int:
    if not isinstance(expr, Expr):
        assert isinstance(expr, int)