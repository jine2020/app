import json
from json import JSONEncoder

import pymysql
from flask import Flask, current_app, g, request, flash, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "seveniruby"
cors = CORS(app)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.75.130/mysql'
db = SQLAlchemy(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


#
class User(db.Model):
    __tablename__ = "seveniruby_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class TestCase(db.Model):
    __tablename__ = "seveniruby_testcase"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=False, nullable=False)
    data = db.Column(db.String(1024), unique=False, nullable=False)

    # 设置外键关联
    uid = db.Column(db.Integer, db.ForeignKey("seveniruby_user.id"),
                    nullable=False)
    # 确定关联关系
    user = db.relationship('User',
                           backref=db.backref("testcases", lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.name


class TestCaseResource(Resource):
    @jwt_required
    def get(self):
        testcases = TestCase.query.all()
        # app.logger.info(testcases)
        res = [{
            'id': t.id,
            'name': t.name,
            'desc': t.desc,
            'data': t.data
        } for t in testcases]
        return {
            'data': res,
            'errcode': 0
        }

    @jwt_required
    def put(self):
        testcase = TestCase.query.filter_by(id=request.json['id']).first()
        testcase.name = request.json['name']
        testcase.desc = request.json['desc']
        testcase.data = request.json['data']
        # 更新操作
        db.session.flush()
        db.session.commit()

        return {
            "errcode": 0,
            "msg": "seccess"
        }

    @jwt_required
    def post(self):
        name = request.json['name']
        desc = request.json['desc']
        data = request.json['data']
        # 新增操作

        testcase = db.session.query(TestCase).filter(TestCase.id==request.json['id']).first()
        if testcase==None:
            case1 = TestCase(name=name, desc=desc, data=data,
                          uid=1)
            db.session.add(case1)
            db.session.commit()

        return {
            "errcode": 0,
            "msg": "seccess"
        }

class LoginResource(Resource):
    @jwt_required
    def get(self):
        # 从token中解密原始内容 username
        username = get_jwt_identity()
        app.logger.info(username)
        user = User.query.filter_by(username=username).first()
        app.logger.info(user)
        if user is None:
            return "not login"
        else:
            return {
                "id": user.id,
                "user": user.username,
            }

    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username, password=password).first()
        # session["user"] = user.username
        if user is None:
            return {
                'data': None,
                'errcode': 1
            }
        else:
            return {
                'data': {
                    "id": user.id,
                    "user": user.username,
                    # 生成token
                    "token": create_access_token(user.username)
                },
                'errcode': 0
            }

    def delete(self):
        # session["user"] = ""
        return "logout"

api.add_resource(LoginResource, '/login')
api.add_resource(TestCaseResource, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
