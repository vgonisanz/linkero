# -*- coding: utf-8 -*-

import core.linkero as linkero
import submodules.pythonScripts.modules.alert_viewer as av
import sys

numItems = int(linkero.config['API']['pythonScriptsAPI']['numItems'])

class alerts(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        filters = []
        filters.append("[todo]")
        numItems = av.countLines(av.openLog())
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            if (sys.version_info > (3, 0)):
                alert[0] = str(alert[0]).replace('\n', '')
            else:
                alert[0] = unicode(alert[0]).replace('\n', '')
        return alerts

class alertsByUser(linkero.Resource):
    @linkero.auth.login_required
    def get(self, user):
        filters = []
        filters.append("[info]")
        filters.append(user)
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            if (sys.version_info > (3, 0)):
                alert[0] = str(alert[0]).replace('\n', '')
            else:
                alert[0] = unicode(alert[0]).replace('\n', '')
        return alerts

class alertsByUserAndMonth(linkero.Resource):
    @linkero.auth.login_required
    def get(self, user, month):
        filters = []
        filters.append("[info]")
        filters.append(user)
        filters.append(month)
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            if (sys.version_info > (3, 0)):
                alert[0] = str(alert[0]).replace('\n', '')
            else:
                alert[0] = unicode(alert[0]).replace('\n', '')
        return alerts

##
## Actually setup the Api resource routing here
##
def loadPythonScriptsAPI():
    linkero.api.add_resource(alerts, '/alerts')
    linkero.api.add_resource(alertsByUser, '/alerts/<user>')
    linkero.api.add_resource(alertsByUserAndMonth, '/alerts/<user>&<month>')
    linkero.logger.info('Loaded pythonScriptsAPI')