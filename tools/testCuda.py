import torch

# Check if CUDA is available
cuda_available = torch.cuda.is_available()

if cuda_available:
    print("CUDA is available. You can use GPU for acceleration.")
    print(f"Number of GPUs available: {torch.cuda.device_count()}")
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Please check your GPU drivers and CUDA installation.")
    print("Find your cuda version uing command `nvcc --version`")
    print("Then follow https://pytorch.org/get-started/locally/")