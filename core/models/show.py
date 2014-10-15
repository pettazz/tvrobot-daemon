""" Represents an entire show
    
"""

from core.models.base_model import BaseModel

class ShowModel(BaseModel):

    FIELDS = [
        'guid', # tvrobot's id for this show
        'tvdb_id', # tvdb's id for this show
        'name', # full show name
        'search_name', # name safe to use for searching TPB
        'runtime', # episode length in mins
        'ended' # boolean if series ended
    ]

    API_SEARCH = 'http://api.trakt.tv/search/shows.json/%(api_key)s?query=%(name)s&seasons=true'


