#!/usr/bin/python3
""" Fabric script """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ tgz """
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        name_folder = "web_static_" + date + ".tgz"
        path = "versions/" + name_folder
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
