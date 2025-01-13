from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q,F,Max, Subquery, OuterRef,Avg
# Create your views here.
class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def user_rating(self,request):
        user_id=request.data.get('user_id','None')
        novel_id=request.data.get('novel_id','None')
        user_rating=request.data.get('rating','None')
        parameter=request.data.get('parameter','None')
        if parameter =='1':
            rating=Rating.objects.filter(id_id=user_id,novel_id_id=novel_id)
            serializer=RatingSerializer(rating,many=True)
            return Response(serializer.data)
        elif parameter=='2':
             rating=Rating.objects.filter(id=user_id,novel_id=novel_id).first()
             if rating is None:
                 rating=Rating.objects.create(id_id=user_id, novel_id_id=novel_id,user_rating=user_rating)
                 rating=Rating.objects.filter(id_id=user_id,novel_id_id=novel_id)
                 serializer=RatingSerializer(rating,many=True)
                 return Response(serializer.data)
             else:
                 rating.user_rating=float(user_rating)
                 rating.save()
                 rating=Rating.objects.filter(id_id=user_id,novel_id_id=novel_id)
                 serializer=RatingSerializer(rating,many=True)
                 return Response(serializer.data)
        else :
            if novel_id is None:
                return Response({"error": "novel_id is required"}, status=500)
            avg_rating=Rating.objects.filter(novel_id_id=novel_id).aggregate(Avg('user_rating'))
            avg_value = avg_rating.get('user_rating__avg', 0)
            return Response([{"novel_id": novel_id, "average_rating": avg_value}], status=200)
    
    @action(detail=False, methods=['get'])
    def avgrate(self,request):
        novel_id=request.query_params.get('novel_id',None)
        if novel_id is None:
            return Response({"error": "novel_id is required"}, status=500)
        avg_rating=Rating.objects.filter(novel_id=novel_id).aggregate(Avg('user_rating'))
        avg_value = avg_rating.get('user_rating__avg', 0)
        return Response([{"novel_id": novel_id, "average_rating": avg_value}], status=200)