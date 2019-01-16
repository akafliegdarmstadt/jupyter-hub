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
c.LDAPAuthenticator.bind_dn_template = ['CN={username},CN=Users,DC=akaflieg,DC=tu-darmstadt,DC=de']
c.LDAPAuthenticator.user_attribute = 'name'
c.LDAPAuthenticator.allowed_groups = []
c.LDAPAuthenticator.lookup_dn = False
c.LDAPAuthenticator.use_ssl = True

#Admins
c.Authenticator.admin_users = {'sebastian_clermont', 'jannik_birk'}

# User Data Persistence with Docker Volumes
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.environment = {
    'JUPYTER_ENABLE_LAB': '1',
}
