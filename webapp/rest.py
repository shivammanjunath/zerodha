import cherrypy
import json
from cherrypy import tools
import redis_wrapper as rw

class BhavcopyReader(object):
    
    
    def format_data(self, value_data):
        value_data = value_data.replace("[", "")
        value_data = value_data.replace("]", "")
        value_data = value_data.replace("'", "")
        value_data = value_data.split(",")
    
        return value_data
    
    
    @cherrypy.expose
    def index(self):
        return open('home.html')
    
    
    @cherrypy.expose
    @tools.json_out()
    def top_ten(self):
        last_date   = rw.get_data('lastdate')
        pattern     = "{}*".format(last_date)
        keys        = rw.search_data(pattern)
        loop_count  = 0
        top_ten     = []
        for key in keys:
            value_data  = rw.get_data(key)
            if value_data != "" and (value_data.find('None') == -1 and value_data.find('NONE') == -1):
                value_data = self.format_data(value_data)
                top_ten.append(value_data)
                loop_count += 1
                if loop_count == 10:
                    break

        return {'top_ten': top_ten}


    @cherrypy.expose
    @tools.json_in()
    @tools.json_out()
    def search(self):
        json_input = cherrypy.request.json
        keyword = json_input['search_text']
        keys        = rw.search_data("*{}*".format(keyword.upper()))
        results     = []
        for key in keys:
            results.append(key)

        return {'search_result': results}


    @cherrypy.expose
    @tools.json_out()
    def info(self, name):
        bse_id = rw.get_data(name)
        last_date = rw.get_data('lastdate')
        value_data = rw.get_data(last_date + ':' + bse_id)
        value_data = self.format_data(value_data)
        return {'info': value_data}

