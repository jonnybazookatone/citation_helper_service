import requests
from flask import current_app

requests.packages.urllib3.disable_warnings()

client = lambda: Client(current_app.config).session


class Client:
    """
    The Client class is a thin wrapper around requests; Use it as a centralized
    place to set application specific parameters, such as the oauth2
    authorization header
    """
    def __init__(self, config):
        """
        Constructor
        :param client_config: configuration dictionary of the client
        """

        self.session = requests.Session()
        self.token = config.get('CITATION_HELPER_API_TOKEN')
        if self.token:
            self.session.headers.update(
                {'Authorization': 'Bearer %s' % self.token}
            )
