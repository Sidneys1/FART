from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Mission, TestCase
from .search import get_query
from django.db.models import Q

ITEMS_PER_PAGE = 4

def index(request):
    return render(request, 'core/index.html')

def search(request):
    GET_params_wmp = request.GET.copy()
    GET_params_wtp = request.GET.copy()

    if 'mission_page' in GET_params_wmp:
        del GET_params_wmp['mission_page']
    if 'test_page' in GET_params_wtp:
        del GET_params_wtp['test_page']

    query = request.GET.get('q', '')
    if query:
        mission_entry_query = get_query(query, ['mission_title', 'mission_description'])
        mission_objs = Mission.objects.filter(mission_entry_query).order_by('create_date')
        mission_paginator = Paginator(mission_objs, ITEMS_PER_PAGE)

        test_entry_query = get_query(query, ['test_case_title'])
        test_objs = TestCase.objects.filter(test_entry_query).order_by('-create_date')
        test_paginator = Paginator(test_objs, ITEMS_PER_PAGE)
    else:
        test_objs = []
        mission_objs = []

    test_page = request.GET.get('test_page')
    try:
        test_ret = test_paginator.page(test_page)
    except PageNotAnInteger:
        test_ret = test_paginator.page(1)
    except EmptyPage:
        test_ret = test_paginator.page(test_paginator.num_pages)

    mission_page = request.GET.get('mission_page')
    try:
        missions_ret = mission_paginator.page(mission_page)
    except PageNotAnInteger:
        missions_ret = mission_paginator.page(1)
    except EmptyPage:
        missions_ret = mission_paginator.page(mission_paginator.num_pages)

    context = {
        'missions': missions_ret,
        'tests': test_ret,
        'searchterm': query,
        'GET_params_wmp': GET_params_wmp,
        'GET_params_wtp': GET_params_wtp
    }

    return render(request, 'core/search.html', context)

def missions(request):
    mission_objs = Mission.objects.order_by('create_date').all()
    paginator = Paginator(mission_objs, ITEMS_PER_PAGE)

    page = request.GET.get('page')
    try:
        ret = paginator.page(page)
    except PageNotAnInteger:
        ret = paginator.page(1)
    except EmptyPage:
        ret = paginator.page(paginator.num_pages)

    context = {
        'missions': ret
    }
    return render(request, 'core/missions.html', context)

def mission_edit(request, mission_id):
    mission_obj = get_object_or_404(Mission, pk=mission_id)
    return render(request, 'core/mission_edit.html', {'mission': mission_obj})

def tests(request, mission_id):
    mission_obj = get_object_or_404(Mission, pk=mission_id)
    test_objs = TestCase.objects.filter(Q(**{'mission': mission_id})).order_by('create_date').all()

    paginator = Paginator(test_objs, ITEMS_PER_PAGE)

    page = request.GET.get('page')
    try:
        ret = paginator.page(page)
    except PageNotAnInteger:
        ret = paginator.page(1)
    except EmptyPage:
        ret = paginator.page(paginator.num_pages)

    return render(request, 'core/tests.html', {'mission': mission_obj, 'tests': ret})

def test(request, mission_id, test_id):
    return HttpResponse("You are looking at test %s in mission %s"  % (test_id, mission_id))
