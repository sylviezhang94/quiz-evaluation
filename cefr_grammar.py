"""CEFR 语法级别对照表

每个级别列出该级别应掌握的语法点。
评测时若题目使用了高于目标级别的语法结构，应标注 D-3（语法过难）。
若题目语法远低于目标级别（如 C1 题只用一般现在时），可标注 D-4（语法过易）。

参考来源：Cambridge English Profile, British Council CEFR descriptors,
Common European Framework of Reference for Languages.
"""

from __future__ import annotations

GRAMMAR_BY_LEVEL: dict[str, list[str]] = {
    "A1": [
        "be 动词 (am/is/are) 的基本用法",
        "have got 表示拥有",
        "一般现在时 (I work, She works)",
        "现在进行时 (I am working) — 基本用法",
        "一般过去时 (be 动词: was/were)",
        "be going to 表示将来",
        "情态动词 can (能力), must (义务)",
        "祈使句 (Sit down, Don't go)",
        "There is / There are",
        "人称代词 (I, you, he, she, it, we, they)",
        "物主限定词 (my, your, his, her)",
        "基本冠词 a/an, the",
        "基本介词: in, on, at, to, from",
        "基本疑问句: Wh- 和 Yes/No",
        "基本连词: and, but, or",
        "名词复数 (regular -s)",
        "形容词位置 (a big house)",
        "副词: 频率 (always, sometimes, never) — 基本",
        "指示代词: this, that, these, those"
    ],
    "A2": [
        "一般现在时 vs 现在进行时 的对比使用",
        "一般过去时 (规则和不规则动词: worked, went)",
        "现在完成时 (经历: Have you ever...?)",
        "will 表示将来预测",
        "be going to vs will",
        "过去进行时 (I was working) — 基本",
        "形容词比较级和最高级 (-er, -est, more, most)",
        "情态动词 should (建议), might (可能), have to (必须)",
        "可数/不可数名词 (some, any, much, many, a lot of)",
        "数量词: a few, a little",
        "频率副词 (often, usually, sometimes, never) — 完整使用",
        "条件句: 零条件 (If you heat water, it boils)",
        "第一条件句 (If it rains, I will stay home)",
        "物主代词 (mine, yours, his, hers)",
        "'s 所有格",
        "动名词 after like/love/hate (I like swimming)",
        "时间介词: in, on, at 的完整用法",
        "方向介词: across, along, through",
        "不定代词: someone, anything, nowhere",
        "so / because 连接句子"
    ],
    "B1": [
        "现在完成时 (for/since, just/already/yet, 与一般过去时的对比)",
        "过去进行时 (When I arrived, he was cooking)",
        "used to 表示过去的习惯",
        "将来形式: will, going to, 现在进行时表将来",
        "情态动词: must / have to (义务), may / might (可能), can/could (能力/请求)",
        "第二条件句 (If I had money, I would travel)",
        "被动语态: 一般现在时和一般过去时 (It is made, It was built)",
        "关系从句（限定性）: who, which, that, where",
        "间接引语: 陈述句和疑问句 (He said that..., He asked if...)",
        "疑问尾句 (You like coffee, don't you?)",
        "so / such, too / enough",
        "动名词 vs 不定式 (stop doing vs stop to do, remember doing vs remember to do)",
        "形容词顺序 (a beautiful old wooden house)",
        "现在完成进行时 (I have been working) — 基本",
        "连词: although, however, unless, as long as",
        "情态动词完成式 (must have been, can't have gone) — 基本",
    ],
    "B2": [
        "现在完成进行时 (全场景使用)",
        "过去完成时 (When I arrived, he had already left)",
        "过去完成进行时 — 基本",
        "将来进行时 (I will be waiting)",
        "将来完成时 (By Friday, I will have finished)",
        "情态动词推测: must have, can't have, might have, should have (过去推测)",
        "第三条件句 (If I had known, I would have come)",
        "混合条件句 (If I had studied, I would be a doctor now)",
        "被动语态: 所有时态, 含情态动词被动",
        "关系从句（非限定性）: which, who — 带逗号用法",
        "间接引语: 时态后移 (He said he was coming)",
        "wish / if only 表示愿望和遗憾",
        "使役结构: have/get something done",
        "倒装: 否定副词开头 (Never have I seen... , Not only...) — 基本",
        "分词从句 (Walking home, I saw...; Having finished, he...)",
        "名词化 (the destruction of, the arrival of)",
        "动名词 vs 不定式: 完整辨析",
        "短语动词: 大量掌握",
        "话语标记语: however, therefore, furthermore, on the other hand",
        "强调结构: It is... that/who (分裂句)",
        "虚拟语气: wish, if only, it's time",
        "将来完成进行时 — 了解",
    ],
    "C1": [
        "所有时态的流畅运用, 包括进行体和完成体的精确切换",
        "情态动词细微辨析: needn't have vs didn't need to, should have vs ought to have",
        "所有条件句: 显性和隐性条件 (Had I known..., Were it not for...)",
        "被动语态: 报告动词被动 (It is said that..., He is believed to be...)",
        "倒装句: 全范围 (Not only..., Rarely..., Only when..., Should you...)",
        "分裂句和假分裂句 (What I need is..., It was John who...)",
        "分词从句: 完整掌握",
        "名词化: 高级运用",
        "虚拟语气: 完整掌握 (包括 should + 动词原形, 正式文体中)",
        "间接引语: 完整掌握, 含复杂转述动词",
        "前置与后置修饰语 (a crucially important decision, the person concerned)",
        "省略与替代 (I think so, He can if he wants to)",
        "复杂介词: notwithstanding, in accordance with, by means of",
        "语篇标记语: 全范围准确使用",
        "长难句的构建和控制",
        "正式与非正式语体的语法切换",
        "无动词从句 (Though tired, he continued)",
        "比较结构: 高级 (the more..., the more...; not so much... as...)",
    ],
    "C2": [
        "所有语法结构达到母语级精确度",
        "语法选择带有风格意识 (正式/非正式, 口语/书面语, 学术/文学)",
        "微妙情态差异: 能够根据语境选择最精确的表达",
        "修辞性语法: 排比、对比、强调等修辞手法的语法实现",
        "多层级嵌套从句: 流畅准确",
        "时态和体的高级衔接: 叙事中的时间线精确控制",
        "语域切换: 可根据交际场景自如切换语法风格",
        "任何语法结构的直觉性正确运用",
        "能够识别并修正自身和他人语法中的细微偏差",
    ],
}

# ── 判断语法是否符合级别 ──
LEVEL_ORDER = {'A1': 0, 'A2': 1, 'B1': 2, 'B2': 3, 'C1': 4, 'C2': 5}


def get_grammar_for_level(level: str) -> list[str]:
    """获取某个级别及以下应该掌握的所有语法点"""
    result = []
    target_idx = LEVEL_ORDER.get(level, -1)
    for lvl, idx in LEVEL_ORDER.items():
        if idx <= target_idx:
            result.extend(GRAMMAR_BY_LEVEL.get(lvl, []))
    return result


def get_grammar_added_at_level(level: str) -> list[str]:
    """获取某个级别新增的语法点（不含低级别已掌握的）"""
    return GRAMMAR_BY_LEVEL.get(level, [])


def build_grammar_prompt_for_level(level: str) -> str:
    """生成给 LLM 的语法参考 prompt 片段
    
    列出该级别应掌握的语法点 + 不应出现的超纲语法
    """
    target_idx = LEVEL_ORDER.get(level, 1)
    
    lines = [f"### {level} 级别语法要求", ""]
    
    # 该级别应掌握的语法
    lines.append("**该级别应掌握的语法点：**")
    for lvl, idx in LEVEL_ORDER.items():
        if idx <= target_idx:
            grammars = GRAMMAR_BY_LEVEL.get(lvl, [])
            if grammars:
                lines.append(f"\n{lvl} 级别基础：")
                for g in grammars[:5]:  # 每级别只列前5个，避免prompt过长
                    lines.append(f"  - {g}")
    
    # 超纲语法警告
    next_idx = target_idx + 1
    lines.append(f"\n**以下语法结构属于 {level} 超纲，出现应标 D-3：**")
    for lvl, idx in LEVEL_ORDER.items():
        if idx > target_idx:
            grammars = GRAMMAR_BY_LEVEL.get(lvl, [])
            if grammars:
                lines.append(f"\n{lvl} 级别语法（超纲）：")
                for g in grammars[:3]:  # 每个超纲级别列前3个
                    lines.append(f"  - {g}")
    
    return "\n".join(lines)
