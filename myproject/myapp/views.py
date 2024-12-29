from django.shortcuts import render
from .models import Novel,NovelChapter,Bookmark,ReadHistory  # Import the Novel model
from rest_framework import viewsets
from .serializers import NovelSerializer, NovelChaptersSerializer,NovelInfoSerializer,UserSerializer,BookMarkSerializer,Read_HistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from django.db.models import F
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        user_id = request.query_params.get('id', None)
        if user_id is None:
            return Response({"error": "user_id is required"}, status=500)
        user = User.objects.filter(id=user_id)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

def novel_list(request):
    # Get all the novels from the database
    novels = Novel.objects.all()
    return render(request, 'novel_list.html', {'novels': novels})


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    permission_classes = [AllowAny]
    @action(detail=False, methods=['get'])
    def novel(self, request):
        novel_id=request.query_params.get('novel_id', None)
        if novel_id  is None :
            return Response({"error": "One of the both is missing"}, status=500)
        novel=Novel.objects.filter(novel_id=novel_id)
        serializer = NovelSerializer(novel, many=True)
        return Response(serializer.data)

    
    @action(detail=False, methods=['get'])
    def search(self, request):
        novel_name=request.query_params.get('novel_name', None)
        if novel_name is None:
            return Response({"error": "Novel name is missing"}, status=400)
        novel=Novel.objects.filter(novel_name__icontains=novel_name)
        novels = Novel.objects.filter(novel_name__icontains=novel_name)
        if not novels.exists():
            return Response({}, status=404)
        serializer = NovelSerializer(novel, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top(self, request):
    # Get the top 5 novels ordered by read_count (descending)
        top_novels = Novel.objects.all().order_by('-read_count')[:5]
        serializer = NovelSerializer(top_novels, many=True)
        return Response(serializer.data)
    
    
    
    @action(detail=False, methods=['get'])
    def novel_fantasy(self, request):
        fantasy_novels=Novel.objects.filter(fantasy=1)
        serializer=NovelSerializer(fantasy_novels,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def novel_isekai(self, request):
        isekai_novels=Novel.objects.filter(isekai=1)
        serializer=NovelSerializer(isekai_novels,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def novel_adventure(self, request):
        adventure_novels=Novel.objects.filter(adventure=1)
        serializer=NovelSerializer(adventure_novels,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def novel_action(self, request):
        action_novels=Novel.objects.filter(action=1)
        serializer=NovelSerializer(action_novels,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def novel_slice_of_life(self, request):
        slice_of_life_novels=Novel.objects.filter(slice_of_life=1)
        serializer=NovelSerializer(slice_of_life_novels,many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def novel_genre(self, request):
        genre=request.query_params.get('genre', None)
        if genre is None:
            return Response({"error": "Genre parameter needed"},status=400)
        
        genre_mapping={
            'fantasy': 'fantasy',
            'isekai': 'isekai',
            'adventure': 'adventure',
            'action': 'action',
            'slice_of_life': 'slice_of_life'
        }

        if genre not in genre_mapping:
            return Response({"error": "Genre is not present"},status=400)
        
        genre_field=genre_mapping[genre]

        genre_novels=Novel.objects.filter(**{genre_field: 1})
        serializer=NovelSerializer(genre_novels,many=True)
        return Response(serializer.data)
    


#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    

class NovelChapterViewSet(viewsets.ModelViewSet):
    queryset = NovelChapter.objects.all()
    serializer_class=NovelChaptersSerializer
    permission_classes = [AllowAny]
    @action(detail=False, methods=['get'])
    def chapters(self, request):
        novel_id=request.query_params.get('novel_id', None)
        if novel_id is None:
            return Response({"error": "novel_id is required"}, status=500)

        chapters=NovelChapter.objects.filter(novel_id=novel_id)
        serializer=NovelChaptersSerializer(chapters, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def contents(self, request):
        novel_id=request.query_params.get('novel_id', None)
        cpt_no=request.query_params.get('cpt_no', None)
        if novel_id  is None or cpt_no is None:
            return Response({"error": "One of the both is missing"}, status=500)
        contents=NovelChapter.objects.filter(novel_id=novel_id, cpt_no=cpt_no)
        serializer=NovelChaptersSerializer(contents, many=True)
        return Response(serializer.data)
    
class NovelInfoSet(viewsets.ModelViewSet):
    #queryset = NovelChapter.objects.all()
    #serializer_class = NovelInfoSerializer
    permission_classes = [AllowAny]
    @action(detail=False, methods=['get'])
    def chapters(self, request):
        novel_id=request.query_params.get('novel_id', None)
        if novel_id is None:
            return Response({"error": "novel_id is required"}, status=500)

        chapters=NovelChapter.objects.filter(novel_id=novel_id)
        serializer=NovelInfoSerializer(chapters, many=True)
        return Response(serializer.data)

class NovelUpdateViewSet(viewsets.ModelViewSet):
    #queryset = Novel.objects.all()
    #serializer_class = NovelSerializer
    permission_classes = [AllowAny]
    @action(detail=False, methods=['get'])
    def read_count_update(self, request):
        novel_id = request.query_params.get('novel_id', None)
        if novel_id is None:
            return Response({"error": "novel_id is required"}, status=500)
    
        try:
            novel_id = int(novel_id)  # Ensure novel_id is numeric
        except ValueError:
            return Response({"error": "novel_id must be numeric"}, status=400)

    # Increment read_count for the novel with the given novel_id
        Novel.objects.filter(novel_id=novel_id).update(read_count=models.F('read_count') + 1)

    # Fetch the updated novel to serialize
        chapters = Novel.objects.filter(novel_id=novel_id)
        serializer = NovelSerializer(chapters, many=True)
        return Response(serializer.data)

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
