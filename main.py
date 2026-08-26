import json

from hybrid_lab.workflow import HybridWorkflow


if __name__ == "__main__":
    result = HybridWorkflow().run("OTA 변경안의 문서, 위험, 시험 결과를 검토해줘")
    print(json.dumps(result, ensure_ascii=False, indent=2))
