import os


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


# Authentication
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_address = 'karldergrosse.akaflieg.tu-darmstadt.de'
c.LDAPAuthenticator.bind_dn_template = 'akaflieg.tu-darmstadt.de{username}'
c.LDAPAuthenticator.lookup_dn = True
c.LDAPAuthenticator.user_search_base = 'CN=Users,DC=akaflieg,DC=tu-darmstadt,DC=de'
c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
c.LDAPAuthenticator.allowed_groups = []
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
