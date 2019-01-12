import os
from oauthenticator.github import GitHubOAuthenticator


c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]

#c.LDAPAuthenticator.server_address = 'ldap.example.com'
#c.LDAPAuthenticator.bind_dn_template = []
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

# GitHub Authentication
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.GitHubOAuthenticator.oauth_callback_url = 'https://jupyter.akaflieg.tu-darmstadt.de/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = '3fb6064ba4797d2b93fa'
c.GitHubOAuthenticator.client_secret = '39e18dec48c28ecbff1994122e80eec7d316a4e8'
c.Authenticator.admin_users = {'nichtmonti'}

# Whitelist
c.Authenticator.whitelist = {'nichtmonti', 'helo9', 'candraw','moni9'}

# User Data Persistence with Docker Volumes
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.environment = {
    'JUPYTER_ENABLE_LAB': '1',
}
