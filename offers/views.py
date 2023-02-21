from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Offer
from rest_framework.response import Response


"""
class OfferAPIview(APIView):
    def get_offer(self, pk):
        try:
            return Offer.objects.get(pk=pk)
        except Offer.DoesNotExist:
            raise Http404

    def get(request,self, pk=None, format=None,):
        if pk:
            data = self.get_offer(pk=pk)
            serializer = OffersSerializer(data)
        else:
            data = Offer.objects.all()
            serializer = OffersSerializer(data, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = OffersSerializer(data=data)

        # check if passed data is valid
        serializer.is_valid(raise_exception=True)

        # add offer to the database
        serializer.save()

        # now return response to user
        response = Response()
        response.data = {
                'message': 'offer created successfully',
                'data': serializer.data
                }
        return response

    def put(self, request, pk=None, format=None):
        # get the offer to update
        offer_to_update = Offer.objects.get(pk=pk)

        # pass instance to update to the serializer , with the request data
        # and the partiatl will allow us to update without passing the entire
        # offer object
        serializer = OffersSerializer(instance=offer_to_update,
                                      data=request.data,
                                      partiatl=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # return response to the user
        response = Response()
        response.data = {
                'message': 'offer updated successfully',
                'data': serializer.data
                }

        return response

    def delete(self, request, pk, format=None):
        offer_to_delete = Offer.objects.get(pk=pk)

        # just do it right ?
        # otherwise this is not supposed to delete , just change working field
        offer_to_delete.delete()

        return Response({
            'message': 'offer deleted successfully'
            })

"""
def index(request):
    return Response("<h1>hello</h1>")


"""
def get_categories_and_subcategories(request):
   categories
"""
