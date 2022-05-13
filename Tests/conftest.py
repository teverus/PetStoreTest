from datetime import timedelta
from math import ceil

import pytest
from py.xml import html

from API.API import API


########################################################################################
#    Test fixtures                                                                     #
########################################################################################
@pytest.fixture(scope="module")
def api():
    """A fixture that returns the API of the application"""
    return API()


########################################################################################
#    HTML report fixtures                                                              #
########################################################################################
def pytest_html_report_title(report):
    """Changes the report's title"""

    report.title = "PetStore Testing"


def pytest_html_results_summary(prefix, summary, postfix):
    """This fixture creates an HTML report"""

    result_types = ["passed", "skipped", "failed", "error"]
    results = {}
    for element in summary:
        try:
            result_type = element.attr.class_
            if result_type in result_types:
                results[result_type] = int(element[0].split()[0])
        except AttributeError:
            pass

    total = sum([int(v) for v in list(results.values())])
    total_number_of_tests = total
    total_ran = total - results["skipped"]
    global_passed = ceil(results["passed"] / total_ran * 100) if total_ran else 0
    global_failed = 100 - global_passed

    total = 1 if not total else total

    time_total = ceil(float(summary[0][0].split()[-2]))
    time_minutes = int(time_total / 60)
    time_seconds = time_total % 60

    # Display results as a table
    prefix.extend(
        [
            html.table(
                html.tbody(
                    html.tr(
                        html.td(html.b("Test result")),
                        html.td(html.b("Number")),
                        html.td(html.b("Percentage")),
                    ),
                    html.tr(
                        html.td("Passed"),
                        html.td(f"{results['passed']}"),
                        html.td(f"{round(int(results['passed']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Skipped"),
                        html.td(f"{results['skipped']}"),
                        html.td(f"{round(int(results['skipped']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Failed"),
                        html.td(f"{results['failed']}"),
                        html.td(f"{round(int(results['failed']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Error"),
                        html.td(f"{results['error']}"),
                        html.td(f"{round(int(results['error']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Total number of tests"),
                        html.td(f"{total_number_of_tests}"),
                    ),
                    html.tr(
                        html.td(html.b("TOTAL EXECUTED")),
                        html.td(html.b(f"{total_ran}")),
                    ),
                    html.tr(
                        html.td(html.b("TOTAL TIME")),
                        html.td(html.b(f"00:{time_minutes:02}:{time_seconds:02}")),
                    ),
                )
            ),
            html.p(
                html.b("Pass rate "),
                f"|{'#' * global_passed}{'.' * global_failed}| {global_passed}%",
            ),
        ]
    )


def pytest_html_results_table_header(cells):
    # Removes default "Duration" and "Links" columns
    [cells.pop() for _ in range(3)]

    cells[0][0] = "Test name"
    cells.append(html.th("Path to test", class_="sortable"))
    cells.append(html.th("Result", class_="sortable"))
    cells.append(html.th("Duration", class_="sortable"))


def pytest_html_results_table_row(report, cells):
    # Removes default "Duration" and "Links" columns
    [cells.pop() for _ in range(3)]

    # Test name column
    test_name = report.location[2]
    cells[0][0] = test_name
    cells[0].attr.style = "color: black"

    # Path to Test
    path_to_file = report.location[0]
    cells.append(html.td(path_to_file))

    # Result column
    status = report.outcome
    test_status = {
        "passed": "green",
        "skipped": "orange",
        "failed": "red",
        "rerun": "orange",
    }
    cells.append(html.td(status.capitalize(), style=f"color: {test_status[status]}"))

    # Duration column
    cells.append(html.td(str(timedelta(seconds=report.duration)).split(".")[0]))
