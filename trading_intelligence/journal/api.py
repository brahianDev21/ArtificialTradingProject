from rest_framework import viewsets, permissions
from .models import Journal
from .serializers import JournalSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = JournalSerializer
