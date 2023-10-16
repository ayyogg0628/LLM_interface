# LLM_interface
This Python notebook uses llama-2-13b-chat for the model

Running on Metal GPU (macOS):

### 1. Make sure xcode is installed
check the path of your xcode install:
`xcode-select -p`
if xcode is missing then install it:
`xcode-select --install`

### 2. Install the conda version for MacOS that supports Metal GPU
(uninstall anaconda if already exists)
`wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh`
`bash Miniforge3-MacOSX-arm64.sh`

### 3. Create a conda environment
`conda create -n llama python=3.9.16`
`conda activate llama`

### 4. Install the llama-cpp-python version that supports MacOS Metal GPU
`pip uninstall llama-cpp-python -y`
`CMAKE_ARGS="-DLLAMA_METAL=on" pip install -U llama-cpp-python --no-cache-dir`
`pip install 'llama-cpp-python[server]'`

### 6. Run the notebook and pip install all needed packages