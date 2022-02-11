#!/usr/bin/python3
""" This module generates a .tgz archive from """
from fabric.api import *
import datetime
import os.path
env.hosts = ['35.185.4.79', '35.196.72.165']


def do_pack():
    """ Create pack of file .pgz """
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name_file = "versions/web_static_" + date_time + ".tgz"
    localpth = "web_static/"
    local("mkdir -p versions")
    result = local("tar -zcvf {} {}".format(name_file, localpth))
    if result is None:
        return None
    else:
        return name_file


def do_deploy(archive_path):
    """ Distribute archive to server """
    file_name = archive_path.split("/")[-1]
    file_wext = file_name.split(".")[0]
    path = "/data/web_static/releases/"
    if os.path.exists(archive_path) is False:
        return False

    put(archive_path, "/tmp/")
    run("mkdir -p {}{}".format(path, file_wext))
    run("tar -xzf /tmp/{} -C {}{}".format(file_name, path, file_wext))
    run("rm /tmp/{}".format(file_name))
    run("mv {}{}/web_static/* {}{}/".format(path, file_wext, path, file_wext))
    cmd = "rm -rf /data/web_static/releases/"
    run("{}{}/web_static".format(cmd, file_wext))
    run("rm -rf /data/web_static/current")
    command = "ln -s /data/web_static/releases/{}".format(file_wext)
    command += " /data/web_static/current"
    run(command)
    return True
