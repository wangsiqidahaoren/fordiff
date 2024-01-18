def make_buffer_allocation(self, buffer):
    name = buffer.get_name()
    device = buffer.get_device()
    dtype = buffer.get_dtype()
    size = buffer.get_size()
    stride = tuple(buffer.get_stride())