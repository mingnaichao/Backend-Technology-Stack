# -*- coding: utf-8 -*-
# @author : MingNC
# @date : 2019/11/24
# @time : 18:40
class UserModel(object):
    users = {
        1: {'name': 'zhang', 'age': 10},
        2: {'name': 'wang', 'age': 11},
        3: {'name': 'li', 'age': 22}
    }

    @classmethod
    def get(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    @classmethod
    def create(cls, name, age):
        user_dict = {
            'name': name,
            'age': age
        }
        max_id = max(cls.users.keys()) + 1
        cls.users[max_id] = user_dict

    @classmethod
    def update(cls, user_id, age):
        cls.users[user_id]['age'] = age

    @classmethod
    def delete(cls, user_id):
        if user_id in cls.users.keys():
            del cls.users[user_id]
