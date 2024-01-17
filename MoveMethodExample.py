--torch/distributed/fsdp/flat_param.py
...
def _get_shard(
        tensor: Tensor,
        rank: int,
        world_size: int,
    ) -> Tuple[Tensor, int]:
    chunk, numel_to_pad = FlatParamHandle._get_unpadded_shard(tensor, rank, world_size)
    shard = chunk.clone()
    if numel_to_pad > 0:
        shard = F.pad(shard, [0, numel_to_pad])
    return shard, numel_to_pad
...