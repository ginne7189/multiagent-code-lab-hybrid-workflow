from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass


@dataclass
class AnalysisResult:
    role: str
    finding: str
    evidence: str
    status: str
    next_action: str


class HybridWorkflow:
    analysts = ("document", "risk", "test")

    def route(self, request: str) -> str:
        if any(word in request for word in ("변경", "출시", "검토")):
            return "review"
        if any(word in request for word in ("문의", "질문")):
            return "support"
        return "needs_input"

    def analyze(self, role: str, request: str, revision: int) -> AnalysisResult:
        missing = "증적 없음" in request and role == "test"
        return AnalysisResult(
            role=role,
            finding=f"{role} 관점의 {revision + 1}차 결과",
            evidence="" if missing else f"sample://{role}/evidence-{revision + 1}",
            status="insufficient" if missing else "ready",
            next_action="증적 요청" if missing else "결과 통합",
        )

    def evaluate(self, results: list[AnalysisResult]) -> dict:
        missing = [result.role for result in results if not result.evidence]
        if missing:
            return {"verdict": "revise", "feedback": f"근거 누락 역할: {', '.join(missing)}"}
        return {"verdict": "pass", "feedback": "모든 역할의 근거가 확인됨"}

    def run_review(self, request: str, max_retries: int = 2) -> dict:
        trace = ["route=review"]
        for revision in range(max_retries + 1):
            with ThreadPoolExecutor(max_workers=len(self.analysts)) as pool:
                results = list(pool.map(lambda role: self.analyze(role, request, revision), self.analysts))
            trace.extend([f"parallel={result.role}:status={result.status}" for result in results])
            evaluation = self.evaluate(results)
            trace.append(f"evaluator={evaluation['verdict']}:revision={revision}")
            if evaluation["verdict"] == "pass":
                return {"route": "review", "results": [asdict(result) for result in results], "evaluation": evaluation, "status": "review_ready", "required_action": "human_review", "trace": trace}
        return {"route": "review", "results": [asdict(result) for result in results], "evaluation": evaluation, "status": "blocked", "required_action": "human_review", "trace": trace}

    def run(self, request: str) -> dict:
        route = self.route(request)
        if route == "review":
            return self.run_review(request)
        if route == "support":
            return {"route": route, "status": "draft_ready", "answer": "지원 답변 초안", "trace": ["route=support"]}
        return {"route": route, "status": "needs_input", "answer": "검토할 업무와 대상을 입력해 주세요.", "trace": ["route=needs_input"]}
