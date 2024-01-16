def _iterate_columns(X, columns=None):
    ...
    for i in columns:
        yield _get_column(X, i)
    ...
def _get_column(X, i):
    if issparse(X):
        x = np.zeros(X.shape[0])
        start_ptr, end_ptr = X.indptr[i], X.indptr[i + 1]
        x[X.indices[start_ptr:end_ptr]] = X.data[start_ptr:end_ptr]
    else:
        x = X[:, i]
    return x
