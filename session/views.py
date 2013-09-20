from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class SessionView(APIView):
    """
    View to retrieve the current session if one exists, create a new
    session using a valid username and password, or destroy the session.
    """
    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended"
    }

    def _error_response(self, message_key):
        """
        Return an error message.
        """
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }
        return Response(data)

    def get(self, request, *args, **kwargs):
        """
        Return the user id associated with this session if one exists.
        """
        if request.user.is_authenticated():
            return Response({'user_id': request.user.id})
        return Response({'user_id': None})

    def post(self, request, *args, **kwargs):
        """
        Authenticate a user with a username and password.  Return
        appropriate success flag, error messages, and user id.
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = {'success': True, 'user_id': user.id}
                return Response(data)
            return self._error_response('disabled')
        return self._error_response('invalid')

    def delete(self, request, *args, **kwargs):
        """
        Destroy the active session, effectively logging out the
        current user.
        """
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
