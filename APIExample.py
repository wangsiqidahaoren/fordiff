def _get_initial_value(self,
    replica_id=0, device=None,
    primary_var=None, **kwargs):
    if replica_id == 0:
        assert device is not None