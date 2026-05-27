"""CEFR 级别 × 题型约束规则

从"出题系统参考手册 §3 CEFR 级别级联总表"提取。
作为 LLM 评判时的参考标准。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from models import Level, QuestionType, LearningMode


@dataclass
class LevelRule:
    """一个级别 × 题型 × 学习模式的约束规则"""
    level: Level
    question_type: QuestionType
    learning_mode: LearningMode
    description: str = ""  # 对该规则的自然语言描述（供 LLM 阅读）

    # 通用
    option_count: int = 4
    option_form: str = ""       # 选项形式（中文描述）
    option_language: str = ""   # 选项语言
    stem_language: str = ""     # 题干语言
    max_stem_chars: int = 60    # 题干最大字符数

    # 干扰项
    distractor_strategy: str = ""

    # 句子
    min_words: int = 0
    max_words: int = 0
    sentence_type: str = ""

    # REVIEW_S2 专用
    fill_mode: str = ""         # 选词/拼写/拖拽排序/不出现
    candidate_count: int = 0
    has_interference: bool = False

    # S5 专用
    pair_count: int = 4
    pair_mode: str = ""         # 英→图片 / 英→中 / 英→英
    diff_level: str = ""        # 区分难度描述

    # REVIEW_S3 专用
    reading_type: str = ""      # 单词/短句/带情感的句子/复杂句/角色对话
    scoring_dims: list[str] = field(default_factory=list)
    pass_line: int = 0


def _text(rule: LevelRule) -> str:
    """生成给 LLM 阅读的规则描述"""
    parts = [f"级别: {rule.level.value}, 题型: {rule.question_type.value}, 学习模式: {rule.learning_mode.value}"]

    if rule.option_form:
        parts.append(f"选项形式: {rule.option_form}")
    if rule.option_language:
        parts.append(f"选项语言: {rule.option_language}")
    if rule.option_count:
        parts.append(f"选项数量: {rule.option_count}个")
    if rule.stem_language:
        parts.append(f"题干语言: {rule.stem_language}")
    if rule.max_stem_chars:
        parts.append(f"题干最大字符数: {rule.max_stem_chars}")
    if rule.distractor_strategy:
        parts.append(f"干扰项策略: {rule.distractor_strategy}")

    if rule.fill_mode:
        parts.append(f"填空模式: {rule.fill_mode}")
        if rule.candidate_count:
            parts.append(f"候选词数量: {rule.candidate_count}")
        if rule.has_interference:
            parts.append("拖拽排序含干扰项")
    if rule.min_words or rule.max_words:
        parts.append(f"句子长度范围: {rule.min_words}-{rule.max_words}词 ({rule.sentence_type})")

    if rule.pair_mode:
        parts.append(f"配对方式: {rule.pair_mode}, 配对数: {rule.pair_count}对")
    if rule.diff_level:
        parts.append(f"区分难度: {rule.diff_level}")

    if rule.reading_type:
        parts.append(f"朗读内容: {rule.reading_type}, 及格线: {rule.pass_line}分")
    if rule.scoring_dims:
        parts.append(f"评分维度: {'+'.join(rule.scoring_dims)}")

    return " | ".join(parts)


# ════════════════════════════════════════════
# S2 - 词汇理解单选
# ════════════════════════════════════════════
S2 = [
    LevelRule(Level.A1, QuestionType.S2, LearningMode.ENGLISH,
        description="A1英语学英语：选项用四张图片，不同类别物体视觉区别明显，题干英文≤60字符",
        option_form="四张图片", option_language="英文", stem_language="英文", max_stem_chars=60,
        distractor_strategy="不同类别的物体，视觉区别明显"),
    LevelRule(Level.A1, QuestionType.S2, LearningMode.NATIVE,
        description="A1母语学英语：选项用四张图片，不同类别物体视觉区别明显，题干母语≤60字符",
        option_form="四张图片", option_language="用户母语", stem_language="用户母语", max_stem_chars=60,
        distractor_strategy="不同类别的物体，视觉区别明显"),
    LevelRule(Level.A2, QuestionType.S2, LearningMode.ENGLISH,
        description="A2英语学英语：选项用四个英文定义或近义词/四张图片，同一语义范畴近义定义",
        option_form="四个英文定义或近义词/四张图片", option_language="英文", stem_language="英文",
        distractor_strategy="同一语义范畴的近义定义"),
    LevelRule(Level.A2, QuestionType.S2, LearningMode.NATIVE,
        description="A2母语学英语：选项用四个母语释义/四张图片，同一词性的母语迁移错误",
        option_form="四个母语释义/四张图片", option_language="用户母语", stem_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误（如把job翻成'旅行'）"),
    LevelRule(Level.B1, QuestionType.S2, LearningMode.ENGLISH,
        description="B1英语学英语：四个英文定义或近义词，同一语义范畴近义定义，全英文",
        option_form="四个英文定义或近义词", option_language="英文", stem_language="英文",
        distractor_strategy="同一语义范畴的近义定义"),
    LevelRule(Level.B1, QuestionType.S2, LearningMode.NATIVE,
        description="B1母语学英语：四个母语释义，同一词性的母语迁移错误",
        option_form="四个母语释义", option_language="用户母语", stem_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误（如把job翻成'旅行'）"),
    LevelRule(Level.B2, QuestionType.S2, LearningMode.ENGLISH,
        description="B2英语学英语：四个英文定义或近义词，全英文，定义精细",
        option_form="四个英文定义或近义词", option_language="英文", stem_language="英文",
        distractor_strategy="同一语义范畴的近义定义"),
    LevelRule(Level.B2, QuestionType.S2, LearningMode.NATIVE,
        description="B2母语学英语：四个母语释义，同一词性的母语迁移错误",
        option_form="四个母语释义", option_language="用户母语", stem_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误"),
    LevelRule(Level.C1, QuestionType.S2, LearningMode.ENGLISH,
        description="C1英语学英语：四个英文定义或近义词，需要辨别微妙的语义差别",
        option_form="四个英文定义或近义词", option_language="英文", stem_language="英文",
        distractor_strategy="同一语义范畴的近义定义，需要辨别微妙语义差别"),
    LevelRule(Level.C1, QuestionType.S2, LearningMode.NATIVE,
        description="C1母语学英语：四个母语释义",
        option_form="四个母语释义", option_language="用户母语", stem_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误"),
    LevelRule(Level.C2, QuestionType.S2, LearningMode.ENGLISH,
        description="C2英语学英语：四个近义句/隐含含义，考察字面理解vs真实意图",
        option_form="四个近义句/隐含含义", option_language="英文", stem_language="英文",
        distractor_strategy="字面理解 vs 说话者的真实意图"),
    LevelRule(Level.C2, QuestionType.S2, LearningMode.NATIVE,
        description="C2母语学英语：四个母语释义",
        option_form="四个母语释义", option_language="用户母语", stem_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误"),
]

# ════════════════════════════════════════════
# REVIEW_S1 - 听音选义
# ════════════════════════════════════════════
REVIEW_S1 = [
    LevelRule(Level.A1, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="四张图片", option_language="英文",
        distractor_strategy="不同类别物体，视觉区别明显"),
    LevelRule(Level.A1, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四张图片", option_language="用户母语",
        distractor_strategy="不同类别物体，视觉区别明显"),
    LevelRule(Level.A2, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="四个英文单词", option_language="英文",
        distractor_strategy="读音相近的英语词（如job→job/cob/Bob/joke）"),
    LevelRule(Level.A2, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四个英文单词", option_language="用户母语",
        distractor_strategy="读音相近的英语词"),
    LevelRule(Level.B1, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="拼写填空", option_count=1, option_language="英文",
        distractor_strategy="—"),
    LevelRule(Level.B1, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四个母语释义", option_language="用户母语",
        distractor_strategy="同一词性的母语迁移错误"),
    LevelRule(Level.B2, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="四个英文同义词或释义（≤10词）", option_language="英文",
        distractor_strategy="同一语义范畴的近义定义"),
    LevelRule(Level.B2, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四个英文同义词或释义（≤10词）", option_language="用户母语",
        distractor_strategy="同一语义范畴的近义定义"),
    LevelRule(Level.C1, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="四个句子（≤22词）", option_language="英文",
        distractor_strategy="英文句子的同义句转换"),
    LevelRule(Level.C1, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四个句子（≤22词）", option_language="用户母语",
        distractor_strategy="英文句子的同义句转换"),
    LevelRule(Level.C2, QuestionType.REVIEW_S1, LearningMode.ENGLISH,
        option_form="四个近义句/隐含含义", option_language="英文",
        distractor_strategy="字面理解 vs 说话者的真实意图"),
    LevelRule(Level.C2, QuestionType.REVIEW_S1, LearningMode.NATIVE,
        option_form="四个近义句/隐含含义", option_language="用户母语",
        distractor_strategy="字面理解 vs 说话者的真实意图"),
]

# ════════════════════════════════════════════
# REVIEW_S2 - 语境填空 / DRAG_SORT - 中译英拖拽
# ════════════════════════════════════════════
REVIEW_S2 = [
    LevelRule(Level.A1, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="不出现",
        description="A1级别不出现语境填空/拖拽排序题"),
    LevelRule(Level.A1, QuestionType.REVIEW_S2, LearningMode.NATIVE,
        fill_mode="不出现",
        description="A1级别不出现语境填空/拖拽排序题"),
    # A2
    LevelRule(Level.A2, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="选词", candidate_count=4, min_words=5, max_words=8,
        sentence_type="短句", option_language="英文",
        description="A2英语学英语：点击选词填入，4个候选英文单词，短句5-8词"),
    LevelRule(Level.A2, QuestionType.REVIEW_S2, LearningMode.NATIVE,
        fill_mode="选词", candidate_count=4, min_words=5, max_words=8,
        sentence_type="短句", option_language="英文",
        description="A2母语学英语：点击选词填入，4个候选英文单词，短句5-8词"),
    # B1
    LevelRule(Level.B1, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="选词", candidate_count=4, min_words=8, max_words=10,
        sentence_type="简单句", option_language="英文",
        description="B1英语学英语：点击选词填入，4个候选词，简单句8-10词"),
    LevelRule(Level.B1, QuestionType.REVIEW_S2, LearningMode.NATIVE,
        fill_mode="选词", candidate_count=4, min_words=8, max_words=10,
        sentence_type="简单句", option_language="英文",
        description="B1母语学英语：点击选词填入，4个候选词，简单句8-10词"),
    # B2
    LevelRule(Level.B2, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="拼写", min_words=6, max_words=10, sentence_type="日常复合句",
        description="B2英语学英语：拼写填空，日常复合句6-10词"),
    LevelRule(Level.B2, QuestionType.DRAG_SORT, LearningMode.NATIVE,
        fill_mode="拖拽排序", min_words=6, max_words=10, sentence_type="日常复合句",
        has_interference=True,
        description="B2母语学英语：中译英拖拽排序，日常复合句6-10词，有干扰项"),
    # C1
    LevelRule(Level.C1, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="拼写", min_words=12, max_words=15, sentence_type="复杂句",
        description="C1英语学英语：拼写填空，复杂句12-15词"),
    LevelRule(Level.C1, QuestionType.DRAG_SORT, LearningMode.NATIVE,
        fill_mode="拖拽排序", min_words=12, max_words=15, sentence_type="复杂句",
        has_interference=True,
        description="C1母语学英语：中译英拖拽排序，复杂句12-15词，有干扰项"),
    # C2
    LevelRule(Level.C2, QuestionType.REVIEW_S2, LearningMode.ENGLISH,
        fill_mode="拼写", min_words=15, max_words=20, sentence_type="复杂结构句",
        description="C2英语学英语：拼写填空，复杂结构句15-20词"),
    LevelRule(Level.C2, QuestionType.DRAG_SORT, LearningMode.NATIVE,
        fill_mode="拖拽排序", min_words=15, max_words=20, sentence_type="复杂结构句",
        has_interference=True,
        description="C2母语学英语：中译英拖拽排序，复杂结构句15-20词，有干扰项"),
]

# ════════════════════════════════════════════
# S5 - 搭配配对
# ════════════════════════════════════════════
S5 = [
    LevelRule(Level.A1, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→图片", pair_count=4, diff_level="明显的错误搭配",
        description="A1：英文词→图片配对，4对，明显错误搭配"),
    LevelRule(Level.A1, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→图片", pair_count=4, diff_level="明显的错误搭配",
        description="A1：英文词→图片配对，4对，明显错误搭配"),
    LevelRule(Level.A2, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→图片", pair_count=4, diff_level="明显的错误搭配",
        description="A2：英文词→图片配对，4对"),
    LevelRule(Level.A2, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→图片", pair_count=4, diff_level="明显的错误搭配",
        description="A2：英文词→图片配对，4对"),
    LevelRule(Level.B1, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→英", pair_count=4, diff_level="接近正确但有差别的搭配",
        description="B1英语学英语：英文词→英文定义/同义词配对，4对，接近正确但有差别"),
    LevelRule(Level.B1, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→中", pair_count=4, diff_level="接近正确但有差别的搭配",
        description="B1母语学英语：英文词→中文含义配对，4对"),
    LevelRule(Level.B2, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→英", pair_count=4, diff_level="母语者能察觉的微妙错误",
        description="B2英语学英语：英文词→英文定义配对，4对，微妙错误"),
    LevelRule(Level.B2, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→中", pair_count=4, diff_level="母语者能察觉的微妙错误",
        description="B2母语学英语：英文词→中文含义配对，4对"),
    LevelRule(Level.C1, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→英", pair_count=4, diff_level="语域/正式度差异",
        description="C1英语学英语：英文词→高级英文定义，4对，语域/正式度差异"),
    LevelRule(Level.C1, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→中", pair_count=4, diff_level="语域/正式度差异"),
    LevelRule(Level.C2, QuestionType.S5, LearningMode.ENGLISH,
        pair_mode="英→英", pair_count=4, diff_level="语域/内涵/语用差异",
        description="C2英语学英语：英文词→精准英文定义，4对，语域/内涵/语用差异"),
    LevelRule(Level.C2, QuestionType.S5, LearningMode.NATIVE,
        pair_mode="英→中", pair_count=4, diff_level="语域/内涵/语用差异"),
]

# ════════════════════════════════════════════
# REVIEW_S3 - 跟读评分
# ════════════════════════════════════════════
REVIEW_S3 = [
    LevelRule(Level.A1, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="单词", scoring_dims=["发音准确度"], pass_line=70,
        description="A1：朗读单词，评发音准确度，及格线70分"),
    LevelRule(Level.A1, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="单词", scoring_dims=["发音准确度"], pass_line=70),
    LevelRule(Level.A2, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="单词", scoring_dims=["发音准确度", "完整度"], pass_line=75,
        description="A2：朗读单词，评发音准确度+完整度，及格线75分"),
    LevelRule(Level.A2, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="单词", scoring_dims=["发音准确度", "完整度"], pass_line=75),
    LevelRule(Level.B1, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="单词", scoring_dims=["发音准确度", "流利度"], pass_line=80,
        description="B1：朗读单词/短句，评发音准确度+流利度，及格线80分"),
    LevelRule(Level.B1, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="单词", scoring_dims=["发音准确度", "流利度"], pass_line=80),
    LevelRule(Level.B2, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="带情感的句子", scoring_dims=["发音准确度", "流利度", "情感表达"], pass_line=85,
        description="B2：朗读带情感句子，评发音+流利+情感，及格线85分"),
    LevelRule(Level.B2, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="带情感的句子", scoring_dims=["发音准确度", "流利度", "情感表达"], pass_line=85),
    LevelRule(Level.C1, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="复杂句", scoring_dims=["发音准确度", "流利度", "语调"], pass_line=90,
        description="C1：朗读复杂句，评发音+流利+语调，及格线90分"),
    LevelRule(Level.C1, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="复杂句", scoring_dims=["发音准确度", "流利度", "语调"], pass_line=90),
    LevelRule(Level.C2, QuestionType.REVIEW_S3, LearningMode.ENGLISH,
        reading_type="角色对话", scoring_dims=["发音准确度", "流利度", "完整度", "语调", "情感表达"], pass_line=95,
        description="C2：朗读角色对话，五项综合评分，及格线95分"),
    LevelRule(Level.C2, QuestionType.REVIEW_S3, LearningMode.NATIVE,
        reading_type="角色对话", scoring_dims=["发音准确度", "流利度", "完整度", "语调", "情感表达"], pass_line=95),
]

# ── 索引 ──
_ALL_RULES: list[LevelRule] = S2 + REVIEW_S1 + REVIEW_S2 + S5 + REVIEW_S3


def get_rule(level: Level, question_type: QuestionType, learning_mode: LearningMode) -> LevelRule | None:
    """查询指定组合的约束规则"""
    for r in _ALL_RULES:
        if r.level == level and r.question_type == question_type and r.learning_mode == learning_mode:
            return r
    return None


def get_rule_text(level: Level, question_type: QuestionType, learning_mode: LearningMode) -> str:
    """返回规则的 LLM 可读文本，未找到则返回提示"""
    r = get_rule(level, question_type, learning_mode)
    if r is None:
        return f"未找到 {level.value} × {question_type.value} × {learning_mode.value} 的规则"
    lines = [f"【{level.value} × {question_type.value} × {learning_mode.value} 约束规则】"]
    if r.description:
        lines.append(r.description)
    else:
        lines.append(_text(r))

    # 详细列表
    if r.option_form:
        lines.append(f"- 选项形式: {r.option_form}")
    if r.option_language:
        lines.append(f"- 选项语言: {r.option_language}")
    if r.option_count and r.question_type not in (QuestionType.REVIEW_S3,):
        lines.append(f"- 选项数量: {r.option_count}个")
    if r.stem_language:
        lines.append(f"- 题干语言: {r.stem_language}")
    if r.max_stem_chars:
        lines.append(f"- 题干上限: {r.max_stem_chars}字符")
    if r.distractor_strategy:
        lines.append(f"- 干扰项策略: {r.distractor_strategy}")
    if r.fill_mode:
        lines.append(f"- 填空/排序模式: {r.fill_mode}")
        if r.candidate_count:
            lines.append(f"- 候选词数量: {r.candidate_count}")
        if r.has_interference:
            lines.append(f"- 含干扰项: 是")
    if r.min_words or r.max_words:
        lines.append(f"- 句子长度: {r.min_words}-{r.max_words}词 ({r.sentence_type})")
    if r.pair_mode:
        lines.append(f"- 配对模式: {r.pair_mode}, {r.pair_count}对")
        if r.diff_level:
            lines.append(f"- 区分难度: {r.diff_level}")
    if r.reading_type:
        lines.append(f"- 朗读内容类型: {r.reading_type}")
    if r.scoring_dims:
        lines.append(f"- 评分维度: {', '.join(r.scoring_dims)}")
    if r.pass_line:
        lines.append(f"- 及格线: {r.pass_line}分")

    return "\n".join(lines)
