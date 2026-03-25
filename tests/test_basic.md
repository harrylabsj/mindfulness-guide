# Mindfulness Guide - 基础测试

## 测试环境
- Python 3.8+

## 测试用例

### Test 1: 呼吸练习

```bash
python3 scripts/main.py breathe --technique 4-7-8 --cycles 2
```

预期：输出呼吸步骤和时间估算

### Test 2: 身体扫描

```bash
python3 scripts/main.py body-scan
```

预期：输出完整的身体扫描步骤

### Test 3: 压力缓解

```bash
python3 scripts/main.py stress --level 3
```

预期：输出压力等级对应的建议

### Test 4: 睡前放松

```bash
python3 scripts/main.py sleep
```

预期：输出睡前放松步骤

### Test 5: JSON 输出

```bash
python3 scripts/main.py breathe --json
```

预期：JSON 格式输出

## 验收标准

- [x] 呼吸练习功能正常
- [x] 身体扫描功能正常
- [x] 压力缓解功能正常
- [x] 睡前放松功能正常
- [x] JSON 输出正常

