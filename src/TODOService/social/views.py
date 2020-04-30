from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        response = {'message': 'Hello'}
        return Response(response)


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get('token')}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired'}
            return Response(content)

        # Create user if not exists
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            user.email = data['email']
            user.password = User.objects.make_random_password()
            user.save()

        token = RefreshToken.for_user(user)
        response = dict()
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)


class FacebookView(APIView):
    def post(self, request):
        access_token = request.data.get('token')
        payload = {'access_token': access_token, 'fields': 'id, email'}
        r = requests.get('https://graph.facebook.com/me', params=payload)

        data = json.loads(r.text)
        if 'error' in data:
            content = {'message': 'wrong facebook token / this facebook token is already expired'}
            return Response(content)

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            user.email = data['email']
            user.password = User.objects.make_random_password()
            user.save()

        token = RefreshToken.for_user(user)
        response = dict()
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)