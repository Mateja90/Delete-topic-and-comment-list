#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.comments import CommentAdd, CommentListHandler
from handlers.topics import TopicAdd, TopicDetails, TopicDeleteHandler
from handlers.workers.email_new_comment import EmailNewCommentWorker
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),

    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDeleteHandler, name="topic-delete"),
    webapp2.Route('/comment-list', CommentListHandler, name="comment-list"),

    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="taks-email-new-comment"),

], debug=True)
