from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/GriffithLin/my_bbs"

env.user = 'linming'
env.password = 'Root1234'

env.hosts = ['demo.lm2zwf.com']

env.port = '22'

def deploy():
    source_folder = '/home/linming/sites/lm2zwf.com/my_bbs'
    
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder)) 
    sudo('restart gunicorn-demo.lm2zwf.com') 
    sudo('service nginx reload')