def _get_initial_value(self,
    replica_id, device,
    primary_var, **kwargs):
    if replica_id == 0:
        assert device is not None