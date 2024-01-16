def make_buffer_allocation(self, buffer):
    return self.make_allocation(
        buffer.get_name(),
        buffer.get_device(),
        buffer.get_dtype(),
        buffer.get_size(),
        buffer.get_stride(),
        self.can_cache_buffer_in_thread_local(buffer),
    )

def make_allocation(
    self, name, device, dtype, shape, stride, can_cache_buffer_in_thread_local=False
    ):
    device = self.codegen_device(device)
    dtype = self.codegen_dtype(dtype)
    size = self.codegen_shape_tuple(shape)
    stride = self.codegen_shape_tuple(stride)
    if config.aot_inductor.abi_compatible:
        device_type, device_id = device.split(",")
        args = [
            str(len(shape)),
            self.codegen_int_array_var(size, self.wrapper_call),
            self.codegen_int_array_var(stride, self.wrapper_call),
            dtype,
            device_type,
            "this->device_idx_" if V.graph.aot_mode else device_id,
            f"&{name}_handle",
        ]