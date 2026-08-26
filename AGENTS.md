# Hybrid 코드 실습 규칙

- Router는 요청 종류만 결정합니다.
- 독립 Analyst는 서로의 결과를 참고하지 않습니다.
- 모든 Analyst는 같은 Result Contract를 반환합니다.
- Evaluator는 수정 이유를 반환하며 최대 2회까지만 반복합니다.
- 근거 충돌과 반복 한도 도달은 사람 확인으로 끝납니다.
