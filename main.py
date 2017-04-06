from google.appengine.ext import ndb

import webapp2

class IP(ndb.Model):
  ip = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')
    self.response.out.write("""
      <form action="/save" method="post">
        <div><input name="content"></div>
        <div><input type="submit" value="Save"></div>
    </form>
  </body>
  </html>""")

class SubmitForm(webapp2.RequestHandler):
  def post(self):
    row = IP(ip=self.request.get('content'))
    row.put()
    self.redirect('/show')


class DisplayIP(webapp2.RequestHandler):
  def get(self):
    q = ndb.gql("SELECT * FROM IP ORDER BY date DESC")
    row = q.get()
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(row.ip)

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/save', SubmitForm),
  ('/show', DisplayIP)
], debug=True)
