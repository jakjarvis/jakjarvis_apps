from django.shortcuts import render
from .models import Advent
import advent.solutions as solutions

def home(request):
    puzzles = Advent.objects.all()
    return render(request, 'advent/home.html', {'puzzles':puzzles})

def solution(request):
    solution_ref = "Day" + request.POST.get('day') + ", " + request.POST.get('year')
    part1_text = request.POST.get('part1_text')
    part1_text = request.POST.get('part2_text')
    if request.POST.get('day') == '12' and request.POST.get('year') == '2015':
        part1_solution, part2_solution = solutions.solution(request.POST.get('year'),
                                                            request.POST.get('day'),
                                                            request.FILES['part1_file'].read(),
                                                            request.POST.get('part2_text'))

    else:
        part1_solution, part2_solution = solutions.solution(request.POST.get('year'),
                                                            request.POST.get('day'),
                                                            request.POST.get('part1_text'),
                                                            request.POST.get('part2_text'))

    solution_git = "https://github.com/jakjarvis/Jupyter-notebooks/blob/main/Advent%20of%20Code%20" + request.POST.get('year') + "/Day%20" + request.POST.get('day') +".ipynb"
    return render(request, 'advent/solution.html', {'solution_ref':solution_ref,
                                                    'part1_text':part1_text,
                                                    'part2_text':part1_text,
                                                    'part1_solution':part1_solution,
                                                    'part2_solution':part2_solution,
                                                    'solution_git':solution_git})