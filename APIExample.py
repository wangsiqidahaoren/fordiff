def _get_variable_creator_initial_value(self,
                                          replica_id,
                                          device,
                                          primary_var,
                                          **kwargs):
    if replica_id == 0:  # First replica on each worker.
      assert device is not None
      ...