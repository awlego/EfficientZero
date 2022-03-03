import ray

ray.init(num_gpus=1, num_cpus=4,
            object_store_memory=15 * 1024 * 1024 * 1024)
print(ray.available_resources())

# looks like I have 15GB of /dev/shm (shared memory) to use.
# see https://www.cyberciti.biz/tips/what-is-devshm-and-its-practical-usage.html