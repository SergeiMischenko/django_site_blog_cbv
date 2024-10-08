<h1 align="center">Блог 2.0 на Django</h1>
Данный проект представляет собой модернизированный блог на Django, разработанный поэтапно. В нём реализованы расширенные функции на основе классовых представлений, древовидных категорий, комментариев, системы тегов и других технологий. Ниже приведены ключевые этапы разработки и реализованные возможности.

<h2 align="center">Содержание</h2>

1. [Основы проекта](#основы-проекта)
2. [Комментарии, теги и лайки](#комментарии-теги-и-лайки)
3. [Кэширование и оптимизация](#кэширование-и-оптимизация)

---

### Основы проекта

В первом этапе разработки проекта "Блог 2.0" я внедрил основные возможности:

- Использовал классовые представления для работы с постами (ListView, DetailView, CreateView, UpdateView, DeleteView).
- Реализовал систему древовидных категорий (с подкатегориями) для удобной навигации по блогу с помощью Django MPTT.
- Оптимизировал SQL-запросы для повышения производительности с помощью Django-Debug-Toolbar.
- Добавил возможность пользователям создавать записи, а авторам — редактировать свои посты.

### Комментарии, теги и лайки

На втором этапе я значительно расширили функционал:

- Внедрил систему древовидных комментариев с возможностью добавления комментариев без перезагрузки страницы с помощью JavaScript.
- Добавил тегирование постов для улучшения навигации и поиска.
- Установил редактор CKEditor 5 для удобного создания контента.
- Реализовал систему лайков и дизлайков на JavaScript без перезагрузки страницы.
- Внедрил защиту с помощью ReCAPTCHA на страницах авторизации/регистрации и т.д.

### Кэширование и оптимизация

Для оптимизации производительности и улучшения пользовательского опыта я:

- Настроил кэширование данных на примере системы статусов пользователей.
- Добавил RSS-ленту для постов блога.
- Реализовал обработку страниц ошибок (404, 403, 500) с кастомными шаблонами.

---

<h2 align="center">Технологии, которые я использовал:</h2>

- Django
- JavaScript (для реализации асинхронного взаимодействия)
- Bootstrap 5
- CKEditor 5
- django-mptt
- django-recaptcha
- django-taggit

<h2 align="center">Установка и запуск</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/your-username/django_site_blog_cbv.git
    ```

2. **Перейдите в папку проекта:**
    ```bash
    cd django_site_blog_cbv
    ```

3. **Установите виртуальное окружение и активируйте его:**
    ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows
    ```
    
4. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
    
5. **Откройте файл .env и заполнить его своими данными**
    ```env
    SECRET_KEY = 'your-secret-key'
    
    RECAPTCHA_PUBLIC_KEY = 'your-recaptcha-public-key'
    RECAPTCHA_PRIVATE_KEY = 'your-recaptcha-private-key'
    ```

6. **Выполните миграции:**
    ```bash
    python manage.py migrate
    ```

7. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

8. **Доступ к приложению:**
   
    После завершения всех вышеуказанных шагов, приложение будет доступно по адресу http://127.0.0.1:8000.