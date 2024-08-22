from web_project.template_helpers.theme import TemplateHelper


class TemplateBootstrapLayoutBlank:
    def init(context):
        context.update(
            {
                "layout": "blank",
                "content_layout": "wide",
                "display_customizer": False,
            }
        )
        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context
