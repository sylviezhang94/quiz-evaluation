from __future__ import annotations
"""CEFR 词汇数据库

从飞书词表（A1→C2，6个sheet）构建。
提供单词→级别查询，供评测时判断知识点是否超纲。
"""

import json, os

# Load at module level
_VOCAB: dict[str, dict] = {}
_vocab_path = os.path.join(os.path.dirname(__file__), 'cefr_vocab.json')

def _load():
    global _VOCAB
    if not _VOCAB and os.path.exists(_vocab_path):
        with open(_vocab_path, 'r', encoding='utf-8') as f:
            _VOCAB = json.load(f)

def lookup(word: str) -> dict | None:
    """查询单词的CEFR级别
    
    Args:
        word: 单词（英文）
    
    Returns:
        {'level': 'A2', 'pos': 'noun'} 或 None
    """
    _load()
    if not word:
        return None
    key = word.strip().lower()
    return _VOCAB.get(key)

def get_level(word: str) -> str | None:
    """查询单词的CEFR级别，仅返回级别字符串（如'A2'）或None"""
    info = lookup(word)
    return info['level'] if info else None

def _strip_inflection(word: str) -> list[str]:
    """尝试去除常见屈折词缀，返回可能的原形列表"""
    variants = [word]
    w = word.lower().strip('()"\' ')
    # Past tense / participle
    if w.endswith('ied'):
        variants.append(w[:-3] + 'y')
    if w.endswith('ed') and len(w) > 3:
        variants.append(w[:-2])
        variants.append(w[:-1])  # e.g. "liked" → "like"
    if w.endswith('ing') and len(w) > 4:
        variants.append(w[:-3])
        base = w[:-3]
        if not base.endswith('e'):
            variants.append(base + 'e')  # e.g. "making" → "make"
    # Plural / 3rd person
    if w.endswith('ies') and len(w) > 4:
        variants.append(w[:-3] + 'y')
    if w.endswith('es') and len(w) > 3:
        variants.append(w[:-2])
        variants.append(w[:-1])
    if w.endswith('s') and len(w) > 3 and not w.endswith('ss'):
        variants.append(w[:-1])
    # Comparative / superlative
    if w.endswith('ier'):
        variants.append(w[:-3] + 'y')
    if w.endswith('iest'):
        variants.append(w[:-4] + 'y')
    return variants


def check_level_match(knowledge_point: str, target_level: str) -> dict:
    """检查知识点词是否与目标级别匹配
    
    Args:
        knowledge_point: 如 'crazy' 或 'going crazy' 或 'refused (word)'
        target_level: 目标CEFR级别如 'A2'
    """
    LEVEL_ORDER = {'A1': 0, 'A2': 1, 'B1': 2, 'B2': 3, 'C1': 4, 'C2': 5}
    
    # Clean: "(word)" suffix removal
    kp_clean = knowledge_point.strip().lower().replace(' (word)', '').replace(' (phrase)', '')
    
    # Try exact matches and variants
    words_to_try = [kp_clean]
    
    # Also try full phrase
    if ' ' in kp_clean:
        words_to_try.append(kp_clean)
    
    # Try individual words from phrase
    for part in kp_clean.split():
        clean_part = part.strip('()"\' ')
        if len(clean_part) > 2 and clean_part not in ('the', 'is', 'of', 'to', 'in', 'on', 'at', 'no', 'be', 'it'):
            words_to_try.append(clean_part)
            # Also try de-inflected forms
            words_to_try.extend(_strip_inflection(clean_part))
    
    # Deduplicate while preserving order
    seen = set()
    unique_words = []
    for w in words_to_try:
        if w not in seen:
            seen.add(w)
            unique_words.append(w)
    
    for w in unique_words:
        info = lookup(w)
        if info:
            target_idx = LEVEL_ORDER.get(target_level, -1)
            word_idx = LEVEL_ORDER.get(info['level'], -1)
            offset = word_idx - target_idx if target_idx >= 0 and word_idx >= 0 else 0
            return {
                'word': w,
                'vocab_level': info['level'],
                'match': info['level'] == target_level or offset <= 0,
                'offset': offset,
            }
    
    return {'word': '', 'vocab_level': 'unknown', 'match': True, 'offset': 0}
