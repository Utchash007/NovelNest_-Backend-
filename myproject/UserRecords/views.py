from django.shortcuts import render
from rest_framework import viewsets
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q,F,Max, Subquery, OuterRef,Avg
from .models import *
from .serializers import *
# Create your views here.

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset=Bookmark.objects.all()
    serializer_class=BookMarkSerializer
    permission_classes = [AllowAny]

class ReadHostoryViewSet(viewsets.ModelViewSet):
    queryset=ReadHistory.objects.all()  
    serializer_class=  Read_HistorySerializer
    permission_classes = [AllowAny]

class UserBookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def get_bookmark(self, request):
        user_id = request.query_params.get('id', None)
        novel_id=request.query_params.get('novel_id',None)
        if user_id is None or novel_id is None:
            return Response({"error": "user_id is required"}, status=500)
        bookmarks = Bookmark.objects.filter(id=user_id,novel_id=novel_id)
        serializer = BookMarkSerializer(bookmarks, many=True)
        if(serializer.data==[]):
            return Response({"error": "No bookmarks found"}, status=400)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get(self, request):
        user_id = request.query_params.get('id', None)
        if user_id is None:
            return Response({"error": "user_id is required"}, status=500)
        bookmarks = Bookmark.objects.filter(id=user_id)
        serializer = BookMarkSerializer(bookmarks, many=True)
        if(serializer.data==[]):
            return Response({"error": "No bookmarks found"}, status=400)
        return Response(serializer.data) 


class UserHistory(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def get_history(self, request):
        user_id = request.query_params.get('id', None)
        if user_id is None:
         return Response({"error": "user_id is required"}, status=400)

    # Get the latest timeline for each novel_id
        latest_timeline = ReadHistory.objects.filter(id=user_id).values('novel_id').annotate(
            max_timeline=Max('timeline')
            ).values('max_timeline')

    # Filter records with the latest timeline
        read_history = ReadHistory.objects.filter(
         id=user_id, timeline__in=Subquery(latest_timeline)
          ).order_by('-timeline')

        serializer = Read_HistorySerializer(read_history, many=True)
        return Response(serializer.data)
