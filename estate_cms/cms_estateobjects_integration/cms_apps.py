from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class EstateobjectsApphook(CMSApp):
    app_name = "estateobjects"
    name = "Estate Objects"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["estateobjects.urls"]
