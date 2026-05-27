"""数据模型

题目输入、评测结果、问题标签的完整定义。
标签和严重程度分级严格来自飞书文档「题目测评标准-教研侧」。
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum


class Level(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"


class QuestionType(str, Enum):
    S2 = "S2"               # 词汇理解单选
    REVIEW_S1 = "REVIEW_S1" # 听音选义
    REVIEW_S2 = "REVIEW_S2" # 语境填空
    DRAG_SORT = "DRAG_SORT" # 中译英拖拽排序（B2+）
    S5 = "S5"               # 搭配配对
    REVIEW_S3 = "REVIEW_S3" # 跟读评分


class LearningMode(str, Enum):
    ENGLISH = "english"  # 英语学英语
    NATIVE = "native"    # 母语学英语


# ── 八维度 ──
DIMENSIONS = [
    "知识点匹配",
    "题型合规性",
    "语言正确性",
    "级别适配度",
    "选项设计",
    "题干清晰度",
    "与剧情/语境关联",
    "交互体验",
]


# ── 问题标签定义（原文逐字） ──
@dataclass
class ProblemTag:
    code: str        # 如 "O-3"
    category: str    # 大类原文（如"知识点问题-KP / Knowledge Point"）
    name: str        # 标签名
    definition: str  # 定义原文


PROBLEM_TAGS: list[ProblemTag] = [
    # KP - 知识点问题
    ProblemTag("KP-1", "知识点问题-KP / Knowledge Point", "知识点错配",
               "题目考察的知识点与标注不符"),
    ProblemTag("KP-2", "知识点问题-KP / Knowledge Point", "知识点缺失",
               "题目没有围绕任何有效知识点"),
    # T - 题型问题
    ProblemTag("T-1", "题型问题-T / Type", "题型不匹配",
               "题目形式不符合该题型规范"),
    ProblemTag("T-2", "题型问题-T / Type", "题型级别错误",
               "题型难度与目标级别不匹配（如A1出拼写填空）"),
    # L - 语言问题
    ProblemTag("L-1", "语言问题-L / Language", "语法错误",
               "题干或选项存在语法错误"),
    ProblemTag("L-2", "语言问题-L / Language", "拼写错误",
               "存在拼写错误"),
    ProblemTag("L-3", "语言问题-L / Language", "语义模糊",
               "题目意思不清晰，有歧义"),
    ProblemTag("L-4", "语言问题-L / Language", "表达不地道",
               "英文表达不符合母语习惯"),
    # D - 难度问题
    ProblemTag("D-1", "难度问题-D / Difficulty", "超纲词",
               "使用了超出目标级别的词汇"),
    ProblemTag("D-2", "难度问题-D / Difficulty", "句长超限",
               "句子长度超出级别允许范围"),
    ProblemTag("D-3", "难度问题-D / Difficulty", "语法过难",
               "使用了高级别语法结构（如B1题目出现虚拟语气）"),
    ProblemTag("D-4", "难度问题-D / Difficulty", "语法过易",
               "对于高级别来说太简单"),
    # O - 选项问题
    ProblemTag("O-1", "选项问题-O / Option", "答案错误",
               "标准答案本身错误"),
    ProblemTag("O-2", "选项问题-O / Option", "答案不唯一",
               "存在多个正确答案"),
    ProblemTag("O-3", "选项问题-O / Option", "干扰项无效",
               "干扰项太弱，明显错误或语义无关"),
    ProblemTag("O-4", "选项问题-O / Option", "干扰项荒谬",
               "干扰项不符合常识或逻辑"),
    # Q - 题干问题
    ProblemTag("Q-1", "题干问题-Q / Question", "题干不清晰",
               "用户看不懂题目要求"),
    ProblemTag("Q-2", "题干问题-Q / Question", "题干冗余",
               "包含多余信息，影响理解"),
    # C - 语境问题
    ProblemTag("C-1", "语境问题-C / Context", "语境不足",
               "缺少必要的上下文支撑答题"),
    # X - 交互/体验问题
    ProblemTag("X-1", "交互/体验问题-X / eXperience", "打断感强",
               "题目出现时机影响观看节奏"),
    ProblemTag("X-2", "交互/体验问题-X / eXperience", "反馈无效",
               "错误后反馈没有解释原因"),
]

PROBLEM_TAG_MAP: dict[str, ProblemTag] = {t.code: t for t in PROBLEM_TAGS}


# ── 题目输入 ──
@dataclass
class Question:
    """一道待评测的题目"""
    id: str
    level: Level
    type: QuestionType
    knowledge_point: str
    learning_mode: LearningMode = LearningMode.NATIVE

    stem: str = ""               # 题干
    options: list[str] = field(default_factory=list)  # 全部选项
    correct_answer: str = ""     # 正确答案
    source_script: str = ""      # 知识点来源台词
    sentence_length: int = 0     # 句子长度(词数)
    notes: str = ""              # 备注


# ── 评测结果 ──
@dataclass
class DimensionScore:
    dimension: str    # 维度名称
    score: int        # 0/1/2
    reason: str       # 评判理由


@dataclass
class TagWithSeverity:
    code: str         # 标签代码
    severity: str     # High / Medium / Low


@dataclass
class EvaluationResult:
    """单题的完整评测结果"""
    question: Question
    dimension_scores: list[DimensionScore] = field(default_factory=list)
    tags: list[TagWithSeverity] = field(default_factory=list)
    suggestions: str = ""

    @property
    def avg_score(self) -> float:
        if not self.dimension_scores:
            return 0.0
        total = sum(ds.score for ds in self.dimension_scores)
        return round(total / len(self.dimension_scores) * 8) / 8

    @property
    def is_usable(self) -> bool:
        return self.avg_score >= 1.0

    @property
    def is_satisfactory(self) -> bool:
        return self.avg_score >= 2.0


@dataclass
class EvaluationReport:
    """单次评测汇总"""
    results: list[EvaluationResult] = field(default_factory=list)
    batch_name: str = ""

    @property
    def total_questions(self) -> int:
        return len(self.results)

    @property
    def avg_score(self) -> float:
        if not self.results:
            return 0.0
        return round(sum(r.avg_score for r in self.results) / len(self.results) * 8) / 8

    @property
    def usable_rate(self) -> float:
        if not self.results:
            return 0.0
        return sum(1 for r in self.results if r.is_usable) / len(self.results)

    @property
    def satisfaction_rate(self) -> float:
        if not self.results:
            return 0.0
        return sum(1 for r in self.results if r.is_satisfactory) / len(self.results)

    def tag_frequency(self) -> dict[str, int]:
        freq: dict[str, int] = {}
        for r in self.results:
            for t in r.tags:
                freq[t.code] = freq.get(t.code, 0) + 1
        return freq

    def dimension_distribution(self) -> dict[str, dict[int, int]]:
        dist: dict[str, dict[int, int]] = {d: {0: 0, 1: 0, 2: 0} for d in DIMENSIONS}
        for r in self.results:
            for ds in r.dimension_scores:
                if ds.dimension in dist:
                    dist[ds.dimension][ds.score] += 1
        return dist
