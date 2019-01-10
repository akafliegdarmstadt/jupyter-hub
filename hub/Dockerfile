FROM jupyterhub/jupyterhub

# Download script to automatically stop idle single-user servers
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py

RUN pip install --upgrade pip

#RUN pip install jupyterhub-ldapauthenticator dockerspawner

RUN pip install oauthenticator dockerspawner

COPY ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

CMD jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
