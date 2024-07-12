#!/usr/bin/python3
""" Module for Deployment of archive"""

from fabric.api import put, env, run
import os

env.hosts = ['100.24.244.124', '18.210.33.175']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    Args:
    archive_path: path to the archive to deploy

    Returns:
    False if the file at the path archive_path doesn’t exist,
    otherwise returns True.
    """

    if not os.path.exists(archive_path):
        return False
    try:
        arc_filename = os.path.basename(archive_path)
        arc_name = os.path.splitext(arc_filename)[0]
        release_dir = f"/data/web_static/releases/{arc_name}"

        put(archive_path, f"/tmp/{arc_filename}")

        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{arc_filename} -C {release_dir}")

        run(f"rm /tmp/{arc_filename}")

#        run(f"mv {release_dir}/web_static/ {release_dir}")
#        run(f"rm -rf {release_dir}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s {release_dir} /data/web_static/current")

        return True
    except Exception as e:
        print(f"Deployment Failed: {e}")
        return False
