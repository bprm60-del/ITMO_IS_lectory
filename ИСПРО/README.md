# Инструментальные средства разработки ПО (ИСПРО / ИСРПО)

---

## 1. Информация о курсе

* **Университет:** Университет ИТМО (Санкт-Петербург)
* **Преподаватель:** Повышев Владислав Вячеславович
* **Официальные материалы практик:** [sourcecraft.dev/software-development-tools/practice](https://sourcecraft.dev/software-development-tools/practice?rev=main&clckid=f4d3b050)
* **Методические материалы курса:** [Яндекс Диск](https://disk.yandex.ru/i/u4OEWh9pl1NaNA)

---

## 2. Структура дисциплины

```mermaid
graph TD
    ISPRO["Инструменты разработки ПО"] --> Git["1. Системы контроля версий (Git)<br/>ветвление, слияние, rebase, cherry-pick"]
    ISPRO --> Build["2. Системы сборки и автоматизации<br/>Make, CMake, скрипты сборки"]
    ISPRO --> Env["3. Среда разработки и CLI<br/>Bash, Linux CLI, SSH, утилиты GNU"]
    ISPRO --> CI["4. CI/CD и контейнеризация<br/>GitHub Actions, Docker, тестирование"]

    style ISPRO fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style Git fill:#fbe9e7,stroke:#ff5722
    style Build fill:#fff3e0,stroke:#ff9800
    style Env fill:#e8f5e9,stroke:#4caf50
    style CI fill:#f3e5f5,stroke:#9c27b0
```

---

## 3. Регламент оформления лабораторных работ

### Формат отчёта
Отчёт формируется в **PDF** и содержит строго два блока:

```mermaid
flowchart TD
    Report["Структура отчёта по лабораторной работе"] --> Part1["1. Титульный лист<br/>- Министерство / ИТМО<br/>- Дисциплина и тема<br/>- Выполнил (ФИО, группа, ISU)<br/>- Проверил (преподаватель)<br/>- Город и год"]
    Report --> Part2["2. Ход работы<br/>- Нумерация строго по пунктам ТЗ<br/>- Терминальные команды<br/>- Скриншоты выполнения<br/>- Без лишней 'воды' и псевдо-выводов"]
    
    style Report fill:#f5f5f5,stroke:#333
    style Part1 fill:#e8f5e9,stroke:#4caf50
    style Part2 fill:#e1f5fe,stroke:#0288d1
```

> [!IMPORTANT]
> В отчёте **не должно быть** разделов «Цель работы», «Задание», «Вывод», «Список литературы». Отчёт должен быть максимально ёмким и технически точным.

---

## 4. Рабочий процесс Git (Git Workflow)

```mermaid
gitGraph
    commit id: "Initial commit"
    branch develop
    checkout develop
    commit id: "Setup project structure"
    branch feature/lab1
    checkout feature/lab1
    commit id: "Implement Task 1"
    commit id: "Implement Task 2"
    commit id: "Add tests"
    checkout develop
    merge feature/lab1 id: "PR: Lab 1 finished"
    checkout main
    merge develop id: "Release 1.0"
```

---

## 5. Рекомендуемая литература

* **Скотт Чакон, Бен Страуб — «Pro Git»**  
  *Официальная и наиболее полная книга по архитектуре объектов Git, устройству веток, слияниям и командной работе.*
* **Роберт Мартин — «Чистый код» (Clean Code)**  
  *Стандарты промышленного форматирования, именования функций и проектирования легко поддерживаемых программ.*
* **Brian W. Kernighan, Rob Pike — «The Unix Programming Environment»**  
  *Классическое руководство по работе с командной строкой UNIX/Linux, конвейерами (pipelines) и утилитами POSIX.*
