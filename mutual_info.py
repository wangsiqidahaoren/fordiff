def _iterate_columns(X, columns=None):
    ...
    for i in columns:
        yield _get_column(X, i)
    ...
def _get_column(X, i):
    if issparse(X):
        x = np.zeros(X.shape[0])
        s_p, e_p = X.indptr[i], X.indptr[i + 1]
        x[X.indices[s_p:e_p]] = X.data[s_p:e_p]
    else:
        x = X[:, i]
    return x