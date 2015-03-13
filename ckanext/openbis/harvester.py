from ckanext.oaipmh.harvester import OaipmhHarvester
import logging

log = logging.getLogger(__name__)


class OpenbisHarvester(OaipmhHarvester):
    '''
    OpenBis Harvester
    '''

    license_map = {
        'CC BY': 'CC-BY-4.0',
        'CC BY-SA': 'CC-BY-SA-4.0',
        'CC BY-ND': 'CC-BY-ND-4.0',
        'CC BY-NC': 'CC-BY-NC-4.0',
        'CC BY-NC-SA': 'CC-BY-NC-SA-4.0',
        'CC-BY-NC-ND': 'CC-BY-NC-ND-4.0'
    }

    def info(self):
        '''
        Return information about this harvester.
        '''
        return {
            'name': 'openBis',
            'title': 'openBis',
            'description': 'Harvester for openBis (OAI-PMH) data sources'
        }

    def _extract_license_id(self, content):
        if content['rights'] in license_map:
            return license_map[content['rights']]
        return content['rights']

    def _get_possible_resource(self, harvest_obj, content):
        url = None
        candidates = content['source']
        for ident in candidates:
            if ident.startswith('http://') or ident.startswith('https://'):
                url = ident
                break
        return url
