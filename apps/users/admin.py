from django.contrib import admin
from apps.users.models import User
from apps.articles.models import Article
from apps.comments.models import Comment
from apps.commissions.models import Commission
from apps.commission_user.models import CommissionUser
from apps.followers.models import Follower
from apps.ratings.models import Rating
from apps.notifications.models import Notification

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Commission)
admin.site.register(CommissionUser)
admin.site.register(Follower)
admin.site.register(Rating)
admin.site.register(Notification)
