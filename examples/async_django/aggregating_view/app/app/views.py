import asyncio

import httpx
from django.http.response import JsonResponse
from django.urls import reverse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer


class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("hotel",)


class HotelRooms(View):
    async def get(self, request, pk):
        hotel_url = request.build_absolute_uri(
            reverse("hotel-detail", kwargs={"pk": pk})
        )
        room_url = request.build_absolute_uri(reverse("room-list")) + f"?hotel={pk}"

        async with httpx.AsyncClient() as client:
            hotel_response, room_response = await asyncio.gather(
                client.get(hotel_url), client.get(room_url)
            )

        data = {
            "hotel": hotel_response.json(),
            "rooms": room_response.json()["results"],
        }

        return JsonResponse(data, json_dumps_params={"indent": 2})
