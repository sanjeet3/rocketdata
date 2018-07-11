'''
Created on 11-Jul-2018

@author: Sanjay Saini
'''
from src.api.basehandler import Basehandler

class Home(Basehandler):
  def get(self):
    context = self.get_context
    template = self.get_jinja2_env.get_template('html/base.html')    
    self.response.out.write(template.render(context))      
      