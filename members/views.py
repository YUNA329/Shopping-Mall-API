from rest_framework import viewsets

from members.models import Member
from members.serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    