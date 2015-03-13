from ckanext.oaipmh.harvester import OaipmhHarvester
import logging

log = logging.getLogger(__name__)


class OpenbisHarvester(OaipmhHarvester):
    '''
    OpenBis Harvester
    '''

    def info(self):
        '''
        Return information about this harvester.
        '''
        return {
            'name': 'OpenBis',
            'title': 'OpenBis',
            'description': 'Harvester for OpenBis (OAI-PMH) data sources'
        }
