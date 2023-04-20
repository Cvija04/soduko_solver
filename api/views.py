from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .sudoku import generate_board, solve_board

class GenerateBoardView(APIView):
    def get(self, request):
        try:
            sudoku = generate_board()
            return Response({"board":sudoku}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SolveBoardView(APIView):
    def post(self, request):
        try:
            board = request.data.get("board")
            sudoku = solve_board(board)
            return Response(sudoku, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
