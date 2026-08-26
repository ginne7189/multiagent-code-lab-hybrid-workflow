import json
import sys

from hybrid_lab.workflow import HybridWorkflow


if __name__ == "__main__":
    scenario = sys.argv[1] if len(sys.argv) > 1 else "normal"
    request = {
        "normal": "OTA 변경안의 문서, 위험, 시험 결과를 검토해줘",
        "failure": "OTA 변경 검토 증적 없음",
    }.get(scenario)
    if request is None:
        raise SystemExit("사용법: python3 main.py [normal|failure]")
    result = HybridWorkflow().run(request)
    print(json.dumps(result, ensure_ascii=False, indent=2))
