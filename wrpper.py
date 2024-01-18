def make_buffer_allocation(self, buffer):
    name = buffer.get_name()
    device = self.codegen_device(buffer.get_device())
    dtype = self.codegen_dtype(buffer.get_dtype())
    size = self.codegen_shape_tuple(tuple(buffer.get_size()))
    stride = self.codegen_shape_tuple(tuple(buffer.get_stride()))
    if config.aot_inductor.abi_compatible:
        device_type, device_id = device.split(",")
    ...