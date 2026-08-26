# Hybrid Workflow Code Lab

Routing, Parallelization, Result Contract, Evaluator 반복과 사람 확인을 하나의 실행 흐름으로 연결합니다.

```bash
make install
make run
make check
```

각 패턴이 어느 단계의 어떤 문제를 해결하는지 Trace에서 확인합니다.

## Harness 문서와 코드를 연결하는 순서

1. `AGENTS.md`: 공통 목표와 실행 경계
2. `knowledge/`: Hybrid 패턴 선택 이유
3. `roles/`: Router·Analyst·Evaluator 책임
4. `contracts/`: 패턴 사이에 전달되는 필수 값
5. `policies/`: 반복 한도와 사람 확인 조건
6. `src/`: 위 규칙을 실행하는 Python 코드
7. `tests/`: Routing·Contract·반복 한도 검증
