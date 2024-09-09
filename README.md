# HVAC Benchmarks

### Training modality

3B parameter model trained with FSDP on 64 nodes (512 GPUs). 
The dataset consists in 10 samples * number of nodes * number of gpus per node, so each process passes through 10 samples. 

Experiments are run for 3, 5 and 10 epochs, yielding total training times of around 5 minutes (for 3 epochs) and 25 (for 10 epochs). 
Wallclock time is kept at 30 for all runs. 

Each tensor is a 3D grid 128x128x6, so size is ~ 0.375 MB

### Second Training (for epoch time comparison)

Same model has been trained on 2 nodes (16 GPUs). 
The dataset consists in 100 samples * number of nodes * number of gpus per node, so each process passes through 100 samples.

This modality was used only for checking time separation between first and other epochs, to see HVAC improvement. 

### Logged times

I saved times for: 

- Pytorch `dataset_creation_time`
- `train_step_time`: time for one sample to pass through the model (includes backward step and optimizer, not logging overhead)
- `epoch_time`: time to pass through all data samples (includes logging overhead)
- `training_time`: full training from start to end of epochs loop

### Folder structure

- `data`: contains the logged information
- `scripts`: contains bash scripts for submitting jobs
- `src`: contains the code
- `imgs`: contains output plots
