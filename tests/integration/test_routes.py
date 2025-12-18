"""
Интеграционные тесты для маршрутов Flask приложения.
Тестируют полный цикл запросов через HTTP клиент.
"""
import json
import pytest


class TestBasicRoutes:
    """Тесты базовых маршрутов (не связанных с пользователями)"""

    def test_index_route(self, client):
        """
        Тест корневого маршрута.
        Проверяет, что API отвечает на запрос к корню.
        """
        response = client.get('/')

        # Проверка статуса ответа
        assert response.status_code == 200
        # Проверка типа контента
        assert response.content_type == 'application/json'
        # Проверка структуры ответа
        data = response.get_json()
        assert 'message' in data
        assert data['message'] == 'Welcome to Flask API'

    def test_health_check(self, client):
        """
        Тест эндпоинта проверки здоровья.
        Проверяет, что приложение работает корректно.
        """
        response = client.get('/health')

        assert response.status_code == 200
        assert response.content_type == 'application/json'
        data = response.get_json()
        assert 'status' in data
        assert data['status'] == 'healthy'

    def test_404_not_found(self, client):
        """
        Тест обработки несуществующих маршрутов.
        """
        response = client.get('/non-existent-route')

        assert response.status_code == 404


class TestUserCreation:
    """Тесты создания пользователей"""

    def test_create_user_success(self, client):
        """
        Тест успешного создания пользователя.
        Проверяет корректность создания и ответа.
        """
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com'
        }

        response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert response.status_code == 201
        data = response.get_json()

        # Проверка всех полей в ответе
        assert data['username'] == 'newuser'
        assert data['email'] == 'newuser@example.com'
        assert 'id' in data
        assert isinstance(data['id'], int)
        assert 'created_at' in data
        assert data['id'] > 0

    def test_create_user_missing_username(self, client):
        """
        Тест создания пользователя без имени.
        Проверяет валидацию обязательных полей.
        """
        user_data = {
            'email': 'test@example.com'
            # Нет username
        }

        response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'Missing username or email' in data['error']

    def test_create_user_missing_email(self, client):
        """
        Тест создания пользователя без email.
        """
        user_data = {
            'username': 'testuser'
            # Нет email
        }

        response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data

    def test_create_user_empty_json(self, client):
        """
        Тест создания пользователя с пустым JSON.
        """
        response = client.post(
            '/api/users',
            data=json.dumps({}),
            content_type='application/json'
        )

        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data


class TestUserRetrieval:
    """Тесты получения пользователей"""

    def test_get_all_users_empty(self, client):
        """
        Тест получения всех пользователей из пустой БД.
        """
        response = client.get('/api/users')

        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_all_users_with_data(self, client):
        """
        Тест получения всех пользователей.
        """
        # Создаем несколько пользователей
        users_data = [
            {'username': 'user1', 'email': 'user1@example.com'},
            {'username': 'user2', 'email': 'user2@example.com'},
            {'username': 'user3', 'email': 'user3@example.com'}
        ]

        created_ids = []
        for user_data in users_data:
            response = client.post(
                '/api/users',
                data=json.dumps(user_data),
                content_type='application/json'
            )
            if response.status_code == 201:
                created_user = response.get_json()
                created_ids.append(created_user['id'])

        # Получаем всех пользователей
        response = client.get('/api/users')

        assert response.status_code == 200
        data = response.get_json()

        assert isinstance(data, list)
        assert len(data) >= 3

        # Проверяем структуру каждого пользователя
        for user_dict in data:
            assert 'id' in user_dict
            assert 'username' in user_dict
            assert 'email' in user_dict
            assert 'created_at' in user_dict

    def test_get_single_user_success(self, client):
        """
        Тест успешного получения одного пользователя по ID.
        """
        # Сначала создаем пользователя
        user_data = {
            'username': 'singleuser',
            'email': 'single@example.com'
        }

        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert create_response.status_code == 201
        created_user = create_response.get_json()
        user_id = created_user['id']

        # Получаем пользователя по ID
        response = client.get(f'/api/users/{user_id}')

        assert response.status_code == 200
        data = response.get_json()

        assert data['id'] == user_id
        assert data['username'] == 'singleuser'
        assert data['email'] == 'single@example.com'

    def test_get_single_user_not_found(self, client):
        """
        Тест получения несуществующего пользователя.
        """
        response = client.get('/api/users/999')

        assert response.status_code == 404
        data = response.get_json()
        assert 'error' in data
        assert 'User not found' in data['error']

    def test_get_user_invalid_id_format(self, client):
        """
        Тест получения пользователя с неверным форматом ID.
        """
        response = client.get('/api/users/not-a-number')

        # Flask вернет 404, так как маршрут не найден
        assert response.status_code == 404


class TestUserDeletion:
    """Тесты удаления пользователей"""

    def test_delete_user_success(self, client):
        """
        Тест успешного удаления пользователя.
        """
        # Создаем пользователя
        user_data = {
            'username': 'todelete',
            'email': 'delete@example.com'
        }

        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert create_response.status_code == 201
        created_user = create_response.get_json()
        user_id = created_user['id']

        # Удаляем пользователя
        response = client.delete(f'/api/users/{user_id}')

        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'User deleted'

        # Проверяем, что пользователь удален
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 404

    def test_delete_user_not_found(self, client):
        """
        Тест удаления несуществующего пользователя.
        """
        response = client.delete('/api/users/999')

        assert response.status_code == 404
        data = response.get_json()
        assert 'error' in data
        assert 'User not found' in data['error']


class TestInvalidHTTPMethods:
    """Тесты неверных HTTP методов"""

    def test_invalid_method_on_users_collection(self, client):
        """
        Тест неразрешенных методов на /api/users.
        """
        # PUT не разрешен
        response = client.put('/api/users')
        assert response.status_code == 405

        # PATCH не разрешен
        response = client.patch('/api/users')
        assert response.status_code == 405

    def test_invalid_method_on_single_user(self, client):
        """
        Тест неразрешенных методов на /api/users/<id>.
        """
        # Сначала создаем пользователя
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com'
        }

        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert create_response.status_code == 201
        created_user = create_response.get_json()
        user_id = created_user['id']

        # POST не разрешен
        response = client.post(f'/api/users/{user_id}')
        assert response.status_code == 405

        # PUT не разрешен
        response = client.put(f'/api/users/{user_id}')
        assert response.status_code == 405

        # PATCH не разрешен
        response = client.patch(f'/api/users/{user_id}')
        assert response.status_code == 405


class TestResponseFormats:
    """Тесты форматов ответов"""

    def test_json_response_structure(self, client):
        """
        Тест структуры JSON ответов.
        """
        # Создаем пользователя
        user_data = {
            'username': 'jsonuser',
            'email': 'json@example.com'
        }

        create_response = client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        assert create_response.status_code == 201
        created_user = create_response.get_json()
        user_id = created_user['id']

        # Тест для одиночного пользователя
        response = client.get(f'/api/users/{user_id}')
        data = response.get_json()

        # Проверяем все ожидаемые поля
        expected_keys = {'id', 'username', 'email', 'created_at'}
        assert set(data.keys()) == expected_keys

        # Проверяем типы данных
        assert isinstance(data['id'], int)
        assert isinstance(data['username'], str)
        assert isinstance(data['email'], str)
        assert isinstance(data['created_at'], str)  # ISO format string

        # Тест для списка пользователей
        response = client.get('/api/users')
        data_list = response.get_json()

        if data_list:  # если список не пустой
            for item in data_list:
                assert set(item.keys()) == expected_keys