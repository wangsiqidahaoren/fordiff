--torch/distributed/fsdp/flat_param.py
...
def _get_shard(
        tensor: Tensor,
        rank: int,
        world_size: int,
    ) -> Tuple[Tensor, int]:

    chunk, num_to_pad = FlatParamHandle._get_chunk(
        tensor, rank, world_size,
    )
    shard = chunk.clone()
    if num_to_pad > 0:
        shard = F.pad(shard, [0, num_to_pad])
    return shard, num_to_pad
...