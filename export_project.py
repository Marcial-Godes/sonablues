from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIGURACIÓN
# =========================================================

ROOT_DIR = Path(".")

OUTPUT_FILE = "project_export.md"

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
    ".web",
    "node_modules",
    "dist",
    "build",
}

ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".css",
    ".scss",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".html",
    ".env",
}

LANGUAGE_MAP = {
    ".py": "python",
    ".md": "markdown",
    ".json": "json",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".css": "css",
    ".scss": "scss",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".jsx": "jsx",
    ".html": "html",
    ".txt": "text",
    ".env": "bash",
}


# =========================================================
# UTILIDADES
# =========================================================

def should_ignore(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def get_language(path: Path) -> str:
    return LANGUAGE_MAP.get(path.suffix.lower(), "text")


def build_tree(root: Path) -> str:
    lines = []

    for path in sorted(root.rglob("*")):

        if should_ignore(path):
            continue

        depth = len(path.relative_to(root).parts) - 1
        indent = "    " * depth

        if path.is_dir():
            lines.append(f"{indent}📁 {path.name}")
        else:
            lines.append(f"{indent}📄 {path.name}")

    return "\n".join(lines)


# =========================================================
# EXPORTACIÓN
# =========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    export_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -----------------------------------------------------
    # CABECERA
    # -----------------------------------------------------

    output.write("# EXPORTACIÓN DE PROYECTO\n\n")
    output.write(f"Fecha: {export_date}\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ÁRBOL DE ARCHIVOS
    # -----------------------------------------------------

    output.write("# ESTRUCTURA DEL PROYECTO\n\n")
    output.write("```text\n")
    output.write(build_tree(ROOT_DIR))
    output.write("\n```\n\n")

    output.write("---\n\n")

    # -----------------------------------------------------
    # ARCHIVOS
    # -----------------------------------------------------

    for path in sorted(ROOT_DIR.rglob("*")):

        if should_ignore(path):
            continue

        if not path.is_file():
            continue

        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        relative_path = path.relative_to(ROOT_DIR)
        language = get_language(path)

        try:
            content = path.read_text(encoding="utf-8")

        except Exception as e:
            content = f"[ERROR LEYENDO ARCHIVO: {e}]"

        output.write(f"# ARCHIVO: {relative_path}\n\n")

        output.write(f"```{language}\n")
        output.write(content)
        output.write("\n```\n\n")

        output.write("---\n\n")

print(f"\n✅ Proyecto exportado correctamente:")
print(f"📄 {OUTPUT_FILE}\n")