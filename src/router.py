'''
Created on 11-Jul-2018

@author: Sanjay Saini
'''
from src.action import user


from webapp2_extras.routes import RedirectRoute

__route_list = [
    RedirectRoute(r'/', user.Home, name='Home page', strict_slash=True), 
    ]

def get_routes():
  return __route_list

def add_routes(app):
  if app.debug:
    secure_scheme = 'http'
  for __route in __route_list:
    app.router.add(__route)