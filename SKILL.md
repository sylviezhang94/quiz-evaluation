# Skill: quiz-evaluation

## 概述

按照教研侧评测标准对出题结果进行质量评测。输入为飞书文档中的题目表格，由 LLM 逐维度打分并生成评测报告。

## 触发条件

- 用户说：出题评测、题目评测、评测题目、evaluate questions、quiz evaluation
- 用户提供飞书文档链接并要求评测其中的题目

## 输入格式

飞书文档中应包含题目表格，列名建议：

| 列名 | 说明 | 必填 |
|-|-|-|
| 题目ID | 唯一标识 | 是 |
| 级别 | A1/A2/B1/B2/C1/C2 | 是 |
| 题型 | S2/REVIEW_S1/REVIEW_S2/DRAG_SORT/S5/REVIEW_S3 | 是 |
| 学习模式 | english/native | 否（默认native） |
| 知识点 | 核心知识点 | 是 |
| 题干 | 题目引导文本 | 是 |
| 选项 | 逗号分隔的选项列表 | 视题型而定 |
| 正确答案 | 正确选项内容 | 是 |
| 来源台词 | 知识点出现的源台词 | 否 |
| 句子长度(词数) | 题干句子词数 | 否 |
| 备注 | 其他说明 | 否 |

## 工作流

### 步骤 1：读取飞书文档

用 `lark-cli docs +fetch --api-version v2 --doc "<文档URL或token>" --doc-format markdown` 读取文档内容。

**必须**先读取 [`../lark-doc/references/lark-doc-fetch.md`](../lark-doc/references/lark-doc-fetch.md) 了解读取策略。

### 步骤 2：解析题目

从文档的 Markdown/XML 内容中提取题目表格。将每一行转换为 `Question` 对象。

**必须**先读取 `./models.py` 了解数据结构。

### 步骤 3：逐题评判

对每道题，按以下流程执行 LLM 评判：

1. 读取该题对应的 CEFR 规则：`from rules_engine import get_rule` → 获取 `LevelRule`
2. 读取评判评分卡：`./rubric.py` 中的 `EVALUATION_RUBRIC`（八维度 0/1/2 标准 + 问题标签表）
3. 构建评判 prompt，调用 LLM（即当前 agent 自身进行推理判断）给出：
   - 每个维度的评分（0/1/2）+ 理由
   - 问题标签列表
   - 修改建议

**评判质量要求**：
- 对于自动可判的维度（建议数、句子长度等），必须精确对照规则数值
- 对于需理解的维度（语言正确性、选项设计等），需认真分析题目内容
- 禁止敷衍地给所有维度打 2 分或 1 分

### 步骤 4：汇总报告

生成评测报告：
- 控制台打印汇总统计 + 每题详情（参考 `./report.py` 的 `print_report`）
- 如有需要，可将结果 CSV 写入飞书文档

## 文件清单

| 文件 | 用途 |
|-|-|
| `SKILL.md` | 本文件 |
| `models.py` | 数据模型（Question、EvaluationResult、ProblemTag、Score 等） |
| `rules_engine.py` | CEFR 级别×题型约束规则（从级联总表提取） |
| `rubric.py` | LLM 评判评分卡模板（八维度标准 + 标签体系） |
| `report.py` | 报告生成工具 |

## 外部依赖

- `lark-cli docs +fetch --api-version v2`：读取飞书文档
- 依赖 `lark-doc` / `lark-shared` skill 的认证机制

## 关于工作目录

执行此 skill 时，通常在用户的题目评测项目目录下操作。Python 代码可通过以下方式导入：

```python
import sys; sys.path.insert(0, os.path.expanduser('~/.agents/skills/quiz-evaluation'))
from models import ...
from rules_engine import ...
from rubric import ...
from report import ...
```
