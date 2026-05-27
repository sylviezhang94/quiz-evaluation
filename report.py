"""评测报告生成器

控制台报告 + CSV 输出。
"""

from __future__ import annotations
import csv
import io

from models import (
    EvaluationResult, EvaluationReport, DIMENSIONS, PROBLEM_TAGS, TagWithSeverity,
)


def _tag_name(code: str) -> str:
    for t in PROBLEM_TAGS:
        if t.code == code:
            return t.name
    return code


def _score_label(s: int) -> str:
    return {0: "0分(有瑕疵)", 1: "1分(可用)", 2: "2分(满意)"}.get(s, "?")


def generate_csv(report: EvaluationReport) -> str:
    """生成评测结果CSV，列顺序与文档「单次测评表格列说明」一致"""
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["题目ID", "级别", "题型", "知识点", "绝对分"]
                     + DIMENSIONS
                     + ["问题标签", "严重程度", "修改建议", "备注"])

    for r in report.results:
        q = r.question
        dim_scores = {ds.dimension: ds.score for ds in r.dimension_scores}
        dim_cols = [dim_scores.get(d, "-") for d in DIMENSIONS]

        tag_str = ", ".join(f"{t.code} {_tag_name(t.code)}" for t in r.tags) if r.tags else "—"
        sev_str = "/".join(t.severity for t in r.tags) if r.tags else "—"

        writer.writerow([
            q.id, q.level.value, q.type.value, q.knowledge_point,
            f"{r.avg_score:.3f}",
        ] + dim_cols + [tag_str, sev_str, r.suggestions, q.notes])

    return output.getvalue()


def _rate_pct(v: float) -> str:
    return f"{v * 100:.0f}%"


def print_report(report: EvaluationReport) -> str:
    """打印评测报告"""
    out = io.StringIO()

    out.write("=" * 60 + "\n")
    out.write(f"  题目质量评测报告 - {report.batch_name or '(未命名)'}\n")
    out.write("=" * 60 + "\n\n")

    # 总体结果
    out.write("【总体结果】\n")
    out.write(f"  评测题目数: {report.total_questions}\n")
    out.write(f"  平均绝对分: {report.avg_score:.3f}\n")
    out.write(f"  可用率 (≥1分): {_rate_pct(report.usable_rate)}\n")
    out.write(f"  满意率 (=2分): {_rate_pct(report.satisfaction_rate)}\n")

    if report.usable_rate >= 0.90 and report.satisfaction_rate >= 0.70:
        out.write("  质量评价: 达标（可用率≥90% 且 满意率≥70%）\n")
    elif report.usable_rate >= 0.80:
        out.write("  质量评价: 待优化\n")
    else:
        out.write("  质量评价: 不合格\n")
    out.write("\n")

    # 各维度表现
    out.write("【各维度表现】\n")
    dist = report.dimension_distribution()
    for dim in DIMENSIONS:
        d = dist.get(dim, {0: 0, 1: 0, 2: 0})
        total = d[0] + d[1] + d[2] or 1
        avg = (d[0] * 0 + d[1] * 1 + d[2] * 2) / total
        bar = "█" * int(avg * 5) + "░" * (10 - int(avg * 5))
        out.write(f"  {dim:<8s} [{bar}] {avg:.2f}  (2:{d.get(2,0)}, 1:{d.get(1,0)}, 0:{d.get(0,0)})\n")
    out.write("\n")

    # 每题详情
    out.write("【每题详情】\n")
    for r in report.results:
        q = r.question
        out.write(f"\n  [{q.id}] {q.type.value} | {q.level.value} | {q.knowledge_point} | 均分: {r.avg_score:.3f}\n")
        for ds in r.dimension_scores:
            flag = "✓" if ds.score == 2 else ("△" if ds.score == 1 else "✗")
            out.write(f"    {flag} {ds.dimension}: {_score_label(ds.score)} - {ds.reason}\n")
        if r.tags:
            tags_str = ", ".join(f"{t.code} {_tag_name(t.code)} [{t.severity}]" for t in r.tags)
            out.write(f"    问题标签: {tags_str}\n")
        if r.suggestions:
            out.write(f"    修改建议: {r.suggestions}\n")

    # 高频问题标签
    out.write("\n【高频问题标签】\n")
    freq = report.tag_frequency()
    if freq:
        for code, count in sorted(freq.items(), key=lambda x: -x[1]):
            out.write(f"  {code} {_tag_name(code)}: {count}次\n")
    else:
        out.write("  (无问题标签)\n")

    out.write("\n" + "=" * 60 + "\n")

    result = out.getvalue()
    print(result)
    return result


def generate_report(results: list[EvaluationResult], batch_name: str = "") -> EvaluationReport:
    return EvaluationReport(results=results, batch_name=batch_name)
