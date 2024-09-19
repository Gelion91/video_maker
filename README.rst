video_maker
====

Позволяет создать видео из секвенций.
Требования Python 3.8 или более поздние версии.

Установка
----

Создайте виртуальное окружение и активируйте его. Потом установите все необходимые зависимости:

.. code-block:: text

    pip install -r requirements.txt

Запуск
----

Терминал:

.. code-block:: text

    $ python create_video.py 'path_to_folder_with_sequence' 'name_sequence_without_number' 'name_video_file.mov'


Или веб интерфейс:

.. code-block:: text

    $ flask --app core run