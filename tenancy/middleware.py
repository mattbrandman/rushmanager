try:
    from threading import local
except ImportError:
    # Python 2.3 compatibility
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class ThreadLocals(object):
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)
    def process_response(self, request, response):
    	_thread_locals.user = None
    	return response
