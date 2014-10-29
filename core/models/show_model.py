""" Represents an entire show
    
"""

from core.models.base_model import BaseModel

class ShowModel(BaseModel):

    FIELDS = {
        0: 'guid', # tvrobot's id for this show
        1: 'tvdb_id', # tvdb's id for this show
        2: 'name', # full show name
        3: 'search_name', # name safe to use for searching TPB
        4: 'runtime', # episode length in mins
        5: 'ended' # boolean if series ended
    }

    TABLE = 'Show'

    API_SEARCH = 'http://api.trakt.tv/search/shows.json/%(api_key)s?query=%(name)s&seasons=true'
