# quiz-evaluation

CEFR-graded quiz quality evaluation skill — 按照教研侧评测标准，对 AI 出题结果进行八维度质量评测。

## 工作流

```
飞书文档/表格 → lark-cli 读取题目 → LLM 逐维度评判(0/1/2) → 生成评测报告
```

## 文件结构

```
quiz-evaluation/
├── SKILL.md           # Skill 定义，agent 加载此文件获取工作流
├── models.py           # 数据模型：Question、EvaluationResult、ProblemTag
├── rules_engine.py     # CEFR 级别×题型约束规则（5题型×6级别×2学习模式）
├── rubric.py           # LLM 评判评分卡（八维度标准+标签体系+prompt模板）
├── report.py           # 报告生成（控制台+CSV）
└── examples/
    ├── sample_input.csv   # 示例输入（10道覆盖所有级别/题型）
    └── sample_output.csv  # 示例输出
```

## 评测维度

| 维度 | 0分（有瑕疵） | 1分（可用） | 2分（满意） |
|------|------------|-----------|-----------|
| 知识点匹配 | 相关但偏移 | 精准但不完美 | 精准清晰 |
| 题型合规性 | UI细节可优化 | 符合规范 | 完全符合级别规范 |
| 语言正确性 | 生硬不自然 | 基本准确 | 准确自然地道 |
| 级别适配度 | 有超纲词 | 基本符合 | 完全符合CEFR |
| 选项设计 | 干扰偏弱 | 设计合理 | 巧妙有效 |
| 题干清晰度 | 需思考 | 基本清晰 | 清晰无歧义 |
| 语境关联 | 缺上下文 | 不够充分 | 充分支撑 |
| 交互体验 | 打断感强 | 稍有打断 | 自然流畅 |

## 使用方法

在 agent 对话中直接说：

> 帮我评测这个表格里的题目：https://xxx.feishu.cn/sheets/xxxxx

或触发关键词：`出题评测`、`题目评测`、`evaluate questions`

## 外部依赖

- `lark-cli` — 读取飞书文档
- 飞书认证（`lark-shared` skill）
