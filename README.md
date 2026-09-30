# digital-news

주제만 입력하면 같은 조사 기준·구성·문체·분량으로 디지털뉴스 초안을 만들도록 하는
작업 규격 저장소다. 완성 대본과 건별 취재 자료는 이 저장소에 올리지 않는다.

## 목적과 범위

한국어 시사 주제를 최신 자료로 조사해 2분 30초~3분짜리 디지털뉴스 초안으로 만드는
재사용 규격을 배포한다. 개별 기사와 건별 취재 자료는 범위에 포함하지 않는다.

## 소속과 관계

`workCodex/projects/digital-news`가 로컬 정본이며 GitHub의
`ByeongseonReport/digital-news`가 작업자 배포용 원격 저장소다.

## 정본 입력·산출물

입력은 주제, 선택적인 취재 각도와 필수 포함 사항이다. 산출물은 조사된 낭독 초안,
사실표와 쓰지 않은 사실이다. 산출물은 이 규격 저장소 밖에서 관리한다.

## 포함된 정본

- `SKILL.md`: 주제를 받은 뒤 조사하고 초안을 만드는 전체 절차
- `style-guide.md`: 2분 30초~3분 구성과 문체 규격
- `template.md`: 초안 출력 형식
- `research/klab-issue-one-year-analysis.md`: 규격을 만든 분석 근거
- `scripts/check_script.py`: 대본 자수와 예상 낭독 시간 검사

크랩의 개별 문장이나 고정 말버릇을 복제하지 않는다. 질문 중심 전개, 구어적 연결,
구체적 비교, 반론을 거치는 구조만 제작 원리로 사용한다.

## 작업자 설치

Codex가 자동으로 찾을 수 있도록 개인 스킬 폴더에 한 번 복제한다.

```powershell
git clone https://github.com/ByeongseonReport/digital-news.git "$env:USERPROFILE\.codex\skills\digital-news"
```

이후에는 아래 명령만 실행하면 최신 규격으로 갱신된다.

```powershell
git -C "$env:USERPROFILE\.codex\skills\digital-news" pull --ff-only origin main
```

설치 뒤에는 새 대화에서 `디지털뉴스 초안: [주제]`처럼 요청한다. 주제만으로 시작할 수
있으며, 취재 각도나 반드시 넣을 내용이 있으면 함께 적는다.

## 실행·재개

에이전트는 `SKILL.md`를 진입점으로 사용한다. 작업자는 위 pull 명령으로 규격을
갱신한 뒤 새 대화에서 주제를 입력한다.

## 저장소 운영

- 정본 브랜치는 `main`이다.
- 규격 수정과 원격 저장소 push는 소유자가 담당한다.
- 완성 대본, 다운로드한 자료, 취재 메모는 `artifacts/`, `drafts/`, `sources/`에 둘 수
  있지만 Git에는 포함되지 않는다.
- 대본 파일을 검사할 때는 `python scripts/check_script.py <대본.md>`를 실행한다.

## 완료 조건

주제만 입력한 요청에서 최신 시점과 후속 공방을 반영한 150~180초 초안, 사실표와
제외 사실이 생성되고 길이 검사를 통과하면 한 건의 작업이 완료된다.

## 보존 조건

`SKILL.md`, 제작 규격, 템플릿, 분석 근거와 검사 도구는 장기 보존한다. 개별 대본과
건별 자료는 이 저장소에서 보존하지 않는다.
