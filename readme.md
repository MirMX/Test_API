<p align = "center">
  <a href ="#"><img src="https://i.imgur.com/3Vg0Jfw.png" width="130" /></a>
</p>

# <p align="center">[<img src="https://i.imgur.com/G7LQsqu.png"  height="25" />](https://be-tester.ru/ "https://be-tester.ru") HomeWork - Level 2 (Automation) :fire:</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python%20&%20Magic-blue.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Total%20code--coverage-100%25-green)](#)

### Description
The Homework includes different Steps for testing API using Python with Pytest and Requests Librarys.<br>
There are four request methods will be using to complete the Task:
1. **POST** - create Isssue report,
2. **GET** - get Issue Info,
3. **PUT** - update Issue report,
4. **DEL** - delete Issue report.<br>

The assignment was designed to improve a Test Automation mastery.<br>
 
### Task and Specification/Instruction:

- <details>
  <summary><b>Issue Report </b></summary>

     Test-Case ([test_api_jira.py][1] + [post.json][5]) in the same folder<br>

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
    - <details>
      <summary><b>Logic:</b> логика работы</summary>

        Framework logic:<br>
        [<img src="https://i.imgur.com/bbnMtWJ.png" />][4]
      </details>
  </details> 
---

### How to Use:

- <details>
  <summary><b>Usage</b></summary>

    - <details>
      <summary><b>Soft Requirements:</b></summary>

        - Python 3.8.5 
        - Pytest 7.0.1 (to install use `pip install pytest` in terminal)
        - Request 2.27.1 (to install use `pip install requests` in terminal)

      </details>
    - <details>
      <summary><b>to Run Tests:</b></summary>

        
        Make sure, Test-Case ([test_api_jira.py][1] + [post.json][5]) **are in the same folder**<br>
        execute code with command below in PowerShell
        ```PowerShell
        pytest test_api_jira.py -s -v
        ```
        the key `-s` is to see print in terminal<br>
        the key `-v` is to show more detailed report
      </details>

        - <details>
          <summary><b>to chose which test to run:</b></summary>

            Uncomment `@pytest.mark.skip` to skip test(s)<br>
            [<img src="https://i.imgur.com/VJjQzF0.gif" />][2]
          </details>
    - <details>
      <summary><b>Results:</b></summary>

        There are 8 tests and each of them has his own result bases on Task Requirements:<br>
        [<img src="https://i.imgur.com/9K6i8fd.png" />][3]
      </details>
  </details> 

<!-- ----------------------------------------------------------------------- -->
[1]: /test_api_jira.py "Open File in New Tab (ctrl + click)"
[2]: https://i.imgur.com/VJjQzF0.gif "Open File in New Tab (ctrl + click)"
[3]: https://i.imgur.com/9K6i8fd.png "Open File in New Tab (ctrl + click)"
[4]: https://i.imgur.com/bbnMtWJ.png "Open File in New Tab (ctrl + click)"
[5]: /post.json "Open File in New Tab (ctrl + click)"
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