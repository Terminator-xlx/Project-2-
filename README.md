# Flask API Project with Full Test Suite 
 
## Описание проекта 
Веб-приложение на Flask с полным набором тестов и CI/CD. 
 
## Функциональности 
- REST API для управления пользователями 
- SQLite/PostgreSQL база данных 
- Полная аутентификация (JWT) 
- Docker контейнеризация 
 
## Структура проекта 
\`\`\` 
Структура папок
Серийный номер тома: 94A6-A569
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
|   |   ИтоговыйПроект.iml
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
        
\`\`\` 
 
## Запуск тестов 
\`\`\`bash 
python -m pytest tests/ -v 
\`\`\` 
 
## Результаты тестов 
\`\`\` 
============================= test session starts =============================
platform win32 -- Python 3.10.2, pytest-7.4.0, pluggy-1.6.0 -- C:\Users\└ыхъёрэфЁ\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.10.2', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '7.4.0', 'pluggy': '1.6.0'}, 'Plugins': {'anyio': '4.6.2.post1', 'cov': '4.1.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.8.0'}}
rootdir: C:\Users\└ыхъёрэфЁ\PycharmProjects\╚Єюуют√щ╧ЁюхъЄ
plugins: anyio-4.6.2.post1, cov-4.1.0, html-4.1.1, metadata-3.1.1, xdist-3.8.0
collecting ... collected 7 items

tests/integration/test_routes.py::test_index_route PASSED                [ 14%]
tests/integration/test_routes.py::test_health_check PASSED               [ 28%]
tests/system/test_app.py::test_full_application_flow PASSED              [ 42%]
tests/unit/test_models.py::test_user_creation PASSED                     [ 57%]
tests/unit/test_models.py::test_user_to_dict PASSED                      [ 71%]
tests/unit/test_services.py::test_create_user_manually PASSED            [ 85%]
tests/unit/test_services_simple.py::test_simple_user_creation PASSED     [100%]

============================== 7 passed in 0.25s ==============================
\`\`\` 
 
## CI/CD 
Автоматический запуск тестов при push в репозиторий через GitHub Actions. 
 
## Docker 
\`\`\`bash 
docker-compose up --build 
\`\`\` 
