import os
import time
import json
from typing import Any, List, Optional, Union, Dict
from rich.console import Console
from rich.progress import * # type: ignore
from rich.columns import Columns
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.tree import Tree
from rich.layout import Layout
from rich.syntax import Syntax
from rich.rule import Rule
from rich.prompt import Prompt
from rich.traceback import install as install_traceback
from rich.pretty import Pretty
from rich.markdown import Markdown  # New Import

# ==========================================
# 1. Core Layout Engine
# ==========================================
class LayoutEngine:
    def __init__(self, console: Console):
        self._console = console

    def draw_rule(self, title: str = "", style: str = "bold blue"):
        self._console.print(Rule(title, style=style))

    def render_columns(self, content_list: List[Any], title: str = ""):
        panel_list = [Panel(str(c), title=f"{title} {i+1}", expand=True) for i, c in enumerate(content_list)]
        self._console.print(Columns(panel_list))

    def create_standard_layout(self) -> Layout:
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3),
        )
        layout["main"].split_row(
            Layout(name="side", size=30),
            Layout(name="body")
        )
        return layout

# ==========================================
# 2. Visualization Tools
# ==========================================
class VisualizationTool:
    def __init__(self, console: Console | Any):
        self._console = console

    def render_tree(self, data: Dict[str, Any], title: str = "Root"):
        def build_tree(current_tree: Tree, node_data: Any):
            if isinstance(node_data, dict):
                for k, v in node_data.items():
                    branch = current_tree.add(f"[bold cyan]{k}[/]")
                    build_tree(branch, v)
            elif isinstance(node_data, list):
                for item in node_data: build_tree(current_tree, item)
            else:
                current_tree.add(str(node_data))
        
        tree_obj = Tree(f"[bold yellow]{title}[/]")
        build_tree(tree_obj, data)
        self._console.print(tree_obj)

    def auto_table(self, data: Union[Dict, List[Dict]], title: str = ""):
        table = Table(title=title)
        if isinstance(data, dict):
            table.add_column("Key", style="cyan")
            table.add_column("Value", style="magenta")
            for k, v in data.items(): table.add_row(str(k), str(v))
        elif isinstance(data, list) and len(data) > 0:
            for k in data[0].keys(): table.add_column(k)
            for item in data: table.add_row(*[str(item.get(k, "")) for k in data[0].keys()])
        self._console.print(table)

    def render_code(self, code: str, language: str = "python"):
        self._console.print(Syntax(code, language, line_numbers=True, theme="monokai"))

    # --- New Feature: Markdown Rendering ---
    def render_markdown(self, md_text: str):
        """Renders beautiful Markdown text in the terminal"""
        self._console.print(Markdown(md_text))

    # --- New Feature: JSON Syntax Highlighting ---
    def render_json(self, data: Any):
        """Prints a prettified and colorized JSON string"""
        json_str = json.dumps(data, indent=4)
        self._console.print(Syntax(json_str, "json", theme="monokai"))

    def loading_status(self, message: str = "Processing...", spinner_type: str = "dots"):
        return self._console.status(message, spinner=spinner_type)

    def create_progress_bar(self) -> Progress:
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=self._console
        )

# ==========================================
# 3. Master Controller
# ==========================================
class MasterConsole:
    def __init__(self, pretty_exceptions: bool = True, record_mode: bool = True):
        self._console = Console(record=record_mode)
        self.layout = LayoutEngine(self._console)
        self.viz = VisualizationTool(self._console)

        if pretty_exceptions:
            install_traceback(console=self._console, show_locals=True)

    def output(self, *objects: Any, style: Optional[str] = None):
        for item in objects:
            if isinstance(item, (dict, list, tuple)):
                self._console.print(Pretty(item, expand_all=True))
            else:
                self._console.print(item, style=style)

    # --- New Feature: Quick Dashboard ---
    def quick_dashboard(self, left_content: Any, right_content: Any, title: str = "Dashboard"):
        """Displays a simple two-column dashboard layout"""
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="left", ratio=1)
        grid.add_row(
            Panel(str(left_content), title="System Info", border_style="green"),
            Panel(str(right_content), title="Activity Log", border_style="blue")
        )
        self._console.print(Panel(grid, title=title))

    def log(self, text: str):
        self._console.log(text)

    def ask(self, question: str, check_empty: bool = False) -> Optional[str]:
        answer = self._console.input(f"[bold yellow]?[/] {question}: ")
        if check_empty and not answer.strip():
            return None
        return answer

    def draw_line(self, title: str) -> None:
        self._console.rule(title)

    def safe_execute(self, func: Any, *args: Any, **kwargs: Any):
        try:
            return func(*args, **kwargs)
        except Exception:
            self._console.print_exception(show_locals=True)
            return None

    def export_output(self, filename: str = "output.html"):
        self._console.save_html(filename)
        self._console.log(f"Output saved to [bold green]{filename}[/]")