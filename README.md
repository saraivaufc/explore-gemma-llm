# explore-gemma-llm

# Install requirements

```shell 
pip install git+https://github.com/huggingface/transformers -U
pip install accelerate
pip install -i https://pypi.org/simple/ bitsandbytes
pip install -U keras-nlp
pip install -U keras
pip install tensorflow[and-cuda]==2.14.0
```

# Install CUDNN
https://developer.nvidia.com/cudnn-downloads?target_os=Linux
https://toranbillups.com/blog/archive/2023/08/19/install-cuda-12-on-popos/
```shell
sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.4.25_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.4.25/cudnn-local-72322D7F-keyring.gpg /usr/share/keyrings/
sudo apt update
sudo apt list --upgradable
sudo apt install libcudnn8=8.9.4.25-1+cuda12.2
pip3 install nvidia-cudnn-cu11==8.9.5.30
nvcc -V
```

# Download Gemma model (9B)

https://www.kaggle.com/models/google/gemma/frameworks/keras/variations/gemma_instruct_7b_en

# Execute

```
python3 main.py
```
