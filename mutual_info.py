def _iterate_columns(X, columns=None):
    ...
    if issparse(X):
        for i in columns:
            x = np.zeros(X.shape[0])
            s_p, e_p = X.indptr[i], X.indptr[i + 1]
            x[X.indices[s_p:e_p]] = X.data[s_p:e_p]
            yield x
    else:
        for i in columns:
            yield X[:, i]
    ...