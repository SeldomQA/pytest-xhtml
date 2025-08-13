# pytest-xhtml

pytest-xhtml is a plugin for `pytest` that generates a HTML report for test results.

## install

```bash
$ pip install pytest-xhtml
```

## usage

* unit test

```bash
cd testing_unit
$ pytest test_selenium.py --html=report.html
```
![unit test](./images/unit_report.png)

* e2e test

```bash
# install selenium library
$ pip install selenium

$ cd testing_e2e
$ pytest test_selenium.py --html=report.html
```

![e2e test](./images/e2e_report.png)

* http test

```bash
# install pytest-req library
$ pip install pytest-req

$ cd testing_req
$ pytest test_req.py --html=report.html
```
![http test](./images/http_report.png)

## Develop

```bash
$ git clone https://github.com/seldomQA/pytest-xhtml.git
$ cd pytest-xhtml
$ pip install .

$ npm run build:css
```
