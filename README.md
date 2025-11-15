Цей репозиторій містить пакет для перекладу тексту та демонстраційні скрипти.

Структура
---------
- texttranslator/ — пакет з модулями для трьох реалізацій перекладача
- gtrans4.py, gtrans3.py, deeptr.py, filetr.py — демонстраційні сценарії
- Didovets/ — (створене віртуальне оточення; в .gitignore) — не коммітити
- python312/ — (embeddable Python; в .gitignore) — не коммітити
- requirements.txt — потрібні пакети
- input_text.txt, filetr_config.json — приклад вхідних даних та конфіг

Як запустити (локально, Windows PowerShell)
-------------------------------------------
1) Активувати віртуальне оточення (створене тут як `Didovets`):

    .\Didovets\Scripts\Activate.ps1

2) Запустити демонстрацію (приклад):

    .\Didovets\Scripts\python.exe f:\\LAB\\py\\gtrans4.py

3) Запустити програму для перекладу файлу (використовує filetr_config.json):

    .\Didovets\Scripts\python.exe f:\\LAB\\py\\filetr.py
