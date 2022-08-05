# firstprojectLex
Код для сортировки файлов. Закидывать в папку 1 файлы для распределения. В папку 2 и 3 будут рассортироваться файлы. В папке 2 будут файлы .txt , в папке 3 будут файлы с расширение .jpg .png

Нужно установить библиотеку watchdog, чтобы отслеживать события перемещения в папку нужно подключить FileSystemEventHandler.
Создаем класс что наследует от класса с событиями в котором реализуем функцию on_modified что срабатывает каждый раз при измении в определенной папке.
Перебираем все в папке folder_track (нужно указать полный путь к папке) и далее переносим эти файлы в folder_dest (полный путь к папке).
Ещё присутствует задержка по времени для выполнения программы через небольшие промежутки времени.


Немного информации об библиотеку watchdog

Реализация: Основные строительные блоки watchdog основаны на следующих классах.
- Наблюдатель (Observer).
- Обработчик событий (Event handler).

Обработчик событий: В настоящее время в модуле доступно 4 типа обработчиков событий.

= FileSystemEventHandler — базовый обработчик событий файловой системы, из которого можно переопределить методы.
- PatternMatchingEventHandler сопоставляет заданные шаблоны с путями к файлам, которые связаны с происходящими событиями.
- RegexMatchingEventHandler сопоставляет заданные регулярные выражения с путями к файлам, которые связаны с происходящими событиями.
- LoggingEventHandler регистрирует все записанные события.

Остальные классы наследуются от FileSystemEventHandler, который предоставляет для переопределения следующие функции.

- on_any_event — обработчик событий Catch-all.
- on_created вызывается при создании файла или каталога.
- on_deleted вызывается при удалении файла или каталога.
= on_modified вызывается при изменении файла или каталога.
- on_moved вызывается при перемещении или переименовании файла или каталога.
