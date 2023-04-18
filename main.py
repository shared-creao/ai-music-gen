#@title Setup 1 (just run this once)
import os
import glob
git clone https://github.com/effusiveperiscope/so-vits-svc -b eff-4.0
os.chdir('so-vits-svc')
# # install requirements one-at-a-time to ignore exceptions
# !cat requirements.txt | xargs -n 1 pip install --extra-index-url https://download.pytorch.org/whl/cu116
# !pip install praat-parselmouth
# !pip install ipywidgets
# !pip install huggingface_hub
# !pip install pip==23.0.1 # fix pip version for fairseq install
# !pip install fairseq==0.12.2
# !jupyter nbextension enable --py widgetsnbextension
# existing_files = glob.glob('/content/**/*.*', recursive=True)
# !pip install numpy==1.21
# !pip install --upgrade protobuf=3.9.2
# !pip uninstall -y tensorflow
# !pip install tensorflow==2.11.0 