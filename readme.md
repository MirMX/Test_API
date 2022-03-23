<p align = "center">
  <a href ="#"><img src="https://i.imgur.com/3Vg0Jfw.png" width="130" /></a>
</p>

# <p align="center">[<img src="https://i.imgur.com/G7LQsqu.png"  height="25" />](https://be-tester.ru/ "https://be-tester.ru") HomeWork - Level 2 (Automation) :fire:</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python%20&%20Magic-blue.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Total%20code--coverage-100%25-green)](#)

### Description
The Homework includes different Steps for testing API using Python with Pytest and Requests Librarys.<br>
There are four request methods will be using to complete the Task:
1. __POST__ - create Isssue report,
2. __GET__ - get Issue Info,
3. __PUT__ - update Issue report,
4. __DEL__ - delete Issue report.<br><br>
The assignment was designed to improve a Test Automation mastery.<br>
 
### Task and Specification/Instruction:

- <details>
  <summary><b>Issue Report</b></summary>

     [Test-Case][1]&nbsp;&nbsp;&nbsp;&nbsp; [![Generic badge](https://img.shields.io/badge/code--coverage-100%25-green)](#)<br>

    - <details>
      <summary><b>Instruction:</b> инструкция по выполнению</summary>

            1. Создайте баг-репорт
            2. Получите информацию о баг-репорте
                • проверьте, что ответ статуса 200
                • скорость запроса быстрее 3000ms
                • наличие заголовка Date в ответе
                • что тип документа Баг
            3. Назначьте себя исполнителем в баг-репорте
                • Добавьте перед этим метод Get current user
                    o Добавьте тест, что в ответе displayName содержит Be Tester
            4. Удалите баг-репорт
                • Добавьте тест, что ответ статуса 204
            5. Автоматизируйте все сценарии
      </details>
  </details> 
---

### How to Use:

- <details>
  <summary><b>Usage</b></summary>

    - <details>
      <summary><b>Soft Requirements:</b></summary>

        1. Python 3.8.5
        2. Pytest 7.0.1
        3. Request 2.27.1

      </details>
    - <details>
      <summary><b>to Run Tests:</b></summary>

        execute code with command below in PowerShell
        ```PowerShell
        pytest test_api_jira.py -s -v
        ```
        the key -s is to see print in terminal<br>
        the key -v is to show more detailed report
      </details>

        - <details>
          <summary><b>to chose which test to run:</b></summary>

            Chose test(s) that shold be skipped if nessesary
            [<img src="https://i.imgur.com/VJjQzF0.gif"  height="300" />][2]
          </details>
    - <details>
      <summary><b>Results:</b></summary>

        There are 8 tests and each of them has his own result bases on Task Requirements:
        [<img src="https://i.imgur.com/9K6i8fd.png"  height="300" />][3]
      </details>
  </details> 

<!-- ----------------------------------------------------------------------- -->
[1]: /test_api_jira.py "Open File in New Tab (ctrl + click)"
[2]: https://i.imgur.com/VJjQzF0.gif "Open File in New Tab (ctrl + click)"
[3]: https://i.imgur.com/9K6i8fd.png "Open File in New Tab (ctrl + click)"
<!-- ----------------------------------------------------------------------- -->

---
### Contributors

 - **Maxim Mir**

 ---
<details>

<summary><b>:zap: GitHub Stats</b></summary>

  [![MirMX's GitHub stats](https://github-readme-stats.vercel.app/api?username=MirMX&hide=contribs,prs&show_icons=true&&theme=dark&hide_border=false&title_color=007acc&icon_color=79ff97&bg_color=151515&border_color=0c1a25")](#)
  
  [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=MirMX&repo=test_api&theme=dark&&title_color=007acc&show_icons=true&layout=compact)](#)
</details>

---  

###### <p align ="center">[<img align ="center" src="https://i.imgur.com/3Vg0Jfw.png" width="30" />](#)&nbsp;&nbsp; © 2022 MirMX</p>