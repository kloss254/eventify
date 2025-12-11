# events/views.py
from django.shortcuts import render
from .models import Event, Testimonial, PricingPlan

def home(request):
    events = Event.objects.all()[:4]        # Latest 4 events
    testimonials = Testimonial.objects.all()[:3]
    pricing_plans = PricingPlan.objects.all()
    return render(request, 'events/home.html', {  # make sure template matches
        'events': events,
        'testimonials': testimonials,
        'pricing_plans': pricing_plans
    })
