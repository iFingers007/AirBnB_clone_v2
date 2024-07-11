#!/usr/bin/python3
"""Module for Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            os.makedir("versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        arc_name = f"versions/web_static_{now}.tgz"
        local("tar -cvfz {} web_static".format(arc_name))
        return arc_name
    except Exception as e:
        return None
    
