from langgraph.graph import StateGraph, START, END

from src.state import CodeReviewState

from src.nodes.fetch_pr import fetch_pr
from src.nodes.analyze_code import analyze_code
from src.nodes.bug_detector import bug_detector
from src.nodes.security_checker import security_checker
from src.nodes.quality_checker import quality_checker
from src.nodes.aggregator import aggregate_findings
from src.nodes.report_generator import generate_report


# =========================================================
# Create Graph
# =========================================================

graph = StateGraph(CodeReviewState)


# =========================================================
# Add Nodes
# =========================================================

graph.add_node(
    "fetch_pr",
    fetch_pr
)

graph.add_node(
    "analyze_code",
    analyze_code
)

graph.add_node(
    "bug_detector",
    bug_detector
)

graph.add_node(
    "security_checker",
    security_checker
)

graph.add_node(
    "quality_checker",
    quality_checker
)

graph.add_node(
    "aggregate_findings",
    aggregate_findings
)

graph.add_node(
    "generate_report",
    generate_report
)


# =========================================================
# Edges
# =========================================================

graph.add_edge(
    START,
    "fetch_pr"
)

graph.add_edge(
    "fetch_pr",
    "analyze_code"
)


# Parallel reviewers

graph.add_edge(
    "analyze_code",
    "bug_detector"
)

graph.add_edge(
    "analyze_code",
    "security_checker"
)

graph.add_edge(
    "analyze_code",
    "quality_checker"
)


# Join reviewers

graph.add_edge(
    "bug_detector",
    "aggregate_findings"
)

graph.add_edge(
    "security_checker",
    "aggregate_findings"
)

graph.add_edge(
    "quality_checker",
    "aggregate_findings"
)


graph.add_edge(
    "aggregate_findings",
    "generate_report"
)

graph.add_edge(
    "generate_report",
    END
)


# =========================================================
# Compile
# =========================================================

workflow = graph.compile()