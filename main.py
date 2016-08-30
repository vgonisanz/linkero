# -*- coding: utf-8 -*-

# 1) Linkero Core
import core.linkero as linkero

# 2) APIs developed to use with Linkero
import examples.testAPI
import API.pythonScriptsAPI

# 3) Load desired APIs
examples.testAPI.loadTestAPI()
API.pythonScriptsAPI.loadPythonScriptsAPI()

# 4) Run Linkero
linkero.run()
