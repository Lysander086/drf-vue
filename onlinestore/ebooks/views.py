from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, serializers
from rest_framework.generics import get_object_or_404

from .models import Ebook, Review
from .serilizers import EbookSerializer, ReviewSerializer


# class EbookListCreateAPIView(generics.CreateAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer


class EbookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)



class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsReviewAuthorOrReadOnly]

