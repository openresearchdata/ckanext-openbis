from ckanext.oaipmh.harvester import OaipmhHarvester
import logging

log = logging.getLogger(__name__)


class OpenbisHarvester(OaipmhHarvester):
    '''
    OpenBis Harvester
    '''

    license_map = {
        'CC_BY': 'CC-BY-4.0',
        'CC_BY_SA': 'CC-BY-SA-4.0',
        'CC_BY_ND': 'CC-BY-ND-4.0',
        'CC_BY_NC': 'CC-BY-NC-4.0',
        'CC_BY_NC_SA': 'CC-BY-NC-SA-4.0',
        'CC_BY_NC_ND': 'CC-BY-NC-ND-4.0'
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
        # TODO: this needs a proper license file
        # configured on the CKAN instance
        # if content['rights'][0] in self.license_map:
        #     return self.license_map[content['rights'][0]]
        return content['rights'][0]

    def _get_possible_resource(self, harvest_obj, content):
        url = None
        candidates = content['source']
        for ident in candidates:
            if ident.startswith('http://') or ident.startswith('https://'):
                url = ident
                break
        return url

    def _extract_author(self, content):
        if 'contributors' in content:
            authors = (
                ', '.join(content['creator']) + ', '
                ', '.join(content['contributors'])
            )
            return authors
        return ', '.join(content['creator'])

    def _extract_tags_and_extras(self, content):
        # remove part after semicolon of tags
        content['subject'] = [tag.split(';')[0] for tag in content['subject']]
        return super(OpenbisHarvester, self)._extract_tags_and_extras(content)

    def _extract_additional_fields(self, content, package_dict):
        if len(content['maintainer_email']) > 0:
            package_dict['maintainer_email'] = content['maintainer_email'][0]
        return package_dict
