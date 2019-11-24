# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/11/24
# @time : 18:46
import tornado.web
from ..models.user_model import UserModel
from tornado.escape import json_encode


class UserListHandler(tornado.web.RequestHandler):

    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        UserModel.create(name, age)
        resp = {'success': True}
        self.write(json_encode(resp))


class UserHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)
        self.write(json_encode(user_id))

    def put(self, user_id):
        age = self.get_argument('age')
        UserModel.update(int(user_id), age)
        resp = {'success': True}
        self.write(json_encode(resp))

    def delete(self, user_id):
        UserModel.delete(int(user_id))
        resp = {'success': True}
        self.write(json_encode(resp))
