#!/usr/bin/env python

import cherrypy
import sys
import os
import configparser
import json
from PIL import Image
import numpy as np
import cv2
import configparser
from cherrypy.lib import auth_digest

USERS = {'vt': 'uservt'}

class WebApp(object):

    def __init__(self, img_path):
        self.img_path = img_path

    @cherrypy.expose
    def index(self):
      raise cherrypy.HTTPRedirect("/static/")


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def get_all_images(self):
        imgs = [i for i in os.listdir(self.img_path) if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png")]
        return json.dumps(
            {
                "images": [{"file_name": os.path.basename(i)} for i in imgs]
            }
        )

    @cherrypy.expose
    def get_image(self, file_name, thumbnail=0, q=0):
        file_name = self.img_path + "/" + file_name
        if not os.path.isfile(file_name):
            file_name = 'static/empty.png'
        cherrypy.response.headers['Content-Type'] = "image/jpeg"
        img = Image.open(file_name)
        cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        if not thumbnail == 0:
            imgScale = 150 / cv_img.shape[1]
            newX, newY = cv_img.shape[1] * imgScale, cv_img.shape[0] * imgScale
            cv_img = cv2.resize(cv_img, (int(newX), int(newY)))
        #cv_img = cv2.polylines(cv_img, [0, 0, 50, 50], True, (0, 255, 0), 4, lineType=cv2.LINE_AA)
        ret, jpeg = cv2.imencode('.jpg', cv_img)
        return jpeg.tobytes()

def main(config_filename="settings.ini"):
    config = configparser.ConfigParser()
    config.read(config_filename)

    cherrypy.quickstart(WebApp(config["Path"]["img_path"]), '/', {'global':
                            {'server.socket_host': config["Server"]["host"],
                            'server.socket_port': int(config["Server"]["port"]),
                            'tools.staticdir.root': config["Path"]["static_dir_root"],
                            'log.error_file': 'site.log'
                            },
                            '/static':{
                                'tools.staticdir.on': True,
                                'tools.staticdir.dir': 'static',
                                'tools.staticdir.index': 'persons.html',
                                'tools.auth_digest.on': True,
                                'tools.auth_digest.realm': config["Server"]["host"],
                                'tools.auth_digest.get_ha1': auth_digest.get_ha1_dict_plain(USERS),
                                'tools.auth_digest.key': 'a565c27146791cfb',
                                'tools.auth_digest.accept_charset': 'UTF-8',
                            }})

	
if __name__ == '__main__':
   main()
