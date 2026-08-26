# 코드 실습 C-2 — 강사와 함께 Hybrid Workflow 실행하기

이 저장소는 공통 실습용 완성 코드입니다. 강사가 정상 요청과 실패 요청을 실행하고, 수강생은 Routing·Parallelization·Evaluator-Optimizer가 어느 순서로 연결되는지 확인합니다.

## 같이 실행

```bash
make run
make check
```

## 결과를 읽는 순서

1. `route()`가 요청을 어느 처리 경로로 보냈는지 Trace에서 확인합니다.
2. `run_review()`에서 세 Analyst가 같은 입력을 독립적으로 처리한 결과를 비교합니다.
3. Result Contract에서 세 결과에 공통으로 들어가는 필드를 찾습니다.
4. Evaluator의 `pass` 또는 `revise` 판정과 이유를 확인합니다.
5. `증적 없음` 요청이 반복 한도에 도달한 뒤 `human_review`로 끝나는지 확인합니다.
6. `make check`의 세 테스트가 통과하는 것을 확인합니다.

새 Route나 Analyst를 추가하는 활동은 개인 프로젝트에서 진행합니다.
