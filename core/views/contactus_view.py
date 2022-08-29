from core.models import Contact
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import ContactSerializer


class ContactApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializer

    def post(self, request, format=None):
        print(request.data)
        try:
            Contact.objects.create(
                email=request.data['email'], message=request.data['message'], name=request.data['name'])
            return Response({'success': 'Your message is submitted'})
        except Exception as e:
            Response({'error': 'e'})
