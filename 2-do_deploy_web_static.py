#!/usr/bin/python3
""" 2-do_deploy_web_static module"""

from fabric.api import env, run, put
import os


env.hosts = ['xx-web-01', 'xx-web-02']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        my_archive = os.path.basename(archive_path)
        put(archive_path, '/tmp/{}'.format(my_archive))

        release_dir = '/data/web_static/releases/{}'.format(
            my_archive.replace('.tgz', '')
        )

        run('mkdir -p {}'.format(release_dir))

        run('tar -xzf /tmp/{} -C {}'.format(my_archive, release_dir))

        run('rm /tmp/{}'.format(my_archive))

        run('mv {}/web_static/* {}'.format(release_dir, release_dir))

        run('rm -rf {}/web_static'.format(release_dir))

        current_link = '/data/web_static/current'
        run('rm -rf {}'.format(current_link))

        run('ln -s {} {}'.format(release_dir, current_link))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", e)
        return False