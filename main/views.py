from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# tic tac toe play function
from .ttt import main
    
class play(APIView):

    # just to greet
    def get(self, request, format=None):
        return Response("Hii there...", status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            res = main(request.data['no_list'], request.data['res_list'], request.data['user_list'], request.data['com_list'])
            return Response(res, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
