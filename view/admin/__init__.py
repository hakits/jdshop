#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__)
from view.admin import views