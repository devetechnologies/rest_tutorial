from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer
# Create your views here.

class SnippetList(APIView):
    #list all snippet or create a snippet

     def get(self,request,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer( snippets, many=True)
        #print(serializer.data)
        return Response(serializer.data)
    

class SnippetDetail(APIView):
    '''
    Retrive, update or delete a code snippet.
    '''

    def get_object(self,pk):
        try:
         return  Snippet.objects.get(pk=pk)
        except:
            Snippet.DoesNotExist
            raise Http404

    def get(self,request,pk,format=None):
        snippet = self.get_object(pk=pk)
        serializer= SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        snippet = self.get_object(pk=pk)
        serializer= SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    