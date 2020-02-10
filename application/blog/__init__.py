from flask import Blueprint
from ..models import Permission

blog = Blueprint('blog',__name__,template_folder='templates',static_folder='static')

@blog.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

from .views import *

