#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""

from datetime import datetime
from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['54.172.179.45', '100.26.167.148']


def do_pack():
    """
        Create and return archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_path = "versions/web_static_{}.tgz".format(date)
    gzip_archive = local("tar -cvzf {} web_static".format(archived_path))

    if gzip_archive.succeeded:
        return archived_path
    else:
        return None


def do_deploy(archive_path):
    """
    Deploys a web_static archive to the web servers.
    Returns True if successful, False otherwise.
    """
    if os.path.exists(archive_path):
        archive_file = archive_path[9:]
        new_version = "/data/web_static/releases/" + archive_file[:-4]
        archive_file = "/tmp/" + archive_file

        # Upload archive to the /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("sudo mkdir -p {}".format(new_version))

        # Uncompress the archive to the release directory
        run("sudo tar -xzf {} -C {}/".format(archive_file,
                                             new_version))

        # Delete the uploaded archive from the web server
        run("sudo rm {}".format(archive_file))

        # Move the contents to the appropriate directory
        run("sudo mv {}/web_static/* {}".format(new_version,
                                                new_version))

        # Remove the web_static directory from the release directory
        run("sudo rm -rf {}/web_static".format(new_version))

        # Remove the existing symbolic link if it exists
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(new_version))

        print("New version deployed!")
        return True

    return False
