# Звіт комп’ютерного проекту
# на тему «Аналіз зв'язності графів»
# у рамках курсу Дискретної математики

Проєкт "Аналіз зв'язності графів" реалізує функціональність для аналізу орієнтованих і неорієнтованих графів, зокрема для виявлення компонент
зв'язності, компонент сильної зв'язності, артикуляційних точок та мостів. Крім того, забезпечено візуалізацію графів і зручний інтерфейс для
взаємодії з користувачем через командний рядок.     


## ФУНКЦІОНАЛ:

## 1. АНАЛІЗ ГРАФІВ

### 1.1 Компоненти зв'язності (модуль `components.py`). 
Функція `find_conn_comp(graph: dict[int: list[int]]`, `is_oriented: bool) -> list[list[int]]` з модуля `connectivity.py` визначає компоненти зв'язності
у неорієнтованому графі, використовуючи алгоритм DFS. Алгоритм пошуку в глибину (DFS) здійснює обхід графа, починаючи з обраної вершини, шляхом
рекурсивного переходу до кожної сусідньої вершини, яка ще не була відвідана.

#### Реалізація
1. Перевірка орієнтованості графа: Якщо граф орієнтований, функція припиняє виконання, оскільки для таких графів компоненти зв'язності не
визначаються аналогічно неорієнтованим графам.
2. Ініціалізація:
  * Створюється список `visited`, що відстежує, які вершини вже були оброблені.
  * Список `all_components` зберігає всі знайдені компоненти.
3. Допоміжна функція dfs:
  * Виконує рекурсивний обхід графа, починаючи з заданої вершини v.
  * Додає всі досяжні вершини до поточної компоненти.
  * Під час обходу позначає відвідані вершини.
4. Головний цикл:
  * Для кожної вершини графа виконується перевірка: якщо вершина ще не відвідана, запускається обхід dfs з формуванням нової компоненти.
  * Після завершення обходу сформована компонента додається до `all_components`.
5. Результат: Повертається список компонент зв'язності. Клмпонента зв’язності задається як список вершин цієї компоненти.



### 1.2 Компоненти сильної зв'язності (модуль `strong_con.py`). 
Модуль `strong_con.py` реалізує алгоритм Коса-раю для знаходження компонент сильної
зв'язності в орієнтованих графах. Алгоритм передбачає два основних етапи:
  * Виконання DFS для визначення порядку завершення обробки вершин.
  * Транспонування графа та виконання DFS для виявлення компонент сильної зв'язності на оберненому графі.

#### Реалізація
1. Перевірка орієнтованості графа:
Функція виконує перевірку, чи граф орієнтований. Якщо граф не орієнтований, повертається -1, оскільки компоненти сильного зв’язності визначаються лише для орієнтованих графів.

2. Ініціалізація:
  * Словник `visited`: відстежує стан відвіданості кожної вершини.
  * Список stack: накопичує вершини в порядку завершення їх обробки.
3. Допоміжна функція dfs:
  * Виконує пошук у глибину для формування стеку оброблених вершин.
4. Транспонування графа: 
  * Функція `transpose_graph` створює інверсний граф, у якому напрямок усіх ребер змінено на протилежний.

5. Пошук компонент сильного зв’язку:
    1) Головний цикл обробки графа:
      * Для кожної вершини, яка ще не відвідана, викликається dfs, що додає вершину до стеку після завершення її обробки.
    2) Обробка інверсного графа:
      * Використовуючи стек завершення, вершини знову обробляються, але вже у транспонованому графі.
      * Для кожної невідвіданої вершини запускається dfs_scc, яка формує поточну компоненту сильного зв’язку.
      * Компонента додається до списку `scc_list`.
6. Результат:
    Функція повертає список компонент сильного зв’язку. Кожна компонента представлена списком вершин, які належать до неї.



### 1.3 Точки сполучення (модуль `articulation.py`). 
Модуль `articulation.py` містить функції для виявлення артикуляційних точок( сполучення) та мостів у
графах. Алгоритм, заснований на DFS, дозволяє визначити важливі точки, видалення яких призводить до підвищення числа компонент зв'язності, а також
ребра, чиє видалення розриває граф.

#### Точки сполучення
Функція `find_points(graph, is_oriented: bool)` шукає точки сполучення в неорієнтованому графі, тобто такі вершини графа, видалення яких призводить до розірвання графу на кілька компонент звʼязності. При цьому використовується алгоритм DFS, який здійснює обхід графа, починаючи з певної вершини, шляхом рекурсивного переходу до кожної сусідньої вершини, яка ще не була відвідана.

1. Реалізація:

  * Перевірка орієнтованості графа: Якщо граф орієнтований, функція припиняє виконання, оскільки для таких графів точки сполучення не визначаються аналогічно як в неорієнтованих графах.

2. Ініціалізація:

  * Створюється список visited, що відстежує, які вершини вже були відвідані.
  Список connection_points зберігає всі знайдені точки сполучення.

3. Допоміжна функція dfs:

  * Виконує рекурсивний обхід графа, починаючи з заданої вершини node.
  Під час обходу позначає відвідані вершини.
  Якщо вершина ще не відвідана, запускається обхід dfs.

4. Головний цикл:

  * Для кожної вершини графа виконується перевірка, чи отримана довжина відвіданих вершин дорівнює довжині графа. Якщо ні, ця вершина додається до connection_points.

5. Результат:

  * Повертається список точок сполучення.


   


#### Мости
Функція `bridges(graph, is_oriented: bool)` шукає мости у неорієнтованих графах.

Реалізація:

1.Перевірка на неорієнтованість:

  * Якщо граф є орієнтований, то функція припиняє роботу, оскільки алгоритм пошуку мостів у орієнтованих графах інший.

2.Ініціалізація:

* Створюється bridges_list, куди записуються мости, way_length - довжина шляху, visited - словник, з значеннями True або False, в залежності від того чи відвідали ми вершину, first_visit_way і minimum_way - котрі розраховують шлях від однієї вершини до іншої.

3.Основний цикл:

  * Перевіряє чи є функція відвіданою, якщо ні - викликає функцію dfs. Функція dfs виконує обхід всіх вершин графа, а також розраховує шлях між вершинами. Перевіряє чи ребро є мостом і додає його в список.

4.Результат:

  * Cписок кортежів, котрі складаються з двох вершин, котрі утворюють міст.





## 2. РОБОТА З ФАЙЛАМИ, ВІЗУАЛІЗАЦІЯ, ВЗАЄМОДІЯ З КОРИСТУВАЧЕМ:

### 2.1 Модуль `read_write.py` відповідає за ефективну взаємодію з файлами графів. Реалізовано два основні методи:
* Читання графа `read_graph(filename, is_oriented)`: Читання графа з файлу, де кожен рядок визначає з'єднання між двома вершинами.
* Запис графа `write_graph(graph, new_filename)`: Запис графа у файл у форматі списку ребер, де кожне з'єднання записується в окремому рядку.


### 2.2 Візуалізація графів
Модуль `graph_visual.py` реалізує функцію для візуалізації графів за допомогою бібліотеки `networkx` та `matplotlib`. Функція працює яе з орієнтованими, так і з неорієнтованими графами. Функція створює граф за допомогою networkx та візуалізує за допомогою `matplotlib`.
Для того, щоб функція візуалізувала граф, достатньо передати словник з графом і вказати орієнтований він, чи ні.
Використовуються стандартні параметри для відображення графа:
* Вузли позначаються зеленим кольором.
* Ребра — жовтогарячими лініями.
* Кожна вершина маркована її індексом.


### 2.3 Взаємодія з користувачем
Модуль `main.py` дозволяє користувачеві через командний інтерфейс вибирати необхідні операції з графами, використовуючи бібліотеку argparse.
Цей код реалізує інтерфейс командного рядка (CLI) для аналізу властивостей графів, таких як компоненти зв'язності, точки зв'язку, мости, сильні компоненти зв'язності, а також їх візуалізація.
Спочатку граф зчитується з .csv файлу, який вкаже користувач, і також від користувача вимагається введення інформації про те, орієнтований граф, чи ні (ввід у командному рядку `--is_oriented`).
Ввід користувача в командний рядок:
* `file` (обов’язковий) — шлях до файлу з графом. Файл повинен бути у форматі .csv.
* `--is_oriented` (опціональний) — вказує, чи є граф орієнтованим.
* `--connectivity` (опціональний) — виконує пошук точок сполучення.
* `--bridges` (опціональний) — виконує пошук мостів у графі.
* `--components` (опціональний) — виконує пошук компонент зв'язності.
* `--strong_components` (опціональний) — виконує пошук сильних компонент зв'язності (тільки для орієнтованих графів).
* `--visualisation` (опціональний) — виконує візуалізацію графа.

