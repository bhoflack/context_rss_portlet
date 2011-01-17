from zope.interface import implements
from plone.app.portlets.portlets import rss

class IContextRssPortlet(rss.IRSSPortlet):

class Assignment(rss.Assignment):
    implements(rss.IRSSPortlet)

class Renderer(rss.Renderer):

class AddForm(rss.AddForm):

class EditForm(rss.EditForm):

