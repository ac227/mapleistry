import yaml
import re
from pathlib import Path


def get_nav_order():
    with open('mkdocs.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config.get('nav', [])


def flatten_nav(nav, base_path=Path('docs')):
    files = []
    for item in nav:
        if isinstance(item, dict):
            for title, content in item.items():
                if isinstance(content, list):
                    files.extend(flatten_nav(content, base_path))
                elif isinstance(content, str):
                    files.append(base_path / content)
        elif isinstance(item, str):
            files.append(base_path / item)
    return files


def combine_markdown():
    nav = get_nav_order()
    md_files = flatten_nav(nav)

    output = []
    for md_file in md_files:
        if md_file.exists():
            print(f"🔄 Processing: {md_file}")
            output.append("\n\n\\newpage\n\n")
            title = md_file.stem.replace('-', ' ').title()
            output.append(f"# {title}\n\n")

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.startswith('---'):
                    content = content.split('---', 2)[-1].strip()

                # 清理空图片，避免 pandoc withBinaryFile 报错
                content = re.sub(r'!\[\s*\]\(\s*[^)]*?\)', '', content)
                content = re.sub(r'!\[\s*\]\(\s*\)', '', content)

                # 仅修复 MkDocs 绝对路径 /main/... -> main/...
                content = re.sub(r'!\[([^\]]*)\]\(\s*/', r'![\1](', content)

                # 图片尺寸交给 LaTeX 全局控制
                output.append(content)
        else:
            print(f"⚠️ 文件不存在: {md_file}")

    Path('build').mkdir(exist_ok=True)
    Path('build/combined.md').write_text('\n'.join(output), encoding='utf-8')
    print(f"✅ 合并完成！共 {len(md_files)} 个文件 → build/combined.md")


if __name__ == "__main__":
    combine_markdown()
