# -*- coding: utf-8 -*-

import core.linkero as linkero
import submodules.pythonScripts.modules.alert_viewer as av

class alerts(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        filters = []
        filters.append("[todo]")
        numItems = av.countLines(av.openLog())
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            alert[0]=str(alert[0]).replace('\n', '')
        return alerts

class alertsByUser(linkero.Resource):
    @linkero.auth.login_required
    def get(self, user):
        filters = []
        filters.append("[info]")
        filters.append(user)
        numItems = 500
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            alert[0] = str(alert[0]).replace('\n', '')
        return alerts

class alertsByUserAndMonth(linkero.Resource):
    @linkero.auth.login_required
    def get(self, user, month):
        filters = []
        filters.append("[info]")
        filters.append(user)
        filters.append(month)
        numItems = 500
        alerts = av.searchLastEntries(av.openLog(), filters, numItems)
        for alert in alerts:
            alert[0] = str(alert[0]).replace('\n', '')
        return alerts

##
## Actually setup the Api resource routing here
##
def loadPythonScriptsAPI():
    linkero.api.add_resource(alerts, '/alerts')
    linkero.api.add_resource(alertsByUser, '/alerts/<user>')
    linkero.api.add_resource(alertsByUserAndMonth, '/alerts/<user>&<month>')