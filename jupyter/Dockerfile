FROM jupyter/scipy-notebook:latest

# Install ipympl in lab
## If using JupyterLab
## Install nodejs: https://nodejs.org/en/download/
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
jupyter labextension install jupyter-matplotlib && \
jupyter nbextension enable --py widgetsnbextension

RUN pip install https://github.com/helo9/wingstructure/archive/master.zip

RUN pip install ipympl nodejs ipywidgets



