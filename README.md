<h1 align="center">Проект по тестированию онлайн-магазина 
<p align="center">
<a href="https://my-shop.ru/" target="_blank">
<img src="https://s.rbk.ru/v1_companies_s3/resized/960xH/media/trademarks/91cbd2c0-7f6c-48e5-ba52-f72f348a2f65.jpg" 
alt="МАЙШОП" width="128" height="64"> </a> 
</p></h1>

<!-- Тест кейсы -->

## Автоматизировано тестирование функционала:
* Проверка главного меню сайта
* Поле поиска в хедере (позитивный и негативный сценарий)
* Добавление и удаление товара в избранное
* Добавление и удаление товара из корзины


## Структура проекта
# <a name="Technology">Технологии и инструменты</a>
<p  align="center">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="media/logo/selenium.png"></code>
  <code><img width="5%" title="Selene" src="media/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="media/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="media/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>


В данном проекте автотесты написаны на **Python** с использованием фреймворка **Pytest**,
используя популярные библиотеки **Selene, WebDriver-Manager, Selenium**.
Запуск тестов выполняется из **Jenkins**.
**Selenoid** используется для запуска браузеров в контейнерах **Docker**.
**Allure Report, Telegram Bot** используются для визуализации результатов тестирования.


## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job  /">Ссылка на проект в Jenkins</a>









# <a name="AllureReport">Отчет о результатах тестирования в [Allure Report](https://jenkins.autotests.cloud/job/10_da-vasilev_qa-guru-hw25/23/allure/)</a>

#### Общая информация
Главная страница Allure-отчета содержит следующие информационные блоки:

>- <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество прогнанных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
<p align="center">

[//]: # (  <img src="[[[[images/Allure Report]]]].png" alt="Allure Report" width="650">)
</p>

### Список тестов c описанием шагов и визуализацией результатов
На данной странице представляется стандартное распределение выполнявшихся тестов по тестовым наборам или классам, в
которых находятся тестовые методы.



# <a name="AllureTestOps">Интеграция с [Allure TestOps](https://allure.autotests.cloud/project/1203/)</a>

### Основной дашборд
<p align="center">

[//]: # (  <img src="images/allureTestOPS dashboards.png" alt="dashboards" width="650">)
</p>

### Дашборд по разным типам тестов
<p align="center">

[//]: # (  <img src="images/allureTestOPS dashboards test types.png" alt="dashboards test types" width="650">)
</p>

### Запуски
<p align="center">

[//]: # (  <img src="images/allureTestOPS launches.png" alt="launches" width="650">)
</p>

### Результат запуска
<p align="center">

[//]: # (  <img src="images/allureTestOPS launch.png" alt="launch" width="750">)
</p>

### Тест-кейсы
<p align="center">

[//]: # (  <img src="images/Test cases.png" alt="test cases" width="750">)
</p>

### Дефекты
<p align="center">

[//]: # (  <img src="images/testOps_defect.png" alt="defects" width="750">)
</p>



<!-- # <a name="Jira">Интеграция с [Jira](https://jira.autotests.cloud/)</a> -->



# <a name="Results">Результаты выполнения тестов</a>

### Пример запуска теста в Browserstack
<p align="center">

[//]: # (  <img src="images/videoMob.gif" alt="video" width="700">)
</p>

### Пример запуска теста в Selenoid
<p align="center">

[//]: # (    <img src="images/videoUI.jpg" alt="defects" width="900">)

[//]: # (<!--     <video src='images/videoMob.mp4' width=450/> -->)
</p>

### Уведомления в Telegram
<p align="center">

[//]: # (  <a href="http://www.pidor.com/"><img src="images/tlgrm.png" alt="Telegram" width="550"></a>)
</p>
