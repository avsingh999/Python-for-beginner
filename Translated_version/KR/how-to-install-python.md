이 안내서는 Linux, Windows 및 Mac 용 Python 3을 설치하고 설정하는 방법을 알려줍니다.

# Windows :

1 단계 : Python 3 설치 프로그램 다운로드

-브라우저 창을 열고 [python.org] (python.org)에서 Windows 용 [다운로드 페이지] (https://www.python.org/downloads/windows/)로 이동하십시오.
-맨 위에있는 Python Releases for Windows라는 제목 아래에서 최신 Python 3 릴리스-Python 3.x.x 링크를 클릭하십시오.
-맨 아래로 스크롤하여 64 비트 용 Windows x86-64 실행 가능 설치 관리자 또는 32 비트 용 Windows x86 실행 가능 설치 관리자를 선택하십시오.

### 2 단계 : 설치 관리자 실행

설치 프로그램을 선택하고 다운로드했으면 다운로드 한 파일을 두 번 클릭하여 설치 프로그램을 실행하십시오.

대화 상자가 나타납니다.

그런 다음 지금 설치를 클릭하십시오. 거기에 모든 것이 있어야합니다. 몇 분 후에 시스템에 Python 3을 설치해야합니다.

# 리눅스 :

Linux 배포판에 Python이 이미 설치되어있을 가능성이 매우 높지만 아마도 최신 버전이 아닐 수도 있으며 Python 3 대신 Python 2 일 수 있습니다.

사용중인 버전을 확인하려면 터미널 창을 열고 다음 명령을 시도하십시오.

``파이썬-버전 ''

``python2-버전 ''

``python3-버전 ''

이러한 명령 중 하나 이상이 다음과 같이 버전으로 응답해야합니다.

``$ python3-버전 ''
표시된 버전이 Python 2.x.x 또는 최신 버전이 아닌 Python 3 버전 (이 글을 쓰는 시점에서 3.6.5) 인 경우 최신 버전을 설치하려고합니다. 이를 수행하는 절차는 실행중인 Linux 배포판에 따라 다릅니다.

pyenv라는 도구를 사용하여 Linux에서 여러 Python 버전을 관리하는 것이 더 쉬운 경우가 많습니다. 이에 대한 자세한 내용은 여기의 기사를 참조하십시오.

# macOS / Mac OS X :

macOS에 Python 3을 설치하는 가장 좋은 방법은 [Homebrew package manager] (https://brew.sh/)를 사용하는 것입니다. 이 접근법은 또한 [Hitchhiker 's Guide to Python] (http://docs.python-guide.org/en/latest/starting/install3/osx/)와 같은 커뮤니티 가이드에서도 권장합니다.

1 단계 : Homebrew 설치 (1 부)

시작하려면 먼저 Homebrew를 설치하려고합니다.

브라우저를 열고 [http://brew.sh/](http://brew.sh/)로 이동하십시오.

페이지 로딩이 완료되면“Install Homebrew”에서 Homebrew 부트 스트랩 코드를 선택하십시오.

그런 다음 Cmd + C를 눌러 클립 보드에 복사하십시오.

설치가 실패하므로 complete 명령의 텍스트를 캡처했는지 확인하십시오.

이제 Terminal.app 창을 열고 Homebrew 부트 스트랩 코드를 붙여 넣은 다음 Enter 키를 눌러야합니다.

Homebrew 설치가 시작됩니다.

새로 설치 한 macOS에서이 작업을 수행하는 경우 Apple의 "명령 줄 개발자 도구"를 설치하라는 팝업 경고가 표시 될 수 있습니다. 설치를 계속하려면 설치가 필요하므로 "설치"를 클릭하여 대화 상자를 확인하십시오.

이 시점에서 명령 행 개발자 도구의 설치가 완료 될 때까지 기다리는 데 몇 분이 걸릴 것입니다. 커피 나 차를 먹을 시간입니다!

2 단계 : Homebrew 설치 (2 부)

명령 행 개발자 도구 설치가 완료된 후 Homebrew와 Python을 계속 설치할 수 있습니다.

개발자 도구 설치 프로그램에서 "소프트웨어가 설치되었습니다"대화 상자를 확인하십시오.

터미널로 돌아가서 Enter를 눌러 Homebrew 설치를 계속하십시오.

Homebrew는 설치를 완료 할 수 있도록 암호를 입력하라는 메시지를 표시합니다. 계속하려면 사용자 계정 비밀번호를 입력하고 Enter를 누르십시오.

인터넷 연결에 따라 Homebrew에서 필요한 파일을 다운로드하는 데 몇 분이 걸립니다. 설치가 완료되면 터미널 창의 명령 프롬프트로 돌아갑니다.

아휴! Homebrew 패키지 관리자가 설정되었으므로 시스템에 Python 3을 계속 설치하십시오.

### 3 단계 : Python 설치

Homebrew가 설치를 마치면 터미널로 돌아가서 다음 명령을 실행하십시오.

``brew install python3 ''

최신 버전의 Python을 다운로드하여 설치합니다. Homebrew brew install 명령이 완료되면 Python 3을 시스템에 설치해야합니다.

터미널에서 Python에 액세스 할 수 있는지 테스트하여 모든 것이 올바르게되었는지 확인할 수 있습니다.

Terminal.app를 실행하여 터미널을 엽니 다.

``pip3 ''을 입력하고``Enter ''를 누르십시오.

Python의 "Pip"패키지 관리자에서 도움말을 볼 수 있습니다.

pip3을 실행하는 중 오류 메시지가 표시되면 Python 설치 단계를 다시 수행하여 작동중인 Python 설치가 있는지 확인하십시오.

모든 것이 잘되었다고 가정하면 명령 프롬프트 창에서 Pip의 출력을 보았습니다 ... 축하합니다!

방금 시스템에 Python을 설치했으며이 자습서의 다음 섹션을 계속 진행할 수 있습니다.

건배 : 100 :