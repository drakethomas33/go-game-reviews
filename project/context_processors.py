from django.conf import settings

def analytics_keys(request):
        return {
            "mixpanel_key": settings.MIXPANEL_KEY,
            #"ga_key": settings.GOOGLE_ANALYTICS_KEY
        }