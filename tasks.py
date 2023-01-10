#import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

from invoke import task, Collection


@task(name="deploy")
def builds(c):
    print("Root is connected to VPS")
    #c.run("git clone https://github.com/Lumina-Institute/Demo.git")
    c.run("cd /var/www/Demo")
    c.run("git pull origin main")
    c.run("python3 -m venv .env")
    c.run("source .env/bin/activate")
    c.run("pip install --upgrade pip")
    c.run("pip install -r requierement.txt")
    c.run("gunicorn main:app --bind 0.0.0.0:5001 --reload")
    print("is working right")
