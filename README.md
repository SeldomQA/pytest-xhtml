# pytest-xhtml

pytest-xhtml is a plugin for `pytest` that generates a HTML report for test results.

⚠ **`pytest-xhtml` is the alternative library for `pytest-html`. If you have installed `pytest-html`, please uninstall it first.**

## install

```bash
# pip install
$ pip install pytest-xhtml
```

## usage

* unit test

```bash
cd testing_unit
$ pytest test_sample.py --html=report.html
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
# develop 
git clone https://github.com/seldomQA/pytest-xhtml.git
$ cd pytest-xhtml
$ pip install .

$ npm run build:css
```
