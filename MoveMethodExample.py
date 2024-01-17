--torch/distributed/fsdp/fully_sharded_data_parallel.py
...
def _get_shard_functional(
        tensor: torch.Tensor,
        rank: int,
        world_size: int,
    ) -> Tuple[torch.Tensor, int]:

    chunk, num_to_pad = FullyShardedDataParallel._get_chunk(
        tensor, rank, world_size,
    )
 
    shard = chunk.clone()
    if num_to_pad > 0:
        shard = F.pad(shard, [0, num_to_pad])
    return shard, num_to_pad
...