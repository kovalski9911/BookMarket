from django.contrib.contenttypes.models import ContentType
from django.views.generic.base import RedirectView

from .models import Comments


class CommentsAdd(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        next = self.request.POST.get('next', '/')
        ct_id = self.request.POST.get('ct_id')
        obj_id = self.request.POST.get('obj_id')
        comments = self.request.POST.get('comments')
        user = self.request.user
        if ct_id and obj_id and comments:
            ct = ContentType.objects.get_for_id(ct_id)
            comments = Comments.objects.create(
                user=user,
                comments=comments,
                content_type=ct,
                object_id=obj_id,
            )
        return next
