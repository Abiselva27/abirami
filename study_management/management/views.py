from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from django.http import HttpResponse
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# View for displaying all studies
def study_list(request):
    try:
        studies = Study.objects.all()
        logger.info("Fetched all studies successfully.")
        return render(request, 'management/study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error fetching studies: {str(e)}")
        return HttpResponse("Error fetching studies", status=500)

# View for adding a new study
def add_study(request):
    if request.method == 'POST':
        try:
            study_name = request.POST['study_name']
            study_description = request.POST['study_description']
            study_phase = request.POST['study_phase']
            sponsor_name = request.POST['sponsor_name']
            Study.objects.create(
                study_name=study_name,
                study_description=study_description,
                study_phase=study_phase,
                sponsor_name=sponsor_name
            )
            logger.info(f"Study '{study_name}' created successfully.")
            return redirect('study_list')
        except Exception as e:
            logger.error(f"Error adding study: {str(e)}")
            return HttpResponse("Error adding study", status=500)
    return render(request, 'management/add_study.html')

# View for updating an existing study
def edit_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == 'POST':
        try:
            study.study_name = request.POST['study_name']
            study.study_description = request.POST['study_description']
            study.study_phase = request.POST['study_phase']
            study.sponsor_name = request.POST['sponsor_name']
            study.save()
            logger.info(f"Study '{study.study_name}' It is updated successfully.")
            return redirect('study_list')
        except Exception as e:
            logger.error(f"Error updating study with ID {study_id}: {str(e)}")
            return HttpResponse("Error updating study", status=500)
    return render(request, 'management/edit_study.html', {'study': study})

# View for deleting a study
def delete_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        study.delete()
        logger.info(f"Study with ID {study_id} deleted successfully.")
        return redirect('study_list')
    except Exception as e:
        logger.error(f"Error deleting study with ID {study_id}: {str(e)}")
        return HttpResponse("Error deleting study", status=500)

# View for displaying a single study
def view_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        logger.info(f"Fetched details for study with ID {study_id}.")
        return render(request, 'management/view_study.html', {'study': study})
    except Exception as e:
        logger.error(f"Error fetching study with ID {study_id}: {str(e)}")
        return HttpResponse("Error fetching study details", status=500)
