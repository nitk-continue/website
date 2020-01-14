from typing import Union

from django.db.models.query import QuerySet

from .models import *


def fetch_all_health_pros() -> QuerySet:
    """
    Fetch all health professionals from the DB
    :return: 'QuerySet' of all 'HealthProfessional' saved in DB
    """
    return HealthProfessional.objects.all()


def fetch_health_pros_by_location(location: str) -> QuerySet:
    """
    Fetch health professionals from DB on the basis of location (case-insensitive)
    :param location: location to be searched
    :return: 'QuerySet' of 'HealthProfessional' in 'location' saved in DB
    """
    return HealthProfessional.objects.filter(location__iexact=location)


def fetch_health_pros_by_designation(designation: str) -> QuerySet:
    """
    Fetch health professionals from DB on the basis of location
    :param designation: designation to be searched (case-insensitive)
    :return: 'QuerySet' of 'HealthProfessional' in 'location' saved in DB
    """
    return HealthProfessional.objects.filter(designation__iexact=designation)


def fetch_articles(tag: Union[str, None] = None) -> QuerySet:
    """
    Fetch articles from DB. If tag is None, fetch all articles, else fetch tag-associated articles
    :param tag: Name of tag for which articles must be retrieved (case-insensitive)
    :return: 'QuerySet' of articles stored in DB
    """
    if tag is None:
        return Post.objects.filter(author__exact='')
    else:
        tag = Tag.objects.get(name__iexact=tag)
        return tag.posts.filter(author__exact='')


def fetch_blogs(tag: Union[str, None] = None) -> QuerySet:
    """
    Fetch blogs from DB. If tag is None, fetch all blogs, else fetch tag-associated blogs
    :param tag: Name of tag for which blogs must be retrieved (case-insensitive)
    :return: 'QuerySet' of blogs stored in DB
    """
    if tag is None:
        return Post.objects.exclude(author__exact='')
    else:
        tag = Tag.objects.get(name__iexact=tag)
        return tag.posts.exclude(author__exact='')


def fetch_blogs_by_author(author: str) -> QuerySet:
    """
    Fetch blogs by 'author' from DB
    :param author: Name of author whose blogs must be retrieved (case-insensitive)
    :return: 'QuerySet' of blogs stored in DB by 'author'
    """
    return Post.objects.filter(author__iexact=author)
