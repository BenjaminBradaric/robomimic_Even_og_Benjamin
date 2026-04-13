import h5py
import json

with h5py.File("datasets/lift/ph/low_dim_v15.hdf5", "r") as f:
    env_args = json.loads(f["data"].attrs["env_args"])
    print(env_args["env_kwargs"].get("control_freq"))