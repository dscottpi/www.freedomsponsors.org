from exceptions import BaseException
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# This is not used anywhere.
# Im leaving it here just to serve as an example of how to write a decorator
def complete_registration_first(view_func): #pragma: no cover
	def _decorated(request, *args, **kwargs):
		if(request.user.is_authenticated()):
			user = request.user
			if(user.is_registration_complete()):
				return view_func(request, *args, **kwargs)
			else:
				url = reverse('core.views.user_views.editUserForm')
				return redirect('%s?next=%s' % (url, request.get_full_path()))
				#TODO
		else:
			raise BaseException('decorator complete_registration_first invoked on unauthenticated session')
	return _decorated

