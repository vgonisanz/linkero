# -*- coding: utf-8 -*-

import core.linkero as linkero
#import submodules.pythonScripts.alert_viewer as alerts
import submodules.pythonScripts.modules.alert_viewer as alerts


class alert(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        alerts.alertViewer()
        return "hi!"

##
## Actually setup the Api resource routing here
##
def loadPythonScriptsAPI():
    linkero.api.add_resource(alert, '/alert')