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

c.LDAPAuthenticator.server_address = 'ldap.example.com'
c.LDAPAuthenticator.bind_dn_template = []
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'



