def __getitem__(self, val: int) -> Expr:
    return self.shape_env.duck_int(val)
def size_hint(self, expr: Expr) -> int:
    if not isinstance(expr, Expr):
        assert isinstance(expr, int)