#!/usr/bin/python3
"""
This Fabric script creates and distributes an archive to web servers.
"""

from datetime import datetime
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.172.179.45', '100.26.167.148']


def do_pack():
    """Creates a compressed archive of web_static contents"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        gzip_archive = local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
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


def deploy():
    """Creates and distributes an archive to web servers."""
    archived_path = do_pack()
    if not archived_path:
        return False

    return do_deploy(archived_path)


if __name__ == "__main__":
    deploy()
