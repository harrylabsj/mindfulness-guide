# Mindfulness Guide - 使用示例

## 基本使用

### 1. 呼吸练习

```bash
cd ~/.openclaw/skills/mindfulness-guide
python3 scripts/main.py breathe
```

指定技巧和循环：
```bash
python3 scripts/main.py breathe --technique box --cycles 3
```

### 2. 身体扫描

```bash
python3 scripts/main.py body-scan
```

### 3. 压力缓解

```bash
python3 scripts/main.py stress --level 3
```

### 4. 睡前放松

```bash
python3 scripts/main.py sleep
```

### 5. 演示模式

```bash
python3 scripts/main.py demo
```

### 6. JSON 输出

```bash
python3 scripts/main.py breathe --json
```

## 可用呼吸技巧

| 技巧 | 描述 |
|------|------|
| 4-7-8 | 放松神经、帮助入睡 |
| box | 平衡身心、提高专注力 |
| deep | 基础深度呼吸 |

## 程序化调用

```python
from main import MindfulnessGuide

guide = MindfulnessGuide()
result = guide.guide_breathing('4-7-8', cycles=4)
print(result['estimated_time'])
```

