FROM jupyterhub/jupyterhub

RUN pip install --upgrade pip
RUN pip install jupyterhub-ldapauthenticator
