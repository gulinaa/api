# from django.contrib.auth.models import User
# User = get_user_model()
from account.models import MyUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, primary_key=True)

    def __str__(self):
        return self.name

# ROOM_TYPE = (
#     ('STANDARD', 'standard'),
#     ('PREMIUM', 'premium'),
#     ('STUDIO ROOM', 'studio room'),
#     ('EXECUTIVE SUITE', 'executive suite'),
#     ('ROYAL', 'royal'),
#     ('INTERCONNECTING ROOM', 'interconnecting room'),
#     ('PENTHOUSE ROOM', 'penthouse room')
# )
# BED_TYPE = (
#     ('TWIN', 'twin'),
#     ('QUEEN', 'queen'),
#     ('KING', 'king'),
#     ('TRIPLE_BED', 'triple_bed')
# )


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # room_type = models.CharField(choices=ROOM_TYPE, max_length=100)
    # bed_type = models.CharField(choices=BED_TYPE, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='hotels')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class HotelImage(models.Model):
    image = models.ImageField(upload_to='images')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.author}:{self.body}'


class Likes(models.Model):
    likes = models.BooleanField(default=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return str(self.likes)


RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)


class Rating(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rating')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='rating')
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)


class Favorite(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='favourites')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='favourites')
    favorite = models.BooleanField(default=True)


