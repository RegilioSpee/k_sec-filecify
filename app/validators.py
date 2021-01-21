from django.core.exceptions import ValidationError

def file_size(value):
   filesize=value.size 
   if filesize>20000000:
    #    Verander het limiet van de grote van het bestand hieronder
       raise ValidationError("maximum size is 20 mb")

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
      
def captcha_form(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, 'template.html', {'form': form})