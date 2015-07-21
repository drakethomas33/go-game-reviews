from django.http import HttpResponseRedirect


class PrependWWW(object):
    """
    This middleware prepends www. to the domain if there is no other subdomain i.e. naked/root domain always redirected to
    www subdomain
    """
    def process_request(self, request):
        if request.META.get('HTTP_HOST') == 'gogamereview.com':
            url = request.build_absolute_uri(request.get_full_path())
            www_url = url.replace("gogamereview.com", "www.gogamereview.com")
            return HttpResponseRedirect(www_url)