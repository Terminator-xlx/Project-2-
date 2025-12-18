# Flask API Project with Full Test Suite 
 
C:.
|   config.py
|   docker-compose.yml
|   Dockerfile
|   fix_tests.bat
|   README.md
|   requirements.txt
|   run.py
|   setup.py
|   
+---.github
|   \---workflows
|           ci-cd.yml
|           
+---.idea
|   |   misc.xml
|   |   modules.xml
|   |   workspace.xml
|   |   ˆâ®£®¢ë©à®¥ªâ.iml
|   |   
|   \---inspectionProfiles
|           profiles_settings.xml
|           
+---.pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |   
|   \---v
|       \---cache
|               lastfailed
|               nodeids
|               stepwise
|               
+---app
|   |   database.py
|   |   models.py
|   |   routes.py
|   |   services.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           database.cpython-310.pyc
|           models.cpython-310.pyc
|           routes.cpython-310.pyc
|           services.cpython-310.pyc
|           __init__.cpython-310.pyc
|           
+---flask_app.egg-info
|       dependency_links.txt
|       PKG-INFO
|       SOURCES.txt
|       top_level.txt
|       
+---tests
|   |   conftest.py
|   |   
|   +---integration
|   |   |   test_routes.py
|   |   |   
|   |   \---__pycache__
|   |           test_routes.cpython-310-pytest-7.4.0.pyc
|   |           
|   +---system
|   |   |   test_app.py
|   |   |   
|   |   \---__pycache__
|   |           test_app.cpython-310-pytest-7.4.0.pyc
|   |           
|   +---unit
|   |   |   test_models.py
|   |   |   test_services.py
|   |   |   test_services_simple.py
|   |   |   
|   |   \---__pycache__
|   |           test_models.cpython-310-pytest-7.4.0.pyc
|   |           test_services.cpython-310-pytest-7.4.0.pyc
|   |           test_services_simple.cpython-310-pytest-7.4.0.pyc
|   |           
|   \---__pycache__
|           conftest.cpython-310-pytest-7.4.0.pyc
|           
\---__pycache__
        config.cpython-310.pyc
        

\`\`\`bash 
python -m pytest tests/ -v 
\`\`\` 
