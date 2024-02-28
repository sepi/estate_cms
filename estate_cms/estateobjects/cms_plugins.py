from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from estateobjects.models import EstateObject

@plugin_pool.register_plugin
class EstateobjectListPlugin(CMSPluginBase):
    module = _("Estate Objects")
    mame = _("Estate Object List")
    render_template = "cms_estateobjects_integration/estateobjects_plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['object_list'] = EstateObject.objects.order_by('order')
        return context
