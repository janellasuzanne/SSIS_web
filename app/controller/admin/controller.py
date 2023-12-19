import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import user

@user.route('/')
def index():
    return render_template("test.html")