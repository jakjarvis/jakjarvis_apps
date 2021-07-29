from django.shortcuts import render
from .models import Advent
import advent.solutions as solutions

def home(request):
    puzzles = Advent.objects.all()
    return render(request, 'advent/home.html', {'puzzles':puzzles})

def solution(request):
    solution_ref = "Day" + request.GET.get('day') + ", " + request.GET.get('year')
    part1_input = request.GET.get('part1_input')
    part2_input = request.GET.get('part2_input')
    part1_solution, part2_solution = solutions.solution(request.GET.get('year'),
                                                        request.GET.get('day'),
                                                        request.GET.get('part1_input'),
                                                        request.GET.get('part2_input'))
    solution_git = "https://github.com/jakjarvis/Jupyter-notebooks/blob/main/Advent%20of%20Code%20" + request.GET.get('year') + "/Day%20" + request.GET.get('day') +".ipynb"
    return render(request, 'advent/solution.html', {'solution_ref':solution_ref,
                                                    'part1_input':part1_input,
                                                    'part2_input':part2_input,
                                                    'part1_solution':part1_solution,
                                                    'part2_solution':part2_solution,
                                                    'solution_git':solution_git})