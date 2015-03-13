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
            'name': 'openBis',
            'title': 'openBis',
            'description': 'Harvester for openBis (OAI-PMH) data sources'
        }
