from django.shortcuts import render
from rest_framework.exceptions import ValidationError
# Create your views here.
from rest_framework import generics, mixins, serializers
from rest_framework.generics import get_object_or_404

from .models import Ebook, Review
from .serilizers import EbookSerializer, ReviewSerializer
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if  review_queryset.exists():
            raise ValidationError("You've reviewed this book already.")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
