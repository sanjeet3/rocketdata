'''
Created on 11-Jul-2018

@author: Sanjay Saini
'''
from src.app_configration import config
from src.endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.api import namespace_manager
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc import messages

class FormLayout(messages.Enum):
  ''' Enum class for formlayout package.'''
  VERTICAL = 1
  GRID = 2

class FormType(messages.Enum):
  ''' Enum class for formlayout package.'''
  ACTIVITY = 1
  GENERAL = 2
  
class FormSlider(messages.Enum):
  ''' Enum class for formlayout package.'''
  OFF = 1
  PRODUCT = 2
  PRODUCTCATEGORY = 3
  PRODUCTBRAND = 4
  CLIENT = 5

class Domain(EndpointsModel):
  ''' Data Store for Organization '''
  domain = ndb.StringProperty()
  company_title = ndb.StringProperty()
  address = ndb.TextProperty()
  country = ndb.StringProperty(default='KE')
  currency = ndb.StringProperty(default='KES')
  admin_email = ndb.StringProperty()
  admin_name = ndb.StringProperty() 
  subscription_date = ndb.DateProperty(auto_now_add=True)
  user_count = ndb.IntegerProperty(default=0)
  created_on = ndb.DateTimeProperty(auto_now_add=True)
  update_on = ndb.DateTimeProperty(auto_now=True) 

  @classmethod
  def verify_organization_account(cls, domain):
    #namespace_manager.set_namespace(config.get('namespace'))
    query_obj = cls.query(cls.domain == domain).get()
    return query_obj

  @classmethod
  def get_organization_list(cls):
    return cls.query().order(cls.domain)

class Role(EndpointsModel):
  ''' Data Store for User Role configration with access right '''
  creator_email = ndb.StringProperty(default='System')
  creator_name = ndb.StringProperty(default='System')  
  role = ndb.StringProperty(required=True)
  description = ndb.TextProperty(default='') 
    
  @classmethod
  def get_role_list(cls):
    return cls.query().order(cls.role)  
  
  @classmethod
  def get_role_by_name(cls, name):
    return cls.query(cls.role == name).get()


class User(EndpointsModel):
  ''' Data Store for User '''
  created_on = ndb.DateTimeProperty(auto_now_add=True)
  update_on = ndb.DateTimeProperty(auto_now=True) 
  system_owner = ndb.BooleanProperty(default=False)
  active_status = ndb.BooleanProperty(default=False)
  creator_email = ndb.StringProperty(default='System')
  creator_name = ndb.StringProperty(default='System')   
  name = ndb.StringProperty()
  email = ndb.StringProperty()
  role = ndb.StringProperty(default='ADMIN')
  country = ndb.StringProperty()
  telephone = ndb.StringProperty()
  image_url = ndb.StringProperty()
  gs_key = ndb.StringProperty()
  
  @classmethod
  def get_all_user_list(cls):
    return cls.query().order(cls.name)
  
  @classmethod
  def get_active_user_by_email(cls, email):
    return cls.query(cls.email == email, cls.active_status == True).get()

  @classmethod
  def get_user_by_email(cls, email):
    return cls.query(cls.email == email).get()

  @classmethod
  def get_active_user_list(cls):
    return cls.query(cls.active_status == True).order(cls.name)

  @classmethod
  def get_suspend_user_list(cls):
    return cls.query(cls.active_status == False).order(cls.name)

  @classmethod
  def get_active_user_by_role(cls, role):
    return cls.query(cls.role == role, cls.active_status == True).get()
  @classmethod
  def get_user_email_dict(cls):
    user_dict={}  
    for u in cls.query():
      user_dict[u.email] = u
          
    return user_dict  
  
class FormGroup(EndpointsModel):
  ''' Data Store for Form Group '''
  name = ndb.StringProperty(default='')  
  
  @classmethod
  def get_all_formgroup(cls):
    return cls.query()

  
class Form(EndpointsModel):
  ''' Data Store for Form '''
  creator_email = ndb.StringProperty(default='System')
  creator_name = ndb.StringProperty(default='System')  
  title = ndb.StringProperty(default='')
  description = ndb.TextProperty(default='')  
  form_xml = ndb.TextProperty(default='')
  active_status = ndb.BooleanProperty(default=True)
  created_on = ndb.DateTimeProperty(auto_now_add=True)
  created_by = ndb.StringProperty()
  updated_on = ndb.DateTimeProperty(auto_now=True)
  updated_by = ndb.StringProperty()  
  role_key = ndb.KeyProperty(Role)
  role_name = ndb.StringProperty(default='')
  form_layout = msgprop.EnumProperty(FormLayout, indexed=True, default=FormLayout.VERTICAL)
  form_type = msgprop.EnumProperty(FormType, indexed=True)
  form_slider = msgprop.EnumProperty(FormSlider, indexed=True, default=FormSlider.OFF)
  
  @classmethod
  def get_active_form(cls):
    return cls.query(cls.active_status == True)    
  
  @classmethod
  def get_all_form(cls):
    return cls.query()

  @classmethod
  def get_all_activity_form(cls):
    return cls.query(cls.form_type == FormType.ACTIVITY)