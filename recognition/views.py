from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render
# Create your views here.
import cv2
import numpy as np

nm=cv2.imread('F:\python3/test.png',0)
from .forms import FileFieldForm
from .models import Document

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'recognition_form.html'  # Replace with your template.
   # success_url = 'moreorless' # Replace with your URL or reverse().
    files1 = []
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files=request.FILES.getlist('file_field')
        form = FileFieldForm(request.POST, request.FILES)

        if form.is_valid():
            for f in files:
                newpic = Document(file_field=request.FILES['file_field'])
                newpic.save()
                
                x = polygon_test(f.name)


            #return self.form_valid(form)
            return render(request,'final.html',{'word':x,
        })
        else:
            return self.form_invalid(form)

def modelx(request):
    return render(request, "final.html", {})

def polygon_test(name):

    # import and cleaning the image

    str='F:\python3\harry\shapes/media/documents/'+name
    print(type(str))
    imgray = cv2.imread(str,0)

    # Get binary image
    no_use, thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Get image where polygons are filled
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    x, y = thresh.shape
    filledPolygon = np.zeros((x, y, 3), np.uint8)

    color = 0

    # starting from innermost contour loop over all
    for cont in contours:

        if (color >= 255):
            color = 0

        color = color + 1

        # Fill the contour with given color
        cv2.drawContours(filledPolygon, [cont], 0, (int(color), int(color), int(color)), -1)
        # Draw border of contour and this is important if the polygon is open
        # Its previous color used to fill area will be replaced with (0,0,0)
        # as area of contour will be equal to its border
        cv2.drawContours(filledPolygon, [cont], 0, (int(0), int(0), int(0)), 3)

    filled_polygon = filledPolygon
    cv2.imwrite('filledpolygon.png', filled_polygon)

    # For safty remove holes
    kernel = np.ones((5, 5), np.uint8)
    filled_polygon = cv2.erode(filled_polygon, kernel, iterations=3)
    filled_polygon = cv2.cvtColor(filled_polygon, cv2.COLOR_BGR2GRAY)

    # finding contours

    row, column = filled_polygon.shape
    color = []

    # Count number of unique colors
    for rowPixel in range(row):
        for columnPixel in range(column):
            if filled_polygon[rowPixel][columnPixel] not in color:
                color.append(filled_polygon[rowPixel][columnPixel])

    return (len(color) - 1)