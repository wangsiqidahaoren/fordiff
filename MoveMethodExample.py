--torch/distributed/fsdp/fully_sharded_data_parallel.py
...
def _get_shard_functional(
    tensor: torch.Tensor,
    rank: int,
    world_size: int,
) -> Tuple[torch.Tensor, int]:
    chunk, pad_num = FullyShardedDataParallel._get_chunk(
        tensor, rank, world_size,
    )
    shard = chunk.clone()
    if pad_num > 0:
        shard = F.pad(shard, [0, pad_num])
    return shard, pad_num
...