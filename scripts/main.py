#!/usr/bin/env python3
"""
Mindfulness Guide - Main Script
Provides guided mindfulness and meditation exercises
"""

import sys
import json
import argparse
from typing import Dict, List, Optional


class MindfulnessGuide:
    """正念引导核心类"""
    
    BREATHING_EXERCISES = {
        '4-7-8': {
            'name': '4-7-8 呼吸法',
            'inhale': 4,
            'hold': 7,
            'exhale': 8,
            'description': '放松神经、帮助入睡的呼吸技巧'
        },
        'box': {
            'name': '方块呼吸',
            'inhale': 4,
            'hold': 4,
            'exhale': 4,
            'hold_after': 4,
            'description': '平衡身心、提高专注力的呼吸方法'
        },
        'deep': {
            'name': '深度呼吸',
            'inhale': 5,
            'hold': 2,
            'exhale': 5,
            'description': '简单易学的基础呼吸练习'
        }
    }
    
    BODY_SCAN_STEPS = [
        "找一个舒适的姿势躺下或坐着",
        "闭上眼睛，做几次深呼吸",
        "注意力集中在脚趾，感受它们的状态",
        "慢慢向上移动到脚踝、小腿",
        "感受膝盖、大腿的重量",
        "注意腹部的起伏",
        "感受胸腔的心脏跳动",
        "肩膀是否紧绷？放松它们",
        "手臂、手腕、手掌依次放松",
        "面部肌肉、下巴、额头",
        "整个身体作为一个整体感受"
    ]
    
    def __init__(self):
        self.current_exercise = None
        
    def guide_breathing(self, technique: str = '4-7-8', cycles: int = 4) -> Dict:
        """引导呼吸练习"""
        if technique not in self.BREATHING_EXERCISES:
            return {'error': f'未知呼吸技巧: {technique}'}
        
        ex = self.BREATHING_EXERCISES[technique]
        total_time = (ex['inhale'] + ex.get('hold', 0) + ex['exhale'] + ex.get('hold_after', 0)) * cycles
        
        steps = []
        for i in range(1, cycles + 1):
            steps.append({
                'cycle': i,
                'actions': [
                    f"吸气 {ex['inhale']} 秒...",
                    f"屏住呼吸 {ex.get('hold', 0)} 秒..." if ex.get('hold', 0) > 0 else None,
                    f"呼气 {ex['exhale']} 秒...",
                    f"停顿 {ex.get('hold_after', 0)} 秒..." if ex.get('hold_after', 0) > 0 else None,
                ]
            })
        
        return {
            'technique': technique,
            'name': ex['name'],
            'description': ex['description'],
            'cycles': cycles,
            'estimated_time': f"{total_time}秒 ({total_time//60}分{total_time%60}秒)",
            'steps': [s for s in steps if s['actions'][0]]
        }
    
    def guide_body_scan(self) -> Dict:
        """引导身体扫描"""
        return {
            'name': '身体扫描冥想',
            'duration': '10-15分钟',
            'steps': self.BODY_SCAN_STEPS,
            'tips': [
                '保持缓慢的呼吸节奏',
                '不要强迫自己放松',
                '如果有不适感，轻轻转移注意力',
                '结束后慢慢睁开眼睛'
            ]
        }
    
    def get_stress_relief(self, level: int = 5) -> Dict:
        """压力缓解建议"""
        suggestions = {
            1: ['喝一杯温水', '深呼吸3次', '看看窗外'],
            2: ['短暂散步', '听轻音乐', '做简单的伸展'],
            3: ['进行5分钟冥想', '写下烦恼', '联系朋友'],
            4: ['长时间散步', '洗热水澡', '练习瑜伽'],
            5: ['尝试完整冥想', '考虑专业帮助', '给自己放假']
        }
        
        return {
            'stress_level': level,
            'suggestions': suggestions.get(level, suggestions[3]),
            'breathing_exercise': '4-7-8',
            'reminder': '如果压力持续，请考虑寻求专业支持'
        }
    
    def get_sleep_relaxation(self) -> Dict:
        """睡前放松引导"""
        return {
            'name': '睡前放松练习',
            'duration': '15分钟',
            'steps': [
                '1. 平躺好，关闭灯光',
                '2. 做3次深度呼吸',
                '3. 从脚趾开始，逐渐放松全身',
                '4. 想象自己在一个安静的地方',
                '5. 保持缓慢均匀的呼吸',
                '6. 慢慢入睡...'
            ],
            'tips': [
                '避免使用手机等电子设备',
                '保持房间凉爽',
                '可以配合轻柔音乐'
            ]
        }


def format_breathing_guide(result: Dict) -> str:
    """格式化呼吸引导输出"""
    output = []
    output.append("=" * 50)
    output.append(f"🧘 {result['name']}")
    output.append("=" * 50)
    output.append(f"📝 {result['description']}")
    output.append(f"⏱️ 预计时间: {result['estimated_time']}")
    output.append(f"🔄 循环次数: {result['cycles']}")
    output.append("\n📋 步骤:")
    for step in result['steps']:
        actions = [a for a in step['actions'] if a]
        output.append(f"  第{step['cycle']}轮: {' → '.join(actions)}")
    output.append("\n" + "=" * 50)
    return "\n".join(output)


def format_body_scan(result: Dict) -> str:
    """格式化身体扫描输出"""
    output = []
    output.append("=" * 50)
    output.append(f"🧘 {result['name']}")
    output.append("=" * 50)
    output.append(f"⏱️ 预计时间: {result['duration']}")
    output.append("\n📋 步骤:")
    for i, step in enumerate(result['steps'], 1):
        output.append(f"  {i}. {step}")
    output.append("\n💡 小贴士:")
    for tip in result['tips']:
        output.append(f"  • {tip}")
    output.append("\n" + "=" * 50)
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description='Mindfulness Guide - 正念引导工具')
    parser.add_argument('command', choices=['breathe', 'body-scan', 'stress', 'sleep', 'demo'],
                       help='命令类型')
    parser.add_argument('--technique', '-t', default='4-7-8', help='呼吸技巧')
    parser.add_argument('--cycles', '-c', type=int, default=4, help='循环次数')
    parser.add_argument('--level', '-l', type=int, default=5, help='压力等级1-5')
    parser.add_argument('--json', action='store_true', help='JSON输出')
    
    args = parser.parse_args()
    
    guide = MindfulnessGuide()
    
    if args.command == 'demo':
        # 演示所有功能
        print("=== 呼吸练习示例 ===")
        result = guide.guide_breathing('box', 2)
        print(format_breathing_guide(result))
        print("\n=== 身体扫描示例 ===")
        result = guide.guide_body_scan()
        print(format_body_scan(result))
        return
    
    result = None
    if args.command == 'breathe':
        result = guide.guide_breathing(args.technique, args.cycles)
    elif args.command == 'body-scan':
        result = guide.guide_body_scan()
    elif args.command == 'stress':
        result = guide.get_stress_relief(args.level)
    elif args.command == 'sleep':
        result = guide.get_sleep_relaxation()
    
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        if args.command == 'breathe':
            print(format_breathing_guide(result))
        elif args.command == 'body-scan':
            print(format_body_scan(result))
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
