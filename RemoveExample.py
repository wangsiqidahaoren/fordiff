--torch/_inductor/sizevars.py
...
def guard_static_shapes(self, left: List[Expr]) -> List[int]:
    return [self.guard_static_shape(x) for x in left]

def __getitem__(self, val: int) -> Expr:
    return self.shape_env.duck_int(val)

def size_hint(self, expr: Expr) -> int:
    if not isinstance(expr, Expr):
        assert isinstance(expr, int)