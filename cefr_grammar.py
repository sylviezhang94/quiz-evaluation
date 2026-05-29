"""CEFR 语法级别对照表（合并版）

融合两份来源：
1. 飞书文档「分级改写语法标准（A1-C2）」— 时态/从句/语态系统 + 基础语言特征
2. Cambridge English Profile / British Council — 情态动词/虚拟语气/条件句/语体等补充

评测时若题目使用了高于目标级别的语法结构，标注 D-3（语法过难）。
若题目语法远低于目标级别，标注 D-4（语法过易）。
"""

from __future__ import annotations

# ════════════════════════════════════════════
# 核心语法表格：每级可用 / 不可用的语法结构
# ════════════════════════════════════════════

GRAMMAR_TABLE: dict[str, dict[str, list[str]]] = {
    "A1": {
        "available": [
            # 时态
            "一般现在时",
            "现在进行时（此刻正在发生）",
            "一般过去时（be动词was/were + 少量规则动词）",
            "一般将来时（will, be going to）",
            # 从句
            "无从句，全部为简单句",
            # 语态
            "仅主动语态",
            # 情态动词
            "can（能力）",
            "must（义务/必要性）",
            # 句子结构
            "简单句为主，单句5-7词",
            "There is / There are",
            "祈使句",
            "基本疑问句（Wh- / Yes-No）",
            # 词法
            "基本冠词 a/an, the",
            "名词复数 (regular -s)",
            "人称代词和物主限定词",
            "基本介词: in, on, at, to, from",
            "连词: and, but, or",
            "频率副词: always, sometimes, never（基本）",
        ],
        "unavailable": [
            "现在完成时及任何完成体",
            "任何从句",
            "被动语态",
            "条件句",
            "间接引语",
            "比较级和最高级",
            "虚拟语气",
            "任何倒装结构",
        ],
    },
    "A2": {
        "available": [
            # 时态
            "一般现在时 vs 现在进行时的对比",
            "一般过去时（规则和不规则动词）",
            "现在完成时（经历: Have you ever...?）",
            "will vs be going to",
            "过去进行时（基本: I was working）",
            # 从句
            "简单 that 宾语从句（I think that...）",
            "无定语/状语从句",
            # 语态
            "仅主动语态",
            # 情态动词
            "should（建议）",
            "might（可能）",
            "have to（必须）",
            "can/could（能力/请求）",
            # 句子结构
            "短句为主，单句5-12词",
            "零条件句（If you heat water, it boils）",
            "第一条件句（If it rains, I will stay）",
            "比较级和最高级 (-er, -est, more, most)",
            "动名词 after like/love/hate（I like swimming）",
            # 词法
            "可数/不可数名词, some/any/much/many",
            "数量词: a few, a little",
            "物主代词: mine, yours",
            "'s 所有格",
            "频率副词完整使用",
            "不定代词: someone, anything, nowhere",
            "连词: so, because",
        ],
        "unavailable": [
            "现在完成进行时",
            "过去完成时",
            "被动语态",
            "第二/第三条件句",
            "关系从句（定语从句）",
            "间接引语",
            "虚拟语气（wish等）",
            "倒装句",
            "used to（属于B1）",
        ],
    },
    "B1": {
        "available": [
            # 时态
            "现在完成时（for/since, just/already/yet, 与一般过去时对比）",
            "现在完成进行时（基本: I have been working）",
            "过去进行时（与一般过去时搭配: When I arrived, he was cooking）",
            "过去完成时（基本: the past before past）",
            "将来进行时（基本: 将来某时正在发生）",
            "used to（过去的习惯）",
            "将来形式的选择: will vs going to vs 现在进行时表将来",
            # 从句
            "定语从句（限定性）: who, which, that, where",
            "时间状语从句: when, while, before, after",
            "原因状语从句: because, since",
            "条件状语从句: if（真实条件）",
            "表语从句: That's why...",
            "单层从句嵌套",
            # 语态
            "被动语态: 一般现在时和一般过去时",
            # 情态动词
            "must/have to（义务区分）",
            "may/might（可能性）",
            "can/could（能力/请求/允许）",
            "should（建议/义务）",
            "情态动词完成式（基本: must have been, can't have gone）",
            # 虚拟语气
            "第二条件句（If I had money, I would travel）",
            # 句子结构
            "长短句交替，单句6-14词",
            "间接引语: 陈述句和疑问句",
            "疑问尾句: You like coffee, don't you?",
            "so/such, too/enough",
            "动名词 vs 不定式（begin类: start doing/to do）",
            # 词法
            "连词: although, however, unless, as long as",
            "形容词顺序",
            "短语动词基本",
        ],
        "unavailable": [
            "过去完成进行时",
            "将来完成时",
            "第三条件句",
            "非限定性定语从句",
            "分词从句",
            "倒装句",
            "wish/if only（属于B2）",
            "使役结构 have/get sth done",
        ],
    },
    "B2": {
        "available": [
            # 时态
            "现在完成进行时（强调持续）",
            "过去完成时（过去的过去: I had already left）",
            "过去完成进行时（基本）",
            "将来进行时（将来某时正在发生 + 委婉询问）",
            "将来完成时（By Friday, I will have finished）",
            "过去将来时（从过去看将来）",
            # 从句
            "定语从句（非限定性）: which, who（带逗号）",
            "定语从句: whose, where, when",
            "时间状语从句: as soon as, until",
            "条件状语从句: unless, provided that, as long as",
            "让步状语从句: although, even though",
            "原因状语从句: as, for",
            "方式状语从句: as, like",
            "结果状语从句: so...that, such...that",
            "目的状语从句: so that, in order that",
            "主语从句: what引导（What I need is...）",
            "表语从句: The reason is that...",
            "偶尔两层从句嵌套",
            # 语态
            "被动语态: 所有基本时态, 含情态动词被动",
            "使役结构: have/get sth done",
            # 情态动词
            "情态动词推测: must have, can't have, might have, should have（过去推测）",
            "情态动词: all common modals熟练使用",
            # 虚拟语气
            "第三条件句（If I had known, I would have come）",
            "混合条件句",
            "wish / if only 表示愿望和遗憾",
            "it's time + 过去式",
            # 句子结构
            "复杂句增多，单句6-14词",
            "间接引语: 时态后移",
            "分词从句（Walking home, I saw...）",
            "话语标记语: however, therefore, furthermore",
            # 词法
            "短语动词大量掌握",
            "名词化基本用法",
            "强调结构: It is... that/who（分裂句基本）",
        ],
        "unavailable": [
            "倒装句（否定副词开头）— 仅基本了解",
            "报告动词被动（It is said that...）",
            "虚拟语气高级用法（正式文体）",
            "无动词从句",
            "复杂分词从句嵌套",
        ],
    },
    "C1": {
        "available": [
            # 时态
            "所有时态流畅运用, 进行体和完成体的精确切换",
            "将来完成进行时",
            # 从句
            "定语从句: 熟练使用限定性和非限定性",
            "定语从句: 介词+which",
            "时间状语从句: the moment, no sooner...than",
            "条件状语从句: 混合时态条件句",
            "让步状语从句: despite, in spite of, much as",
            "方式状语从句: as if, as though（含虚拟）",
            "结果状语从句: to such an extent that",
            "目的状语从句: lest, for fear that",
            "原因从句: seeing that, in that",
            "主语从句: That...is, Whether...or",
            "同位语从句: The fact that...",
            "多层从句嵌套, 逻辑关系复杂",
            # 语态
            "被动语态: 过去完成时, 进行时, 报告动词",
            "无主被动: It is said that...",
            "使役结构: get sth done, need doing",
            # 情态动词
            "情态动词细微辨析: needn't have vs didn't need to",
            "should have vs ought to have",
            # 虚拟语气
            "所有条件句: 显性和隐性",
            "倒装条件句（Had I known...）",
            "虚拟语气完整掌握（含正式文体）",
            # 句子结构
            "长句频繁，单句10-18词",
            "倒装句全范围: Not only..., Rarely..., Only when...",
            "分裂句和假分裂句",
            "分词从句完整掌握",
            "名词化高级运用",
            "省略与替代",
            "复杂介词: notwithstanding, in accordance with",
            "语篇标记语全范围",
            # 词法
            "正式/非正式语体语法切换",
            "无动词从句",
            "高级比较结构",
        ],
        "unavailable": [
            "C2级别特有修辞性语法和深层嵌套",
        ],
    },
    "C2": {
        "available": [
            # 所有语法结构达到母语级精确度
            "时态: 所有时态在任何语境下的无障碍使用",
            "从句: 多层级嵌套从句流畅准确",
            "语态: 主动/被动在任何场景下的自如切换",
            # 高级语法
            "倒装条件句（Were it not for...）",
            "倒装让步（Try as he might...）",
            "倒装时间状语（Hardly had...when）",
            "倒装否定（Not only..., Rarely..., Only when...）的任意使用",
            "虚拟语气在正式/文学文体中的使用",
            "含蓄条件句",
            "修辞性语法: 排比、对比、强调",
            # 语用
            "语域切换: 可根据交际场景自如切换语法风格",
            "语法选择带有风格意识（正式/非正式，口语/书面语，学术/文学）",
            "微妙情态差异: 能根据语境选择最精确的表达",
            "任何语法结构的直觉性正确运用",
            "能够识别并修正细微语法偏差",
        ],
        "unavailable": [
            # C2 无语法限制
        ],
    },
}

# ════════════════════════════════════════════
# 疑问句复杂度（补充）
# ════════════════════════════════════════════

QUESTION_FORMS: dict[str, dict[str, list[str]]] = {
    "A1": {
        "available": [
            "Wh-疑问句: What/Where/Who/How + be (What is this?)",
            "Yes/No 疑问句: be 提前 (Are you a student?)",
            "or 选择疑问句: Is it A or B?",
            "How much/many 询问数量和价格",
        ],
        "unavailable": [
            "间接疑问句 (Can you tell me where...)",
            "否定疑问句 (Don't you like it?)",
            "疑问词 + to do (I don't know what to do)",
            "嵌入疑问 (Do you know what time it is?)",
        ],
    },
    "A2": {
        "available": [
            "Wh-疑问句: do/does/did 助动词 (Where do you live?)",
            "How often/long/far 频率和程度疑问",
            "Which 选择疑问 (Which one do you prefer?)",
            "Whose 所有格疑问 (Whose book is this?)",
            "间接疑问句（基本）: Can you tell me where the station is?",
            "疑问词 + 不定式（基本）: I don't know where to go",
        ],
        "unavailable": [
            "嵌套疑问 (Do you know what time the meeting starts?)",
            "否定疑问句表示惊讶/确认",
            "疑问尾句 (question tags)",
        ],
    },
    "B1": {
        "available": [
            "嵌入疑问: Do you know where he lives?",
            "疑问尾句 (You like coffee, don't you?)",
            "否定疑问句: Don't you think it's a good idea?",
            "间接疑问句完整使用: Could you tell me when the train arrives?",
            "What/How about 建议疑问",
            "Why don't we/you 建议句式",
            "反问句（基本）: Who doesn't want to be happy?",
        ],
        "unavailable": [
            "复杂嵌入疑问（含完成时/情态+完成）",
            "修辞问句 (Who cares?)",
        ],
    },
    "B2": {
        "available": [
            "复杂嵌入疑问: Do you have any idea when the meeting might finish?",
            "疑问尾句: 各种时态和情态 (You've been there, haven't you?)",
            "间接疑问中的时态后移: He asked where I was going",
            "I was wondering if... 委婉询问",
            "修辞问句: Who wouldn't want to succeed?",
            "Would you mind if I... 礼貌请求",
        ],
        "unavailable": [
            "多层嵌套疑问含虚拟",
            "正式语体中的间接疑问 (I should be grateful if you would inform me...)",
        ],
    },
    "C1": {
        "available": [
            "多层嵌套疑问: Could you clarify what you meant when you said...?",
            "修辞问句在论述中的使用",
            "正式间接疑问: I would be grateful if you could let me know whether...",
            "疑问句中的强调和倒装: What exactly is it that you want?",
            "Would it be possible for you to...? 极度委婉",
        ],
        "unavailable": [],
    },
    "C2": {
        "available": [
            "任意复杂度的疑问句，含多层嵌套、虚拟、倒装",
            "可根据语境和听众自如选择疑问句的正式度和直接度",
        ],
        "unavailable": [],
    },
}

# ════════════════════════════════════════════
# 否定结构（补充）
# ════════════════════════════════════════════

NEGATION_FORMS: dict[str, dict[str, list[str]]] = {
    "A1": {
        "available": [
            "be + not (I am not a student)",
            "do/does + not (I don't like coffee)",
            "can + not (I can't swim)",
            "no + 名词 (no problem, no money)",
            "祈使否定: Don't go!",
        ],
        "unavailable": [
            "双重否定",
            "部分否定 (not all, not every)",
            "否定转移 (I don't think he is...)",
            "倒装否定 (Never have I...)",
        ],
    },
    "A2": {
        "available": [
            "did + not (I didn't go)",
            "will/would + not (I won't be late)",
            "have/has + not (I haven't seen it)",
            "不定代词否定: nothing, nobody, nowhere",
            "never, hardly 等否定副词（基本）",
        ],
        "unavailable": [
            "否定转移",
            "部分否定 (not everyone agrees)",
            "Not only...but also...",
        ],
    },
    "B1": {
        "available": [
            "否定转移: I don't think he is right (≠ I think he isn't right)",
            "部分否定: not all, not every, not always",
            "not...any more / any longer",
            "not...either (I don't like it either)",
            "without + 动名词 (without asking)",
        ],
        "unavailable": [
            "倒装否定 (Never have I seen...)",
            "Not until... / Not only... 句首倒装",
            "否定条件句 (Unless = if not — B2 精准使用)",
        ],
    },
    "B2": {
        "available": [
            "倒装否定: Never have I seen such a thing",
            "Not only...but also... (Not only did he refuse, but he also...)",
            "Not until 句首倒装: Not until I arrived did I realize...",
            "Hardly/Scarcely...when: Hardly had I sat down when...",
            "No sooner...than: No sooner had we left than it started raining",
            "Neither/Nor 倒装: I don't like it. Nor does my wife.",
            "双重否定（强调）: It's not uncommon to see...",
        ],
        "unavailable": [
            "复杂否定+虚拟复合结构",
            "文学性否定修辞",
        ],
    },
    "C1": {
        "available": [
            "所有倒装否定结构的自如使用",
            "否定+虚拟: Were it not for..., I would...",
            "含蓄否定: far from, rather than, instead of",
            "否定在学术/正式语体中的精确使用",
            "I can't help but wonder... / There's no denying that...",
        ],
        "unavailable": [],
    },
    "C2": {
        "available": [
            "所有否定结构达到母语级精确度",
            "微妙否定语义的区分 (hardly vs barely vs scarcely)",
            "否定修辞在文学和正式语体中的自如运用",
        ],
        "unavailable": [],
    },
}

# ════════════════════════════════════════════
# 基础语言特征（每级别的量化指标）
# ════════════════════════════════════════════

LEVEL_FEATURES: dict[str, dict[str, str]] = {
    "A1": {
        "单句词数": "5-7词",
        "句长规律": "超短句，极少超过5词",
        "信息密度": "单信息/多句",
    },
    "A2": {
        "单句词数": "5-12词",
        "句长规律": "短句为主，极少超过12词",
        "信息密度": "单信息/句",
    },
    "B1": {
        "单句词数": "6-14词",
        "句长规律": "长短句交替，长句不超过14词",
        "信息密度": "1-2个信息/句",
    },
    "B2": {
        "单句词数": "6-14词",
        "句长规律": "复杂句增多，可接受12词左右",
        "信息密度": "2-3个信息/句",
    },
    "C1": {
        "单句词数": "10-18词",
        "句长规律": "长句频繁，可达20-25词",
        "信息密度": "3个以上信息/句",
    },
    "C2": {
        "单句词数": "12-30词",
        "句长规律": "长句主导，可达30词，结构复杂",
        "信息密度": "多层信息/句，含隐含信息",
    },
}

# ════════════════════════════════════════════
# 工具函数
# ════════════════════════════════════════════

LEVEL_ORDER = {'A1': 0, 'A2': 1, 'B1': 2, 'B2': 3, 'C1': 4, 'C2': 5}


def get_feature_text(level: str) -> str:
    """获取该级别的基础语言特征描述"""
    features = LEVEL_FEATURES.get(level, {})
    if not features:
        return ""
    lines = [f"{level} 级别语言特征："]
    for k, v in features.items():
        lines.append(f"  - {k}: {v}")
    return "\n".join(lines)


def build_grammar_prompt_for_level(level: str) -> str:
    """生成给 LLM 的语法参考 prompt 片段
    
    列出该级别可用的语法结构 + 超纲警告。
    """
    grammar = GRAMMAR_TABLE.get(level, {})
    available = grammar.get("available", [])
    unavailable = grammar.get("unavailable", [])

    lines = [f"### {level} 级别语法参考", ""]

    # 基础特征
    features = LEVEL_FEATURES.get(level, {})
    if features:
        lines.append(f"**基础特征：** 单句{features.get('单句词数', '')}，{features.get('句长规律', '')}")
        lines.append("")

    # 可用语法（精选）
    if available:
        lines.append(f"**该级别可用的语法结构（精选）：**")
        for item in available[:12]:
            lines.append(f"  - {item}")
        lines.append("")

    # 疑问句
    qf = QUESTION_FORMS.get(level, {})
    q_avail = qf.get("available", [])
    if q_avail:
        lines.append(f"**疑问句能力：**")
        for item in q_avail[:4]:
            lines.append(f"  - {item}")
        lines.append("")

    # 否定
    nf = NEGATION_FORMS.get(level, {})
    n_avail = nf.get("available", [])
    if n_avail:
        lines.append(f"**否定结构能力：**")
        for item in n_avail[:4]:
            lines.append(f"  - {item}")
        lines.append("")

    # 超纲语法（精选不超过8条）
    all_unavailable = list(unavailable)
    all_unavailable.extend(qf.get("unavailable", [])[:2])
    all_unavailable.extend(nf.get("unavailable", [])[:2])
    if all_unavailable:
        lines.append(f"**以下语法属于{level}级别超纲，出现应标 D-3（语法过难）：**")
        for item in all_unavailable[:8]:
            lines.append(f"  - {item}")
        lines.append("")

    return "\n".join(lines)


def check_grammar_match(question: dict, level: str) -> dict:
    """检查题目中使用的语法是否超出目标级别
    
    Args:
        question: 题目数据（含stem, options等）
        level: 目标级别如 'B1'
    
    Returns:
        {'over_level_patterns': [...], 'offset': 0/1/2+}
    
    注意：语法检测仍以 LLM 判断为主，此函数提供关键词辅助。
    """
    grammar = GRAMMAR_TABLE.get(level, {})
    unavailable = grammar.get("unavailable", [])
    target_idx = LEVEL_ORDER.get(level, 1)

    # 合并题目文本
    text = question.get("stem", "") + " "
    for opt in question.get("options", []):
        text += str(opt) + " "

    # 关键词检测（辅助用，不替代 LLM 判断）
    warning_patterns = {
        "虚拟语气": ["if I were", "wish I", "if only", "it's time", "as if", "as though", "had I known"],
        "被动语态": ["is made", "are built", "was done", "were seen", "has been", "being done", "is said to"],
        "过去完成": ["had been", "had done", "had already", "had never"],
        "倒装句": ["not only", "never have", "rarely", "only when", "no sooner", "hardly had"],
        "第三条件句": ["would have", "could have", "might have been"],
        "分词从句": ["having finished", "walking home", "looking at"],
        "否定转移": ["don't think", "doesn't think", "didn't think"],
        "倒装否定": ["not until", "never have I", "nor does", "neither do"],
        "嵌入疑问": ["do you know what", "do you know where", "can you tell me when"],
        "疑问尾句": [", don't you", ", isn't it", ", haven't you", ", won't you"],
    }

    over_level = []
    for pattern_type, keywords in warning_patterns.items():
        if any(kw.lower() in text.lower() for kw in keywords):
            # 检查此结构是否在超纲列表中
            for una in unavailable:
                if pattern_type in una or any(kw.lower() in una.lower() for kw in keywords[:1]):
                    over_level.append(pattern_type)

    return {
        "over_level_patterns": list(set(over_level)),
        "offset": target_idx,  # LLM 使用此信息进一步判断
    }
