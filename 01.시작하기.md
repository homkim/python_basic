# 예제로 배우는 파이썬 프로그래밍

## 1. Python 언어

파이썬 (Python)은 범용 프로그래밍 언어로서 코드 가독성(readability)와 간결한 코딩을 강조한 언어이다.
파이썬은 인터프리터(interpreter) 언어로서, 리눅스, Mac OS X, 윈도우즈 등 다양한 시스템에 널리 사용된다.

Python은 원래 그리스 신화에서 그리스 중부 델파이를 지배하였던 큰 뱀인데, 제우스의 아들 아폴로에 의해 화살을 맞고 죽게된다.

![](https://upload.wikimedia.org/wikipedia/commons/2/20/Virgil_Solis_-_Apollo_Python.jpg)



## 2. Python의 간단한 역사

Python은 1989년 12월 네델란드 개발자 Guido van Rossum 에 의해 개발되기 시작하여, 약 1년 간 개발하여 1991년 처음 Python 0.9 버전을 세상에 내놓았다. 그후 정식 Python 1.0 버젼은 1994년에 출시되었으며, Python 2.0은 2000년에, Python 3.0은 2008년에 각각 출시되었다.

![](http://www.pythonstudy.xyz/images/basics/guido.jpg)


**Guido van Rossum** 1956년 생의 네델란드 개발자로서 Python 창시자. 네델란드 CWI, 미국 NIST 등의 여러 연구소에서 근무하였으며, 구글에서 약 7년간 근무, 현재는 Dropbox에서 일하고 있다.
Python이 구글에서 상당히 많은 프로젝트에 쓰여지고 있다는 점과 Dropbox의 많은 코드가 Python으로 작성되었다는 점은 아마 우연이 아닐 것이다.

Guido는 파이썬의 개발 동기에 대해 이렇게 말하고 있다.

"약 6년 전인 1989년 12월, 크리스마스를 전후하여 취미로 만들어 볼 프로그래밍 프로젝트를 찾고 있었죠. 그 때 사무실은 잠겨있어지만, 집에 컴퓨터가 있었고, 뭐 특별히 할 일도 없었죠. 그래서 그 때 당시 한동안 생각하고 있었던 새 스크립트 언어에 대한 인터프리터를 만들어 보기로 했죠. 유닉스/C 해커들에게 어필할 수 있는, ABC 언어로부터 파생된 언어말이죠. 나는 그 프로젝트명으로 Python이라는 이름을 선택했는데, 그 당시 약간은 불손한 기분이 들어서이기도 했고, 또한 당시 Monty Python's Flying Circus(BBC 코메디)에 열성팬이기도 하여..." - 1996, Guido

# Python 설치

Python은 윈도우즈, Mac, 리눅스 등에 설치하여 사용할 수 있다. 다음은 각 OS별 간단한 설치 방법을 설명한 것이다. 널리 사용되는 Python 버젼으로, 실무에서 많이 사용되었던 Python 2 버전 (예: v2.7)과 새로운 기능을 계속 업그레이드하고 있는 Python 3 버전 (예: v3.7)이 있는데, 이 두 버전 간의 호환성 문제가 존재한다. 여기서는 Python 3 버전를 사용한다.

## 1. 윈도우즈에서 Python 설치
01. 브라우저에서 https://www.python.org/downloads/ 방문
02. 윈도우즈용 Python 3 버젼 다운 받아 설치
03. 설치마법사에서 Custom 설치를 선택, 옵션에서 "Python 경로 환경변수에 추가"를 선택하면 편리

![](http://www.pythonstudy.xyz/images/basics/Python-Windows-Install.png)


## 2. Mac OSX에서 Python 설치
1. 브라우저에서 https://www.python.org/downloads/ 방문
2. Mac 용 Python 3 버젼 패키지 다운
3. 패키지를 오픈해서 설치
4. Python 실행파일 경로는 PATH에 자동으로 추가된다(.bash_profile)

## 3. Linux에서 Python 설치 (Centos)
리눅스 설치 방법은 여러 방법이 있는데, 아래는 이중 한 예로 Centos 7에서 수작업으로 최신 버젼을 다운받아 설치하는 예이다.

1. 아래 URL에서 압축파일 다운로드
```bash
$ wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
```

2. 압축해제
```bash
$ tar xf Python-3.5.1.tar.xz
```

3. 빌드
```
$ cd ./Python-3.5.1
$ ./configure   #빌드 준비
$ make          #빌드
```

4. 설치: 디폴트로 설치된 2.7버젼과 병행하여 사용하기 위해, 아래와 같이 make install (기존 2.7을 덮어씀) 대신 make altinstall을 사용한다.
```bash
$ make altinstall   
```

5. 실행 테스트
```bash
$ python3.5
```

## 파이썬 시작하기

파이썬 설치가 끝났으면, Python을 실행하고 간단한 테스트를 실행해 보자.

## 1. 윈도우즈에서 Python 실행
윈도우즈에서 Python을 실행하기 위해서는, [시작] - [프로그램] - [Python 3.5]에서 "Python 3.5 (32bit)" 콘솔프로그램 혹은 "IDLE (Python 3.5 32-bit)" 윈도우 프로그램을 실행한다. 이 프로그램들은 흔히 대화형 인터프리터 혹은 Python Shell 이라고 불리운다.

아래는 "Python 3.5 (32bit)" 프로그램을 실행한 예인데, str이라는 변수에 Hello World를 넣고, 이를 프린트하는 예제이다.


![](http://www.pythonstudy.xyz/images/basics/win-run-python.png)

여기서 처음 나오는 >>> 는 Python 인터프리터의 프롬프트(Prompt)로서 사용자 입력을 기다리는 표시이다. 이 프롬프트에 입력된 문장들은 파이썬 인터프리터가 해석하고 실행하게 되고, 결과를 출력해 주게 된다. 이렇게 사용자로부터 입력을 받아 (Read), 문장을 즉시 해석하고 평가하며 (Evaluate), 그 출력 결과를 표시한 후(Print), 다시 프롬프트로 돌아가는 (Loop) 프로그램을 흔히 REPL 툴이라 부른다.

Python을 마치고 빠져나오기 위해서는 윈도우즈에서 Ctrl+Z를 사용한다 (Mac 혹은 리눅스는 Ctrl+D를 사용한다). OS와 상관없이 종료하기 위해서는 프롬프트에서 exit() 을 사용할 수 있다.

## 2. Mac에서 Python 실행

Mac에서 Python을 실행하기 위해서는, 터미널(Terminal) 프로그램을 실행하고, "python3.5"를 실행한다. 실행파일에 대한 PATH는 설치시 .bash_profile에 설정된다. Mac에는 python 2.7이 Built-in 되어 있으며, "python"을 실행하면 2.7 버전이 실행된다.

아래 그림은 간단히 Hello World를 출력하고 REPL 프로그램을 종료하는 예이다.

![](http://www.pythonstudy.xyz/images/basics/mac-run-python.png)

## 3. 리눅스에서 Python 실행
리눅스에서 Python을 실행하기 위해서는 프롬프트에서 "python3.5"를 실행한다. 리눅스에 python 2.7이 Built-in 되어 있는 경우, "python"을 실행하면 2.7 버전이 실행된다. (단, 설치에서 설명하였듯이, 2.7 버전을 Overwrite하여 인스톨하지 않은 경우)

아래 그림은 간단한 산술식 계산을 하고 Hello World를 출력한 후 REPL 프로그램을 종료하는 예이다.

![](http://www.pythonstudy.xyz/images/basics/linux-run-python.png)



## Python 간단한 프로그램 작성

일반적으로 실제 파이썬으로 프로그래밍을 하기 위해서는 대화형 인터프리터를 사용하지 않고, 여러 종류의 에디터를 사용하여 파이썬 프로그램 파일을 작성한 후 이를 실행하게 된다.

우선 Notepad와 같은 간단한 에디터로 다음과 같은 코드를 작성하고 이를 test.py 파일로 저장해 보자. 파이썬 프로그램 파일은 관례적으로 .py 확장자를 사용한다.


```python {.line-numbers}
a = 1
b = 2
c = a + b
 
print(c)
```
 
파이썬 파일 test.py를 실행하기 위해서는 python.exe 뒤에 해당 파이썬 파일을 주고 다음과 같이 실행하게 된다.

```bash
C:\Test> python test.py
3
```

## Python 편집기/IDE 소개
파이썬 프로그래밍을 보다 편리하게 하기 위하여 파이썬 전용 에디터 혹은 IDE를 설치하여 사용할 수 있다. 파이썬 편집기/IDE로는 PyCharm, Visual Studio Code, Eclipse/PyDev, Eric, Python Tools for Visual Studio, Komodo, Atom 등 매우 다양한 툴들이 있는데, 여기서는 Cross Platform에서 동작하면서 많이 사용되는 JetBrains의 PyCharm를 사용해 보자. 참고로 윈도우즈 Visual Studio에 익숙한 개발자는 Python Tools for Visual Studio 를 사용하면 편리하다.

1. PyCharm을 설치하기 위해서는 https://www.jetbrains.com/pycharm/download 에서 PyCharm Community Edition을 다운받아 설치한다.

![](http://pythonstudy.xyz/images/basics/pycharm-install.png)

2. 설치후에 PyCharm을 실행하고, [Create New Project]를 선택한다. 새 프로젝트 위치를 지정한다.
3. [File] -> [New...] -> [Python File]을 선택한다. 파일명(예: test.py)를 적고 새 파일을 생성한다.
4. 에디터에 코드를 쓰고, 저장한다. 오른쪽 마우스 버튼을 누르고 [Run] 메뉴를 선택한다.

![](http://pythonstudy.xyz/images/basics/pycharm-run.png)
