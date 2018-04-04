from handlers.base import BaseHandler
from google.appengine.api import users
from models.comment import Comment
from models.topic import Topic
from utils.decorators import validate_csrf


class CommentAdd(BaseHandler):
    @validate_csrf
    def post(self, topic_id):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        text = self.request.get("comment-text")
        topic = Topic.get_by_id(int(topic_id))

        comment = Comment.create(content=text, user=user, topic=topic)

        return self.redirect_to("topic-details", topic_id=topic.key.id())

class CommentListHandler(BaseHandler):

    def get(self):
        user =users.get_current_user()
        commentList=Comment.query(Comment.deleted==False and Comment.author_email==user.email()).fetch()
        params={"commentList":commentList}
        return self.render_template_with_csrf("comment_list.html", params=params)
