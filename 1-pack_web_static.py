#!/usr/bin/python3
"""Module for Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    if not os.path.exists("versions"):
        os.makedirs("versions")
    now = datetime.now()
    arc_name = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
    arc_path = f"versions/{arc_name}"
    cmd = f"tar -cvzf {arc_path} web_static"
    result = local(cmd)
    if result.return_code == 0:
        return arc_path
    else:
        return None
