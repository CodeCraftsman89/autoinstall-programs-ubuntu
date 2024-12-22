# Ubuntu Program Installer / Установщик программ для Ubuntu

Ubuntu Program Installer – это консольное приложение на Python, предназначенное для автоматической установки и удаления программ на Ubuntu. Оно поддерживает работу с традиционными репозиториями, Flatpak, Flathub и Snap. / Ubuntu Program Installer is a Python-based command-line application designed for automatic installation and removal of programs on Ubuntu. It supports traditional repositories, Flatpak, Flathub, and Snap.

Программа также включает автоматизированные скрипты для установки Flatpak, PioneerStation и TRIK Studio. / The application also includes automated scripts for installing Flatpak, PioneerStation, and TRIK Studio.

## Возможности / Features

- Установка программ из стандартного репозитория Ubuntu. / Install programs from the standard Ubuntu repository.
- Удаление программ из стандартного репозитория. / Remove programs from the standard Ubuntu repository.
- Установка программ из Flathub. / Install programs from Flathub.
- Удаление программ из Flathub. / Remove programs from Flathub.
- Установка программ из Snap. / Install programs from Snap.
- Удаление программ из Snap. / Remove programs from Snap.

## Интерфейс / Interface

Программа предоставляет консольный интерфейс для управления действиями: / The application provides a command-line interface for managing actions:

```
1. Install programs
2. Remove programs
3. Install flathub programs
4. Remove flathub programs
5. Install snap programs
6. Remove snap programs
7. Exit
Enter your choice:
```

## Требования / Requirements

- Python 3.8 или выше / Python 3.8 or higher
- Ubuntu 20.04 или выше / Ubuntu 20.04 or higher
- Пакеты: `os`, `subprocess` / Packages: `os`, `subprocess`

## Установка и запуск / Installation and Execution

1. Клонируйте репозиторий: / Clone the repository:
    ```bash
    git clone https://github.com/CodeCraftsman89/autoinstall-programs-ubuntu.git
    ```

2. Перейдите в директорию проекта: / Navigate to the project directory:
    ```bash
    cd autoinstall-programs-ubuntu
    ```

3. Запустите скрипт с правами суперпользователя: / Run the script with superuser privileges:
    ```bash
    sudo python3 main.py
    ```
   
## Изменение переключения языка на Alt+Shift / Change language switching to Alt+Shift
1. Перейдите в директорию проекта если вы не в ней: / Navigate to the project directory:
    ```bash
    cd autoinstall-programs-ubuntu
    ```
2. Запустите скрипт с правами суперпользователя: / Run the script with superuser privileges:
    ```bash
    ./alt_shift.sh
    ```
   
## Как использовать / How to Use

1. После запуска программы выберите номер действия из предложенного списка. / After launching the application, select an action number from the list.
2. Следуйте инструкциям в консоли. / Follow the instructions in the console.

Пример работы: / Example:

```
1. Install programs
2. Remove programs
3. Install flathub programs
4. Remove flathub programs
5. Install snap programs
6. Remove snap programs
7. Exit
Enter your choice: 1
Enter the name of the program to install: gedit
Installing gedit...
Successfully installed gedit!
```

## Функциональные особенности / Functional Features

### Установка Flatpak, PioneerStation и TRIK Studio / Installation of Flatpak, PioneerStation, and TRIK Studio

Программа может автоматически установить эти инструменты: / The application can automatically install these tools:

- **Flatpak**: Для работы с Flathub. / For working with Flathub.
- **PioneerStation**: Программное обеспечение для робототехники. / Robotics software.
- **TRIK Studio**: Среда разработки для программирования роботов. / Development environment for programming robots.

Эти инструменты можно выбрать из предустановленного списка программ в меню. / These tools can be selected from the predefined list of programs in the menu.

## Авторы / Authors

- **CodeCraftsman89** (https://github.com/CodeCraftsman89/). 

## Лицензия / License

Этот проект распространяется под лицензией MIT. Подробности см. в файле LICENSE. / This project is licensed under the MIT License. See the LICENSE file for details.
