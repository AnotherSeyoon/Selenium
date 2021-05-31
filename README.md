# Python Selenium

파이썬 셀레늄을 공부해보자

---
## install

일반 파이썬 환경이라면 pip(pip3)를 사용하고, 아나콘다를 사용한다면 conda를 사용한다

<pre><code>pip install selenium
conda install selenium</code></pre>

일반적인 파이썬 라이브러리와는 다르게, 브라우저별로 selenium webdriver를 다운로드해야 한다. 저는 크롬을 사용했다.

* [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

![Downloads Img](https://media.discordapp.net/attachments/721987795677216811/848866627483205662/E18489E185B3E1848FE185B3E18485E185B5E186ABE18489E185A3E186BA202021-05-3120E1848BE185A9E18492E185AE20.png)

본인이 사용하는 브라우저의 버전에 맞는 webdriver를 다운받아야 한다.
크롬의 버전은 [여기](chrome://version)에서 확인하거나 오른쪽 위 `점 3개 > 도움말 > Chrome 정보` 에서 확인 할 수 있다.

다운받은 파일을 Python 파일과 같은 디렉토리에 둔다. 다른곳에 두어도 상관없지만, driver 경로를 입력하기 귀찮아질 수 있다.

---

## Import