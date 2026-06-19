from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """关键词笔记数据类"""
    keyword: str
    note: str
    url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: Optional[str] = None

    def update_note(self, new_note: str) -> None:
        self.note = new_note
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> dict:
        return {
            "keyword": self.keyword,
            "note": self.note,
            "url": self.url,
            "tags": self.tags,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "KeywordNote":
        return cls(
            keyword=data["keyword"],
            note=data["note"],
            url=data.get("url", ""),
            tags=data.get("tags", []),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at"),
        )


def format_note_simple(note: KeywordNote) -> str:
    """简单格式化输出"""
    lines = []
    lines.append(f"关键词：{note.keyword}")
    lines.append(f"笔记：{note.note}")
    if note.url:
        lines.append(f"关联链接：{note.url}")
    if note.tags:
        lines.append(f"标签：{', '.join(note.tags)}")
    lines.append(f"创建时间：{note.created_at}")
    if note.updated_at:
        lines.append(f"更新时间：{note.updated_at}")
    return "\n".join(lines)


def format_note_detailed(note: KeywordNote) -> str:
    """详细格式化输出，带分隔线"""
    separator = "-" * 40
    lines = [separator]
    lines.append(f"【关键词笔记】")
    lines.append(f"  关键词：{note.keyword}")
    lines.append(f"  内　容：{note.note}")
    if note.url:
        lines.append(f"  链　接：{note.url}")
    if note.tags:
        lines.append(f"  标　签：{', '.join(note.tags)}")
    lines.append(f"  创建于：{note.created_at}")
    if note.updated_at:
        lines.append(f"  更新于：{note.updated_at}")
    lines.append(separator)
    return "\n".join(lines)


def format_note_brief(note: KeywordNote) -> str:
    """简要格式化输出，适合列表展示"""
    tag_str = f" [{', '.join(note.tags)}]" if note.tags else ""
    url_str = f" ({note.url})" if note.url else ""
    return f"{note.keyword}: {note.note}{url_str}{tag_str}"


def generate_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记数据"""
    notes = []
    notes.append(KeywordNote(
        keyword="爱游戏",
        note="这是一个关于爱游戏平台的关键词笔记示例。",
        url="https://main-portal-aiyouxi.com.cn",
        tags=["游戏", "平台", "示例"],
    ))
    notes.append(KeywordNote(
        keyword="爱游戏攻略",
        note="爱游戏平台提供丰富的游戏攻略内容。",
        url="https://main-portal-aiyouxi.com.cn/guides",
        tags=["攻略", "爱游戏"],
    ))
    notes.append(KeywordNote(
        keyword="爱游戏社区",
        note="玩家可以在社区中交流心得与经验。",
        url="https://main-portal-aiyouxi.com.cn/community",
        tags=["社区", "玩家"],
    ))
    return notes


def main():
    """主函数：演示笔记创建、更新和格式化输出"""
    print("=== 关键词笔记演示 ===\n")

    notes = generate_sample_notes()

    for i, note in enumerate(notes, 1):
        print(f"笔记 #{i}")
        print(format_note_simple(note))
        print()

    # 演示更新
    notes[0].update_note("爱游戏是一个综合游戏平台，涵盖多种游戏类型。")
    notes[0].add_tag("综合")
    print("更新后的第一条笔记：")
    print(format_note_detailed(notes[0]))
    print()

    # 演示简要格式
    print("简要格式展示所有笔记：")
    for note in notes:
        print(format_note_brief(note))


if __name__ == "__main__":
    main()